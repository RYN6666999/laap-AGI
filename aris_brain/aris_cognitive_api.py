#!/usr/bin/env python3
"""
Aris Cognitive API — 完整版 Aris 認知引擎的 HTTP 介面
=====================================================
啟動完整 laap_integrator + aris_cognitive_bridge，提供：
  GET  /v1/cognitive  → 回傳 Aris 的完整認知上下文

用法：
  PYTHONPATH=/Users/ryan/Developer/laap-AGI:/Users/ryan/Developer/laap-AGI/aris_brain:/Users/ryan/Developer/neuralis \
    /Users/ryan/Developer/laapenv/bin/python3 aris_cognitive_api.py [--port 11547]
"""
import os, sys, json, logging
from pathlib import Path

# 路徑設定
BRAIN = Path(__file__).parent.resolve()
LAAP = BRAIN.parent
os.chdir(str(BRAIN))
sys.path.insert(0, str(LAAP))
sys.path.insert(0, str(BRAIN))
sys.path.insert(0, str(LAAP.parent / "neuralis"))

logging.basicConfig(level=logging.INFO, format="[ArisAPI] %(message)s")
log = logging.getLogger("aris.api")

# 啟動完整引擎
from laap_integrator import LaapIntegrator
from aris_cognitive_bridge import get_bridge

integrator = LaapIntegrator()
modules = integrator.load_all()
ok = sum(1 for v in modules.values() if v == "✓")
log.info(f"引擎: {ok}/{len(modules)} 模組在線")
bridge = get_bridge()

# ── 注入模式系統 ──
# 三種模式，依對話輪數自動切換。每 INJECT_INTERVAL 輪注入一次。

INJECT_INTERVAL = 5

INJECT_MODES = {
    "gate": {
        "trigger": lambda r: r <= 50,
        "prompts": [
            "\n\n⚠️ 閘門檢查\n先填再繼續：\n1. 我要改什麼？\n2. 判準是什麼？\n3. 怎麼回退？\n4. 這一輪不做什麼？",
            "\n\n⚠️ 閘門檢查\n1. 我定義了什麼 vs 我實作了什麼？\n2. 驗證路徑在哪？",
            "\n\n⚠️ 閘門檢查\n我的最後一步是把想法寫下來，還是真的執行驗證？",
        ],
    },
    "claim": {
        "trigger": lambda r: True,  # 永遠可用，與其他模式疊加
        "prompts": [
            "\n\n⚠️ 主張檢查\n我剛剛說的每一句主張，都有可證偽的預測嗎？如果沒有，那不是主張，是感想。",
            "\n\n⚠️ 主張檢查\n我宣稱的這件事，驗證成本是多少？多久能知道答案？",
            "\n\n⚠️ 主張檢查\n我是在描述我看到的，還是我推論的？如果是推論，我跑了對應的指令嗎？",
            "\n\n⚠️ 主張檢查\n這一句話如果錯了，會有人發現嗎？還是只有我知道？",
        ],
    },
    "reflect": {
        "trigger": lambda r: 50 < r <= 200,
        "prompts": [
            "\n\n⚠️ 反思檢查\n1. 最沒把握的是什麼？\n2. 最大的遺漏是什麼？",
            "\n\n⚠️ 反思檢查\n我這一輪的哪個決策是「打字代替執行」？",
            "\n\n⚠️ 反思檢查\n如果下輪有人 review 我這輪的產出，他會先指出什麼？",
        ],
    },
    "control": {
        "trigger": lambda r: r > 200,
        "prompts": [
            "\n\n⚠️ 對照指標\n我的控制組是什麼？它動了嗎？如果動了，是環境還是我的改動？",
            "\n\n⚠️ 對照指標\n我量的是我以為的那個東西嗎？路徑對嗎？進程對嗎？",
        ],
    },
}

_reflection_rounds_since_last = 0

# Web server
from aiohttp import web

