"""原子 JSON 寫入 — 防 torn write。

問題：state/*.json 多處用 write_text() / open(w)，先 truncate 再寫。
若進程在寫入中被 kill（watchdog / launchd / SIGKILL），檔案剩半截 JSON，
下次 load 走 except → 靜默 fallback 到 hardcoded 預設 → 認知連續性歸零。

用法：
    from atomic_json import write_json
    write_json(path, data)

同房既有正確樣式：psi_jspace_bridge/psi_bridge.py:139-145
"""
import json
import os
import tempfile
from pathlib import Path


def write_json(path, data, indent: int = 2) -> bool:
    """原子寫 JSON。成功回 True，失敗回 False（不拋，由呼叫端決定）。

    tmp 與目標同目錄（os.replace 要求同一 filesystem），寫完 fsync 再 rename。
    rename 在 POSIX 是原子的：讀者只會看到舊檔或新檔，不會看到半截。
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(p.parent), prefix=p.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, p)
        return True
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        return False


if __name__ == "__main__":
    # self-check：寫入後可讀回，且過程中目標檔從不處於半截狀態
    import shutil
    d = tempfile.mkdtemp()
    try:
        t = Path(d) / "sub" / "s.json"
        payload = {"cycle": 61, "zh": "認知狀態", "nested": {"a": [1, 2, 3]}}
        assert write_json(t, payload) is True
        assert json.loads(t.read_text(encoding="utf-8")) == payload

        # 覆寫成較小內容：若非原子，殘留舊尾巴會讓 json.loads 失敗
        assert write_json(t, {"x": 1}) is True
        assert json.loads(t.read_text(encoding="utf-8")) == {"x": 1}

        # 不可序列化 → 回 False，且目標檔維持前一版（未被 truncate）
        assert write_json(t, {"bad": object()}) is False
        assert json.loads(t.read_text(encoding="utf-8")) == {"x": 1}

        # 無殘留 tmp
        assert [f for f in os.listdir(t.parent) if f.endswith(".tmp")] == []
        print("atomic_json self-check OK")
    finally:
        shutil.rmtree(d)
