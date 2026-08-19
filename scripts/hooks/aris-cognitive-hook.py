#!/usr/bin/env python3
"""aris-cognitive-hook.py — pre_llm_call + pre_tool_call dual hook for Hermes.

pre_llm_call: calls /v1/cognitive, injects context + writes gate state
pre_tool_call: blocks destructive tools if gate wasn't honored
"""
import json, sys, os, urllib.request, urllib.parse

ARIS_API = os.environ.get("ARIS_API_URL", "http://localhost:11547")
STATE_FILE = "/tmp/aris-gate-state.json"

# Tools that modify files — block if gate not honored
DESTRUCTIVE_TOOLS = {"write_file", "patch", "terminal"}

def call_cognitive(user_msg: str) -> dict:
    """Call API and return cognitive context + injection mode."""
    # 2026-08-19 V1.5：原本是 str(user_msg)[:200]，Ryan 常貼整篇長文，
    # 後半段關鍵字全被砍掉 → 中文關鍵字腳白搭（記憶裡有那個詞，但問句被截了）。
    #
    # 不是把 200 調大就好：URL query 塞不下長文。實測 2400 字中文 quote 後約
    # 21600 bytes，遠超 aiohttp 預設 max_line_size 8190。所以改走 POST body。
    # 11547 的 /v1/cognitive 同時掛了 GET 與 POST，GET 仍可用（短句/手動測試）。
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
    """Inject cognitive context + write gate state file."""
    user_msg = data.get("extra", {}).get("user_input", "") or "."
    result = call_cognitive(user_msg)
    cc = result.get("cognitive_context", "")

    # Write gate state for pre_tool_call to read
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

    # Read gate state
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