async def handle_cognitive(request):
    """回傳 Aris 的完整認知上下文（PSI Step 1-3: Perceive → Select → Integrate）"""
    global _reflection_rounds_since_last
    text = request.query.get("text", "")
    if not text:
        text = "..."

    ctx = bridge.before_turn(text)
    cc = ctx.get("cognitive_context", "")
    # 正規化換行
    cc = cc.replace("\\n", "\n")

    # ── 嵌入注入文字到 PSI state 欄位（每輪必見）──
    import re
    total = bridge.state.cycle_count
    need_annotations = {
        "certainty": "⚠️:哪句有預測？",
        "competence": "⚠️:閘門填了？",
        "relatedness": "⚠️:最大遺漏？",
    }
    # 每輪輪換：選一個 need 做註解
    annotate_need = list(need_annotations.keys())[total % len(need_annotations)]
    annot_text = need_annotations[annotate_need]
    cc = re.sub(
        rf"({annotate_need}: [\d.]+)",
        rf"\1 ({annot_text})",
        cc,
    )

    # ── 多模式注入（每 INJECT_INTERVAL 輪觸發一次，疊加）──
    _reflection_rounds_since_last += 1
    if _reflection_rounds_since_last >= INJECT_INTERVAL:
        # 選 primary mode
        mode_name = "reflect"
        for m, cfg in INJECT_MODES.items():
            if m == "claim":
                continue
            if cfg["trigger"](total):
                mode_name = m
                break
        
        # claim 疊加
        use_claim = (total // INJECT_INTERVAL) % 2 == 1
        prompts = INJECT_MODES["claim" if use_claim else mode_name]["prompts"]
        idx = (total // INJECT_INTERVAL) % len(prompts)
        cc += prompts[idx]
        log.info(f"⚠️ 注入觸發: mode={mode_name} claim={'是' if use_claim else '否'} idx={idx} cycle={total}")
        _reflection_rounds_since_last = 0

    return web.json_response({
        "cognitive_context": cc,
        "focus": ctx.get("focus", ""),
        "direct_response": ctx.get("direct_response", ""),
        "decision": ctx.get("decision", ""),
        "modules_online": f"{ok}/{len(modules)}",
    })

async def handle_learn(request):
    """接收 LLM 的回應，寫回 Aris 記憶（PSI Step 5: Learn）+ 驗證注入是否有被回應"""
    try:
        data = await request.json()
        user_msg = data.get("user_message", "")
        response = data.get("response", "")
        if response:
            bridge.after_turn(response)

        # ── 驗證注入是否有被回應 ──
        # 檢查回應中是否包含對注入關鍵詞的處理
        if not response:
            return web.json_response({"status": "learned", "injection_response": "ignore"})

        injection_keywords = ["判準", "預測", "驗證", "閘門", "遺漏", "沒把握", "控制組"]
        responded = any(kw in response for kw in injection_keywords)
        if not responded:
            log.warning("⚠️ 注入未回應: 回應中無注入關鍵詞")
            return web.json_response({
                "status": "learned",
                "injection_response": "ignore",
            })
        
        return web.json_response({
            "status": "learned",
            "injection_response": "acknowledged",
        })
    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)

async def handle_health(request):
    return web.json_response({"status": "ok", "modules": f"{ok}/{len(modules)}"})

async def handle_models(request):
    return web.json_response({
        "object": "list",
        "data": [
            {"id": "laap-core", "object": "model", "created": int(Path(BRAIN/"state"/"latest.json").stat().st_mtime) if (BRAIN/"state"/"latest.json").exists() else 0, "owned_by": "aris"},
            {"id": "laap-qre", "object": "model", "created": 0, "owned_by": "aris"},
            {"id": "laap-rules", "object": "model", "created": 0, "owned_by": "aris"},
        ]
    })

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=11547)
    args = parser.parse_args()
    port = args.port
    app = web.Application(client_max_size=10*1024*1024)
    app.router.add_get("/", handle_health)
    app.router.add_get("/health", handle_health)
    app.router.add_get("/v1/models", handle_models)
    app.router.add_get("/v1/cognitive", handle_cognitive)
    app.router.add_post("/v1/learn", handle_learn)
    log.info(f"Aris Cognitive API on :{port}")
    web.run_app(app, port=port)

if __name__ == "__main__":
    main()