from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def trace_log_path() -> Path | None:
    configured = os.getenv("TRACE_LOG_PATH", "data/traces/retrieval.jsonl")
    if configured.lower() in {"", "off", "none", "false"}:
        return None
    return Path(configured)


def write_trace(event: dict[str, Any]) -> None:
    path = trace_log_path()
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            **event,
        }, ensure_ascii=False, sort_keys=True) + "\n")
