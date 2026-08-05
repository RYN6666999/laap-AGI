#!/usr/bin/env python3
"""psi-adapter: 讀 rust-latest.json → 映射成 Aris 格式 → 寫 latest.json"""
import json
import time
from pathlib import Path

RUST_FILE = Path(__file__).parent / "state" / "rust-latest.json"
LATEST_FILE = Path(__file__).parent / "state" / "latest.json"

while True:
    try:
        raw = json.loads(RUST_FILE.read_text())
        mapped = {
            "schema": "neuralis-rust-psi/v1",
            "tick": raw.get("tick", 0),
            "cycle": raw.get("tick", 0),
            "needs": raw.get("needs", {}),
            "affect": raw.get("affect", {}),
            "quantum_engine": "psi-daemon",
            "quantum_response": "",
            "quantum_latency_us": 0.0,
            "attention": "social",
            "emotion": str(raw.get("affect", {})),
            "self_presence": raw.get("affect", {}).get("dominance", 0.5),
            "energy": raw.get("endorphin", 0.5),
        }
        LATEST_FILE.write_text(json.dumps(mapped, ensure_ascii=False, indent=2))
    except Exception:
        pass
    time.sleep(0.5)