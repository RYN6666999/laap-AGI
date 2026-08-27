"""
LAAP Memory Store — stub (2026-08-27 收斂).

已由 aris-memory.py（:11551）取代所有實際記憶功能。
此 stub 僅保留 import 相容性，不儲存、不讀取任何資料。
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class MemoryFragment:
    """Stub — 不儲存內容。"""
    content: str = ""
    layer: str = "episodic"
    importance: float = 0.5
    topics: List[str] = field(default_factory=list)
    timestamp: float = field(default_factory=time.time)
    fragment_id: str = "stub"


class MemoryStore:
    """Stub — 永遠空。"""

    def __init__(self, state_dir: Optional[Path] = None):
        self._fragments: List[MemoryFragment] = []

    def store(self, fragment: MemoryFragment) -> None:
        pass

    def query(self, layer: Optional[str] = None, top_k: int = 5) -> List[MemoryFragment]:
        return []

    def get_stats(self) -> Dict[str, int]:
        return {"total": 0, "core": 0, "episodic": 0, "working": 0}

    def get_memory_embedding(self, query: str = "", layer: str = "episodic", top_k: int = 3) -> Any:
        return None


# ── 輔助函數 stub ──────────────────────────────────────────

def _query_tokens(query: str, limit: int = 8) -> str:
    return ""

def _memory_first(hits: list) -> list:
    return hits or []

def hybrid_hits_any(client, query: str, limit: int) -> list:
    return []