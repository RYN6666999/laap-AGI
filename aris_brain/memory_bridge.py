"""
LAAP Memory Bridge — minimal fallback implementation.

Provides the public interface expected by aris_cognitive_bridge and
laap_integrator when the full memory bridge is not available.
"""
from __future__ import annotations

from typing import List

from memory_store import MemoryFragment, MemoryStore


_store: MemoryStore | None = None


def _get_store() -> MemoryStore:
    global _store
    if _store is None:
        _store = MemoryStore()
    return _store


def get_memory_context(max_core: int = 3, max_recent: int = 3, max_working: int = 2) -> str:
    """Return a short memory context string for prompt injection."""
    store = _get_store()
    parts: List[str] = []

    core = store.query(layer="core", top_k=max_core)
    if core:
        parts.append("[核心记忆] " + "；".join(f.content[:80] for f in core))

    recent = store.query(layer="episodic", top_k=max_recent)
    if recent:
        parts.append("[最近经历] " + "；".join(f.content[:80] for f in recent))

    working = store.query(layer="working", top_k=max_working)
    if working:
        parts.append("[当前工作记忆] " + "；".join(f.content[:60] for f in working))

    return "\n".join(parts)


def recall_related(query: str, top_k: int = 3) -> List[MemoryFragment]:
    """Return memory fragments related to the query.

    2026-08-12 修復（live 實際載入的是本檔，不是 neuralis overlay 版）：
      - 舊版 query_words 白話 split()：中文整句交集必 0（跨對話記憶全黑）。
      - 新版：標點/空白切詞 + CJK 長詞補頭尾 2 字；任一詞命中 content 即算分。
      - 再補 gbrain 遠端（laap/memory/* 頁，2026-08-12 種子）——本機 _fragments
        冷啟動是空的，種子記憶在 gbrain。
    """
    import re as _re
    store = _get_store()
    toks = [
        t for t in _re.split(r"[\s\u3000，。！？、；：,.!?;:（）()/\\_'\"\-]+", query.lower())
        if len(t) >= 2
    ]
    ext = []
    for t in list(toks):
        if len(t) > 4 and _re.search(r"[\u4e00-\u9fff]", t):
            ext += [t[:2], t[-2:]]
    toks += ext

    scored = []
    for f in store._fragments:
        c = f.content.lower()
        hit = sum(1 for t in toks if t in c)
        if hit > 0:
            scored.append((hit, f))
    scored.sort(key=lambda x: x[0], reverse=True)
    local = [f for _, f in scored[:top_k]]

    # gbrain 遠端兜底（本機冷啟動空 + 種子記憶住在 gbrain laap/memory/*）
    try:
        from gbrain_client import get_client, hybrid_hits
        client = get_client()
        if client is not None:
            remote = []
            seen = {f.id for f in local} if hasattr(local[0], "id") else set()
            def _fmt(h):
                return (h.get("chunk_text") or "")[:160]
            try:
                hits = hybrid_hits(client, " ".join(toks[:8]), top_k * 3)
                remote += [_fmt(h) for h in hits or []]
            except Exception:
                pass
            if not remote:
                for t in toks[:6]:
                    try:
                        for h in hybrid_hits(client, t, top_k * 3):
                            remote.append(_fmt(h))
                    except Exception:
                        continue
            frags = []
            for i, text in enumerate(remote):
                if not text or len(text) < 4:
                    continue
                frags.append(MemoryFragment(content=text, layer="core",
                                            importance=0.9, topics=[]))
                if len(frags) >= top_k:
                    break
            return (local + frags)[:top_k]
    except Exception:
        pass
    return local


def store_important(content: str, layer: str = "episodic", importance: float = 0.7, topics: List[str] | None = None) -> None:
    """Store an important memory fragment."""
    store = _get_store()
    fragment = MemoryFragment(
        content=content,
        layer=layer,
        importance=importance,
        topics=topics or [],
    )
    store.store(fragment)
