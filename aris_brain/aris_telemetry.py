"""
Aris Telemetry v1 — 育種基線專用埋點模組
===========================================
純觀察，不介入。只加 log，不改行為。

四條測量線：
  1. gbrain 讀寫成敗
  2. 記憶檢索有沒有回傳
  3. 檢索結果有沒有被用進回應
  4. 「⟶下一步」有沒有變成真的 tool call

每筆記錄寫到 state/telemetry.jsonl（append-only JSON Lines）。
"""

import json, logging, time, os, re
from pathlib import Path
from typing import Optional

logger = logging.getLogger("aris.telemetry")

# ── 狀態目錄 ────────────────────────────────────────────────
STATE_DIR = Path(__file__).parent / "state"
STATE_DIR.mkdir(parents=True, exist_ok=True)
TELEMETRY_FILE = STATE_DIR / "telemetry.jsonl"

# ── 跨輪追蹤（session 內狀態，不持久化） ──────────────────
_last_attention: Optional[str] = None  # 上一輪的 ⟶下一步 文字
_last_memory_context: Optional[str] = None  # 上一輪注入的記憶內容


# ════════════════════════════════════════════════════════════
# 測量 1: gbrain 讀寫成敗
# ════════════════════════════════════════════════════════════

def log_gbrain(method: str, endpoint: str, success: bool, latency_ms: float,
               detail: str = ""):
    """記錄一次 gbrain 操作。

    Args:
        method: query / search / get_page / put_page / health
        endpoint: 完整 URL 或工具名
        success: 是否成功
        latency_ms: 耗時（毫秒）
        detail: 錯誤訊息或結果摘要
    """
    _write({
        "type": "gbrain",
        "method": method,
        "endpoint": endpoint[:80],
        "success": success,
        "latency_ms": round(latency_ms, 1),
        "detail": detail[:200],
        "ts": time.time(),
    })


# ════════════════════════════════════════════════════════════
# 測量 2: 記憶檢索有沒有回傳
# ════════════════════════════════════════════════════════════

def log_memory_retrieval(source: str, query_len: int, returned: int,
                         layers: str):
    """記錄一次記憶檢索。

    Args:
        source: perceive / get_memory_context / recall_related
        query_len: 查詢字串長度
        returned: 回傳的 fragment 數量
        layers: 查詢的層級（core / episodic / working）
    """
    _write({
        "type": "memory_retrieval",
        "source": source,
        "query_len": query_len,
        "returned": returned,
        "layers": layers,
        "ts": time.time(),
    })


# ════════════════════════════════════════════════════════════
# 測量 3: 檢索結果有沒有被用進回應
# ════════════════════════════════════════════════════════════

def check_memory_used_in_response(memory_context: str, response: str):
    """檢查記憶內容是否出現在 Aris 的回應中。

    Args:
        memory_context: 注入的記憶文字
        response: Aris 的回應文字
    """
    global _last_memory_context
    _last_memory_context = memory_context

    if not memory_context or not response:
        return

    # 簡單檢查：記憶中的關鍵詞是否出現在回應中
    # 取記憶中每條 fragment 的前 20 字作為 signature
    fragments = memory_context.split("；")
    used_count = 0
    for frag in fragments:
        sig = frag.strip()[:20]
        if sig and len(sig) > 5 and sig in response:
            used_count += 1

    _write({
        "type": "memory_used_in_response",
        "memory_fragments": len(fragments),
        "used_in_response": used_count,
        "used_ratio": round(used_count / max(1, len(fragments)), 2),
        "response_len": len(response),
        "ts": time.time(),
    })


# ════════════════════════════════════════════════════════════
# 測量 4: 「⟶下一步」有沒有變成真的 tool call
# ════════════════════════════════════════════════════════════

def log_next_step(attention_text: str):
    """記錄 Aris 說的「⟶下一步」內容。

    Args:
        attention_text: 注意力文字（下一步要做的事）
    """
    global _last_attention
    _last_attention = attention_text
    _write({
        "type": "next_step_planned",
        "attention": attention_text[:200],
        "ts": time.time(),
    })


def check_next_step_executed(actual_action: str, route: str = ""):
    """檢查上一步的「⟶下一步」是否被執行。

    在 Aris 做出實際行動時呼叫。

    Args:
        actual_action: 實際執行的行動描述
        route: 路由鍵（如 "gbrain", "research"）
    """
    global _last_attention
    if not _last_attention:
        return

    planned = _last_attention.lower()
    actual = actual_action.lower()

    # 寬鬆匹配：計畫文字中的關鍵詞是否出現在實際行動中
    # 取計劃的前 3 個中文/英文詞
    plan_words = set(re.findall(r'[\w\u4e00-\u9fff]{2,}', planned))
    actual_words = set(re.findall(r'[\w\u4e00-\u9fff]{2,}', actual))
    overlap = plan_words & actual_words

    executed = len(overlap) >= 2 or route.lower() in planned
    _write({
        "type": "next_step_executed",
        "planned": _last_attention[:200],
        "actual": actual_action[:200],
        "route": route,
        "word_overlap": len(overlap),
        "executed": executed,
        "plan_words": list(plan_words)[:10],
        "actual_words": list(actual_words)[:10],
        "ts": time.time(),
    })
    _last_attention = None  # 已檢查，清空


# ════════════════════════════════════════════════════════════
# 寫入
# ════════════════════════════════════════════════════════════

def _write(entry: dict):
    """寫一條 telemetry 記錄到 append-only JSONL。"""
    try:
        with open(TELEMETRY_FILE, "a") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        logger.debug(f"[Telemetry] write failed: {e}")


# ════════════════════════════════════════════════════════════
# 匯出（供基線腳本使用）
# ════════════════════════════════════════════════════════════

def get_telemetry_path() -> str:
    """回傳 telemetry 檔案路徑。"""
    return str(TELEMETRY_FILE)


def get_round_summary(round_number: int = None) -> dict:
    """計算到目前為止的匯總統計。

    Args:
        round_number: 可選，指定第幾輪（基於記錄數量/100 推算）
    """
    records = []
    if TELEMETRY_FILE.exists():
        with open(TELEMETRY_FILE) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        records.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue

    if not records:
        return {"total_records": 0}

    # 分類統計
    gbrain_records = [r for r in records if r.get("type") == "gbrain"]
    memory_records = [r for r in records if r.get("type") == "memory_retrieval"]
    usage_records = [r for r in records if r.get("type") == "memory_used_in_response"]
    plan_records = [r for r in records if r.get("type") == "next_step_planned"]
    exec_records = [r for r in records if r.get("type") == "next_step_executed"]

    gbrain_ok = sum(1 for r in gbrain_records if r.get("success"))
    exec_ok = sum(1 for r in exec_records if r.get("executed"))

    return {
        "total_records": len(records),
        "gbrain": {
            "total": len(gbrain_records),
            "success": gbrain_ok,
            "rate": round(gbrain_ok / max(1, len(gbrain_records)), 3),
        },
        "memory_retrieval": {
            "total": len(memory_records),
            "with_results": sum(1 for r in memory_records if r.get("returned", 0) > 0),
            "empty": sum(1 for r in memory_records if r.get("returned", 0) == 0),
        },
        "memory_usage": {
            "total": len(usage_records),
            "avg_used_ratio": round(
                sum(r.get("used_ratio", 0) for r in usage_records) / max(1, len(usage_records)), 3),
        },
        "next_step": {
            "planned": len(plan_records),
            "executed": exec_ok,
            "execution_rate": round(exec_ok / max(1, len(plan_records)), 3),
        },
    }