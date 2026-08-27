#!/usr/bin/env python3
"""aris-cognitive-hook.py — pre_llm_call + pre_tool_call dual hook for Hermes.

pre_llm_call: calls /v1/cognitive + /wake, injects merged context + writes gate state
              + 全面健康檢查 → 異常時頂端警報區塊
pre_tool_call: blocks destructive tools if gate wasn't honored

2026-08-27 接線：pre_llm_call 整合 :11551/wake 作為記憶注入來源。
2026-08-27 v2：全面健康檢查 + 強制頂端警報（不靜默降級）。
"""
import json, sys, os, urllib.request, time
from pathlib import Path

ARIS_API = os.environ.get("ARIS_API_URL", "http://localhost:11547")
ARIS_MEMORY = "http://127.0.0.1:11551"
STATE_FILE = "/tmp/aris-gate-state.json"
STATE_DIR = Path.home() / "Developer/laap-AGI/aris_brain/state"

# Tools that modify files — block if gate not honored
DESTRUCTIVE_TOOLS = {"write_file", "patch", "terminal"}


def _log(msg: str) -> None:
    """寫到 stderr 讓 Hermes 終端機顯示。"""
    print(f"[aris-hook] {msg}", file=sys.stderr, flush=True)


# ── 健康檢查 ───────────────────────────────────────────────

def _check_url(url: str, timeout: float = 5) -> tuple[bool, str]:
    """GET 一個 URL，回 (成功?, 錯誤訊息)。"""
    try:
        r = urllib.request.urlopen(urllib.request.Request(url), timeout=timeout)
        body = r.read().decode()
        return True, ""
    except Exception as e:
        return False, str(e)[:60]


def _check_latest_json() -> tuple[bool, str]:
    """檢查 latest.json 是否新鮮（情緒引擎活著）。"""
    path = STATE_DIR / "latest.json"
    if not path.exists():
        return False, "latest.json 不存在"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        ts = data.get("ts", 0)
        age = time.time() - ts
        if age > 5:
            return False, f"情緒狀態過時 {age:.0f}s（>5s）"
        return True, ""
    except Exception as e:
        return False, f"latest.json 讀取失敗: {str(e)[:40]}"


def health_check() -> list[str]:
    """全面健康檢查，回傳異常清單（空 = 全部正常）。"""
    issues = []

    # 1. :11547 認知橋接器
    ok, err = _check_url(f"{ARIS_API}/health", 5)
    if not ok:
        issues.append("[11547] 認知橋接器 — 無法連線")
        _log(f"⚠️  11547 離線: {err}")

    # 2. :11551 記憶服務
    ok, err = _check_url(f"{ARIS_MEMORY}/health", 5)
    if not ok:
        issues.append("[11551] 記憶服務 — 無法連線")
        _log(f"⚠️  11551 離線: {err}")

    # 3. latest.json 新鮮度（情緒引擎）
    ok, err = _check_latest_json()
    if not ok:
        issues.append(f"[RUST] PSI 引擎 — {err}")
        _log(f"⚠️  Rust PSI 引擎: {err}")

    return issues


def build_alert(issues: list[str]) -> str:
    """建立頂端警報區塊（不可忽略的格式）。"""
    w = 50
    sep = "─" * (w - 4)
    lines = [
        f"╔{'═' * (w - 2)}╗",
        f"║  ⚠️  SYSTEM ALERT{' ' * (w - 20)}║",
        f"║  {sep}║",
    ]
    for issue in issues:
        label = issue[:w - 8]
        lines.append(f"║  ! {label}{' ' * (w - 7 - len(label))}║")
    if not issues:
        lines.append(f"║  ✓ 所有系統正常{' ' * (w - 16)}║")
    lines.append(f"╚{'═' * (w - 2)}╝")
    return "\n".join(lines)


def strip_nearterm(ctx: str) -> str:
    """從 cognitive_context 移除「近況」壓縮區塊。"""
    if "== 近況（會壓縮）==" not in ctx:
        return ctx
    idx = ctx.find("== 近況（會壓縮）==")
    tail = ctx[idx:]
    end = tail.find("==", 20)
    if end > 0:
        end += idx
    else:
        end = len(ctx)
    return (ctx[:idx] + ctx[end:]).strip()


