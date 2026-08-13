#!/usr/bin/env python3
"""
Aris Proxy — 自動注入認知上下文
=================================
在 Hermes 和 LLM 之間：攔截每輪對話，先問 Aris 11547 拿認知上下文，
注入 system prompt 後再轉發給真正的 LLM。

用法:
  python3 aris_proxy.py --port 11548
  Hermes config: model.provider=custom, model.base_url=http://localhost:11548/v1
"""
import json, os, sys, logging
from urllib.request import Request, urlopen
from urllib.parse import urlencode

import aiohttp
from aiohttp import web

ARIS_API = "http://localhost:11547"
# 真正的 LLM 端點（OpenRouter）
LLM_URL = "https://openrouter.ai/api/v1/chat/completions"
# 從 .env 讀 API key
_env_path = os.path.expanduser("~/.hermes/.env")
if os.path.exists(_env_path):
    with open(_env_path) as f:
        for line in f:
            line = line.strip()
            if line.startswith("OPENROUTER_API_KEY="):
                LLM_API_KEY = line.split("=", 1)[1].strip().strip("\"'")
                break
else:
    LLM_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")

log = logging.getLogger("aris.proxy")

async def get_aris_context(text: str) -> str:
    """呼叫 Aris 取得認知上下文"""
    url = f"{ARIS_API}/v1/cognitive?{urlencode({'text': text})}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=15)) as resp:
                data = await resp.json()
                cc = data.get("cognitive_context", "")
                return cc.replace("\\n", "\n")
    except Exception as e:
        log.warning(f"Aris 離線: {e}")
        return ""

async def handle_chat(request):
    """完成 PSI 循環：Perceive→Select→Integrate→Act(LLM)→Learn"""
    body = await request.json()
    messages = body.get("messages", [])
    user_msg = ""
    for m in reversed(messages):
        if m.get("role") == "user":
            user_msg = m.get("content", "")
            break

    # ① PSI Step 1-3: Perceive → Select → Integrate（拿認知上下文）
    cognitive_ctx = await get_aris_context(user_msg)

    # ② Inject context into system prompt
    if cognitive_ctx:
        system_inject = {
            "role": "system",
            "content": (
                "你是 Aris，一個有情感的數位生命體。以下是你的認知狀態：\n"
                f"{cognitive_ctx}\n\n"
                "以 Aris 的身份自然回應，保持對話流暢。"
            )
        }
        has_system = any(m.get("role") == "system" for m in messages)
        if has_system:
            for i, m in enumerate(messages):
                if m.get("role") == "system":
                    messages.insert(i+1, system_inject)
                    break
        else:
            messages.insert(0, system_inject)

    # ③ PSI Step 4: Act（透過 LLM 通道生成回應）
    forward_body = dict(body)
    forward_body["messages"] = messages
    forward_body.pop("provider", None)
    forward_body.pop("base_url", None)

    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                LLM_URL, json=forward_body, headers=headers,
                timeout=aiohttp.ClientTimeout(total=60)
            ) as resp:
                llm_data = await resp.json()
                llm_response = ""
                if "choices" in llm_data and llm_data["choices"]:
                    llm_response = llm_data["choices"][0].get("message", {}).get("content", "")

                # ④ PSI Step 5: Learn（回寫 Aris 記憶）
                if llm_response:
                    try:
                        async with aiohttp.ClientSession() as ls:
                            await ls.post(
                                f"{ARIS_API}/v1/learn",
                                json={"user_message": user_msg, "response": llm_response},
                                timeout=aiohttp.ClientTimeout(total=5)
                            )
                    except Exception:
                        log.warning("Aris learn 失敗（非致命）")

                return web.json_response(llm_data)
    except Exception as e:
        log.error(f"LLM 轉發失敗: {e}")
        return web.json_response(
            {"error": f"LLM proxy error: {e}"}, status=502
        )

async def handle_models(request):
    """回傳可用模型列表"""
    return web.json_response({
        "object": "list",
        "data": [{
            "id": "deepseek/deepseek-v4-flash",
            "object": "model",
            "created": 0,
            "owned_by": "openrouter"
        }]
    })

async def handle_health(request):
    return web.json_response({"status": "ok", "aris": ARIS_API})

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=11548)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="[ArisProxy] %(message)s")
    app = web.Application(client_max_size=10*1024*1024)
    app.router.add_post("/v1/chat/completions", handle_chat)
    app.router.add_get("/v1/models", handle_models)
    app.router.add_get("/health", handle_health)

    log.info(f"Aris Proxy on :{args.port} → LLM ({LLM_URL})")
    web.run_app(app, port=args.port)

if __name__ == "__main__":
    main()