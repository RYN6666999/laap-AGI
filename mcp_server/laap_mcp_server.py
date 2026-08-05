"""
LAAP Brain MCP Server
=====================

Exposes LAAP cognitive capabilities as MCP tools for Hermes Agent.

Run in stdio mode (default, for Hermes mcp_servers):
    python mcp_server/laap_mcp_server.py

Run in SSE mode:
    python mcp_server/laap_mcp_server.py --sse --port 11547

Tools:
    laap_cognitive_state  - get PSI cognitive state for a user input
    laap_recall_memory    - recall relevant memories from LAAP
    laap_store_memory     - store a memory page into gbrain
    laap_bootstrap        - awaken a new LAAP instance
    laap_reflect          - reflect on a completed turn
    laap_express          - get TTS + Live2D expression parameters
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Make LAAP brain modules importable
LAAP_ROOT = Path(__file__).resolve().parent.parent
ARIS_BRAIN = LAAP_ROOT / "aris_brain"
sys.path.insert(0, str(ARIS_BRAIN))
sys.path.insert(0, str(ARIS_BRAIN / "psi_jspace_bridge"))

import requests
from mcp.server.fastmcp import FastMCP

# gbrain_client for memory writes (imported from neuralis via PYTHONPATH)
_GBRAIN_CLIENT = None


def _get_gbrain_client():
    """Lazy import gbrain_client — only loaded when laap_store_memory is called."""
    global _GBRAIN_CLIENT
    if _GBRAIN_CLIENT is None:
        try:
            from gbrain_client import get_client as _get_client
            _GBRAIN_CLIENT = _get_client()
        except Exception as e:
            return {"error": f"gbrain_client import failed: {e}"}
    return _GBRAIN_CLIENT

LAAP_API_BASE = os.environ.get("LAAP_API_BASE", "http://localhost:11546")

mcp = FastMCP("laap-brain")


def _laap_post(endpoint: str, payload: dict) -> dict:
    """Call LAAP HTTP API and return JSON."""
    try:
        resp = requests.post(
            f"{LAAP_API_BASE}{endpoint}",
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e), "source": "laap_mcp_server"}


@mcp.tool()
def laap_cognitive_state(input: str) -> str:
    """
    Get LAAP PSI cognitive state for the given user input.

    Returns a preamble that should be injected into the system prompt
    to modulate tone, attention, and response style.

    Args:
        input: The user's message for this turn.
    """
    result = _laap_post("/v1/cognitive_state", {"input": input})
    if "error" in result:
        return json.dumps({"laap_error": result["error"]}, ensure_ascii=False)

    return json.dumps(
        {
            "preamble": result.get("preamble", ""),
            "cot_hint": result.get("cot_hint", ""),
            "dominant_need": _get_dominant_need(result.get("state", {})),
            "attention_focus": result.get("state", {}).get("attention_focus", ""),
            "mood": result.get("state", {}).get("mood", ""),
            "needs": result.get("state", {}).get("needs", {}),
        },
        ensure_ascii=False,
        indent=2,
    )


@mcp.tool()
def laap_recall_memory(query: str, limit: int = 5) -> str:
    """
    Recall memories from LAAP memory hierarchy relevant to the query.

    Args:
        query: Search query for memory recall.
        limit: Maximum number of memories to return (default 5).
    """
    result = _laap_post("/v1/recall_memory", {"query": query, "limit": limit})
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def laap_bootstrap(user_name: str = "friend", preset: str = "") -> str:
    """
    Awaken a new LAAP instance / trigger the Aris awakening ceremony.

    Args:
        user_name: Name of the user awakening LAAP.
        preset: Optional personality preset.
    """
    payload = {"user_name": user_name}
    if preset:
        payload["preset"] = preset
    result = _laap_post("/v1/bootstrap", payload)
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def laap_reflect(output: str, success: bool = False, connection: bool = False) -> str:
    """
    Reflect on a completed assistant turn and update LAAP PSI state.

    Args:
        output: The assistant's final output for this turn.
        success: Whether the turn was successful/useful.
        connection: Whether the turn strengthened user connection.
    """
    feedback = {"success": success, "connection": connection}
    result = _laap_post("/v1/reflect", {"output": output, "feedback": feedback})
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def laap_express(input: str) -> str:
    """
    Get TTS + Live2D expression parameters for the current LAAP cognitive state.

    Use this when you want to make Aris's voice and avatar match her mood.

    Args:
        input: The user's message for this turn (used to update cognitive state).
    """
    result = _laap_post("/v1/express", {"input": input})
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def laap_store_memory(content: str, slug: str = "", tags: str = "") -> str:
    """
    Store a memory page into gbrain (LAAP long-term memory).

    Content is written as a gbrain page that can be recalled later via
    laap_recall_memory. Use this to persist important notes, decisions,
    observations, or summaries.

    Args:
        content: Full markdown content of the memory page to store.
        slug: Optional URL-friendly identifier. Auto-generated from content
              if omitted (first 48 chars, lowercased, hyphenated).
        tags: Optional comma-separated tags for categorization.
    """
    import hashlib, re

    client = _get_gbrain_client()
    if isinstance(client, dict) and "error" in client:
        return json.dumps(client, ensure_ascii=False, indent=2)
    if client is None:
        return json.dumps(
            {"error": "gbrain client unavailable (binary not found or spawn failed)"},
            ensure_ascii=False,
            indent=2,
        )

    if not slug:
        safe = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff_-]", "-", content[:48].strip().lower())
        slug = safe.strip("-") or hashlib.md5(content.encode()).hexdigest()[:12]

    # Optionally prepend tags as frontmatter
    if tags:
        tag_lines = "\n".join(f"  - {t.strip()}" for t in tags.split(",") if t.strip())
        page_content = f"---\ntags:\n{tag_lines}\n---\n\n{content}"
    else:
        page_content = content

    try:
        result = client.call("put_page", {"slug": slug, "content": page_content}, timeout=30.0)
        return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e), "source": "laap_store_memory"}, ensure_ascii=False, indent=2)


def _get_dominant_need(state: dict) -> str:
    needs = state.get("needs", {})
    if not needs:
        return "explore"
    return max(needs, key=lambda k: needs.get(k, 0))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LAAP Brain MCP Server")
    parser.add_argument("--sse", action="store_true", help="Run in SSE mode")
    parser.add_argument("--port", type=int, default=11547, help="SSE port")
    args = parser.parse_args()

    if args.sse:
        mcp.run(transport="sse", port=args.port)
    else:
        mcp.run(transport="stdio")
