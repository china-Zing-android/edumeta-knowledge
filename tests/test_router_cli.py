from __future__ import annotations

import json
import subprocess
import sys
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_args):
        return

    def do_POST(self):  # noqa: N802
        length = int(self.headers.get("content-length", "0"))
        body = self.rfile.read(length)
        if self.path == "/v1/retrieve":
            request = json.loads(body)
            response = {
                "trace_id": "tr_cli", "mode": "l1",
                "scope": {"university_id": request.get("university_id") or "mit", "dataset_version": "mit_v1"},
                "matches": [{"fact_type": "english_requirement", "raw_value": "TOEFL 100"}],
                "evidence": [], "missing_slots": [], "warnings": [],
                "timings": {"total_ms": 1, "l1_ms": 1, "weknora_ms": 0},
            }
            payload = json.dumps(response).encode()
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        self.send_response(404)
        self.end_headers()


class RouterCliTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_address[1]}"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()

    def test_retrieve_cli_calls_http_contract(self) -> None:
        completed = subprocess.run(
            [
                sys.executable, str(ROOT / "scripts/router_cli.py"), "--base-url", self.base_url,
                "retrieve", "--query", "MIT EECS PhD TOEFL", "--university-id", "mit",
            ],
            check=True, capture_output=True, text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["mode"], "l1")
        self.assertEqual(payload["matches"][0]["raw_value"], "TOEFL 100")


if __name__ == "__main__":
    unittest.main()
