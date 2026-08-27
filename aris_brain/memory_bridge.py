"""
LAAP Memory Bridge — stub (2026-08-27 收斂).

已由 aris-memory.py（:11551）取代所有實際記憶功能。
此 stub 僅保留 import 相容性，永遠回空。
"""
from __future__ import annotations

from typing import List

from memory_store import MemoryFragment, MemoryStore


def get_memory_context(max_core: int = 3, max_recent: int = 3, max_working: int = 2) -> str:
    """Stub — 永遠回空。"""
    return ""


def recall_related(query: str, top_k: int = 3) -> List[MemoryFragment]:
    """Stub — 永遠回空。"""
    return []


def store_important(content: str, layer: str = "episodic", importance: float = 0.5, topics: List[str] = None) -> None:
    """Stub — 不儲存。"""
    pass