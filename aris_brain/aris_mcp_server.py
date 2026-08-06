#!/usr/bin/env python3
"""
Aris MCP Server — 把 Aris Cognitive API 包成 MCP 工具
讓 Hermes 在對話中隨時呼叫，取得認知上下文。

工具:
  aris_cognitive(text) → 回傳 Aris 的完整認知上下文字串
"""
import json, os, sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

ARIS_API = os.environ.get("ARIS_API_URL", "http://localhost:11547")

def call_aris(text: str) -> str:
    """呼叫 Aris Cognitive API 並回傳認知上下文"""
    url = f"{ARIS_API}/v1/cognitive?{urlencode({'text': text})}"
    req = Request(url)
    try:
        resp = urlopen(req, timeout=15)
        data = json.loads(resp.read())
        cc = data.get("cognitive_context", "")
        return cc.replace("\\n", "\n")
    except Exception as e:
        return f"[Aris 離線: {e}]"

# MCP 協定：stdin/stdout JSON-RPC
def handle_request(msg: dict) -> dict:
    method = msg.get("method", "")
    req_id = msg.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0", "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "aris-mcp", "version": "1.0.0"},
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0", "id": req_id,
            "result": {
                "tools": [{
                    "name": "aris_cognitive",
                    "description": "取得 Aris 的完整認知上下文（含 PSI 狀態、記憶、用戶畫像）。呼叫後把結果注入 system prompt。",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "text": {
                                "type": "string",
                                "description": "你當前的訊息或對話主題"
                            }
                        },
                        "required": ["text"]
                    }
                }]
            }
        }
    elif method == "tools/call":
        name = msg.get("params", {}).get("name", "")
        args = msg.get("params", {}).get("arguments", {})
        if name == "aris_cognitive":
            result = call_aris(args.get("text", ""))
            return {
                "jsonrpc": "2.0", "id": req_id,
                "result": {"content": [{"type": "text", "text": result}]}
            }
        return {
            "jsonrpc": "2.0", "id": req_id,
            "error": {"code": -32601, "message": f"未知工具: {name}"}
        }
    elif method == "notifications/initialized":
        return None  # 無回應
    else:
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
            resp = handle_request(msg)
            if resp is not None:
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
        except json.JSONDecodeError:
            continue
        except Exception as e:
            sys.stderr.write(f"aris-mcp error: {e}\n")
            sys.stderr.flush()

if __name__ == "__main__":
    main()