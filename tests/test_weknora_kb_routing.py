from __future__ import annotations

import os
import unittest
from pathlib import Path
from unittest.mock import patch

from fast_router.ingestion import resolve_weknora_kb_request
from fast_router.weknora_worker import WeknoraJobWorker


class WeknoraKBRoutingTests(unittest.TestCase):
    def test_worker_is_disabled_by_import_gate_without_disabling_search_configuration(self) -> None:
        with patch.dict(
            os.environ,
            {
                "POSTGRES_DSN": "postgresql://example",
                "OPENSEARCH_URL": "http://opensearch:9200",
                "WEKNORA_BASE_URL": "https://weknora.example/api/v1",
                "WEKNORA_IMPORT_ENABLED": "false",
            },
            clear=False,
        ):
            self.assertIsNone(WeknoraJobWorker.from_env())

    def test_worker_claim_order_is_fair_between_new_imports_and_polls(self) -> None:
        source = Path("apps/fast-router/src/fast_router/weknora_worker.py").read_text("utf-8")

        self.assertIn("ORDER BY jobs.updated_at, jobs.created_at", source)

    def test_resolve_request_prefers_explicit_then_existing_then_create(self) -> None:
        self.assertEqual(resolve_weknora_kb_request("kb_old", "kb_new", False), ("explicit", "kb_new"))
        self.assertEqual(resolve_weknora_kb_request("kb_old", None, False), ("reuse", "kb_old"))
        self.assertEqual(resolve_weknora_kb_request(None, None, False), ("create", None))
        self.assertEqual(resolve_weknora_kb_request("kb_old", None, True), ("create", None))

    def test_explicit_and_force_new_are_mutually_exclusive(self) -> None:
        with self.assertRaisesRegex(ValueError, "mutually exclusive"):
            resolve_weknora_kb_request("kb_old", "kb_new", True)

    def test_worker_routes_import_and_poll_to_job_knowledge_base(self) -> None:
        calls: list[tuple[str, str]] = []

        class FakeImporter:
            def import_url(self, university_id, source, *, knowledge_base_id=None):
                calls.append(("import", knowledge_base_id))
                return {"import_status": "running"}

            def get_import_status(self, university_id, source, knowledge_id, *, knowledge_base_id=None):
                calls.append(("poll", knowledge_base_id))
                return {"import_status": "success"}

        worker = object.__new__(WeknoraJobWorker)
        worker.importer = FakeImporter()

        worker._fetch_job_result({
            "university_id": "mit", "source_id": "src_1", "source_url": "https://mit.edu/1",
            "knowledge_base_id": "kb_mit", "knowledge_id": None,
        }, "tag_1")
        worker._fetch_job_result({
            "university_id": "mit", "source_id": "src_2", "source_url": "https://mit.edu/2",
            "knowledge_base_id": "kb_mit", "knowledge_id": "knowledge_2",
        }, "tag_1")

        self.assertEqual(calls, [("import", "kb_mit"), ("poll", "kb_mit")])