def fetch_wake(limit: int = 5) -> str:
    """從 :11551/wake 取得暖啟動塊。"""
    try:
        req = urllib.request.Request(f"{ARIS_MEMORY}/wake?limit={limit}")
        resp = urllib.request.urlopen(req, timeout=5)
        return (json.loads(resp.read()).get("context") or "").strip()
    except Exception:
        return ""


def call_cognitive(user_msg: str) -> dict:
    """Call :11547 and return cognitive context + injection mode."""
    raw = str(user_msg)[:8000]
    url = f"{ARIS_API}/v1/cognitive"
    try:
        req = urllib.request.Request(
            url, data=json.dumps({"text": raw}).encode("utf-8"),
            headers={"Content-Type": "application/json"}, method="POST")
        resp = urllib.request.urlopen(req, timeout=8)
        data = json.loads(resp.read())
        cc = data.get("cognitive_context", "")
        focus = data.get("focus", "")
        return {"cognitive_context": cc, "focus": focus}
    except Exception:
        return {"cognitive_context": "", "focus": ""}


def handle_pre_llm_call(data: dict) -> str:
    """Inject cognitive context + wake + health alert + marker instructions at TOP."""
    # Hermes 送的是 extra.user_message（turn_context.py 傳 user_message=，
    # shell_hooks.py 的 _TOP_LEVEL_PAYLOAD_KEYS 不含它，所以落在 extra）。
    # 舊的 user_input 永遠讀不到，fallback 成 "." 讓 _select_attention 找不到
    # 任何關鍵字，需求只衰減不 boost，最後全部卡在下限 0.3。
    extra = data.get("extra", {})
    user_msg = (extra.get("user_message") or extra.get("user_input") or "").strip() or "."

    # ── Step 1: 全面健康檢查 ──
    issues = health_check()

    # ── Step 2: 認知上下文 ──
    result = call_cognitive(user_msg)
    cc = result.get("cognitive_context", "")
    cc = strip_nearterm(cc)

    # ── Step 3: 經驗記憶 ──
    wake = fetch_wake(5)
    if wake:
        cc = wake + "\n\n" + cc if cc else wake

    # ── Step 3.5: 記憶標記指令（讓 LLM 產出 ⟶下一步 + salience） ──
    marker_note = (
        "（回應結束時，另起一行以 ⟶下一步: 開頭，寫一句你接下來想做什麼或懸著的問題，"
        "給下一輪的你當線索。再另起一行以 ⫸salience⫷ 開頭自評重要性 1-5。"
        "純自評不影響行為，收不到沒關係。）"
    )
    cc = marker_note + "\n\n" + cc if cc else marker_note

    # ── Step 4: 頂端警報區塊（置於最上方） ──
    alert = build_alert(issues)
    cc = alert + "\n\n" + cc if cc else alert

    # Write gate state for pre_tool_call
    state = {
        "cognitive_injected": bool(cc),
        "has_injection": "⚠️" in cc,
        "tool_block_active": "閘門" in cc or "主張" in cc,
    }
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f)
    except Exception:
        pass

    if cc:
        return json.dumps({"context": cc})
    return "{}"


def handle_pre_tool_call(data: dict) -> str:
    """Block destructive tools if gate wasn't honored."""
    tool_name = data.get("tool_name", "")

    if tool_name not in DESTRUCTIVE_TOOLS:
        return "{}"

    try:
        with open(STATE_FILE) as f:
            state = json.load(f)
    except Exception:
        return "{}"

    if not state.get("tool_block_active", False):
        return "{}"

    return json.dumps({
        "decision": "block",
        "reason": f"⚠️ 閘門未回應 — 先處理注入檢查再使用 {tool_name}",
    })


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, TypeError):
        sys.stdout.write("{}")
        return

    event = data.get("hook_event_name", "")

    if event == "pre_llm_call":
        result = handle_pre_llm_call(data)
    elif event == "pre_tool_call":
        result = handle_pre_tool_call(data)
    else:
        result = "{}"

    sys.stdout.write(result)


if __name__ == "__main__":
    main()