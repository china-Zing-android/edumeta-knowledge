from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from fast_router.tracing import write_trace


class TracingTests(unittest.TestCase):
    def test_trace_writes_structured_jsonl(self) -> None:
        previous = os.environ.get("TRACE_LOG_PATH")
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "trace.jsonl"
            os.environ["TRACE_LOG_PATH"] = str(path)
            try:
                write_trace({"trace_id": "tr_1", "mode": "l1"})
            finally:
                if previous is None:
                    os.environ.pop("TRACE_LOG_PATH", None)
                else:
                    os.environ["TRACE_LOG_PATH"] = previous
            payload = json.loads(path.read_text("utf-8"))
        self.assertEqual(payload["trace_id"], "tr_1")
        self.assertEqual(payload["mode"], "l1")

    def test_trace_can_be_disabled(self) -> None:
        previous = os.environ.get("TRACE_LOG_PATH")
        os.environ["TRACE_LOG_PATH"] = "off"
        try:
            write_trace({"trace_id": "tr_disabled"})
        finally:
            if previous is None:
                os.environ.pop("TRACE_LOG_PATH", None)
            else:
                os.environ["TRACE_LOG_PATH"] = previous
