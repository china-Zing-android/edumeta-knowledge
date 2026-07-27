from __future__ import annotations

import os
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from fast_router.ingestion import IngestionService, resolve_weknora_kb_request
from fast_router.weknora_worker import WeknoraJobWorker


class WeknoraKBRoutingTests(unittest.TestCase):
    def test_disabled_import_skips_synchronous_kb_control_plane_call(self) -> None:
        service = object.__new__(IngestionService)
        service._resolve_weknora_knowledge_base = Mock(return_value=("unexpected", "unexpected"))
        service._set_run_status = Mock()

        with patch.dict(os.environ, {"WEKNORA_IMPORT_ENABLED": "false"}):
            resolved = service._prepare_weknora_knowledge_base(
                "run_1",
                "reuse",
                "kb_existing",
                "mit",
                "MIT",
            )

        self.assertEqual(resolved, ("kb_existing", None))
        service._resolve_weknora_knowledge_base.assert_not_called()
        service._set_run_status.assert_not_called()

    def test_enabled_import_reports_preparation_and_calls_kb_control_plane(self) -> None:
        service = object.__new__(IngestionService)
        service._resolve_weknora_knowledge_base = Mock(return_value=("kb_existing", "MIT KB"))
        service._set_run_status = Mock()

        with patch.dict(os.environ, {"WEKNORA_IMPORT_ENABLED": "true"}):
            resolved = service._prepare_weknora_knowledge_base(
                "run_1",
                "reuse",
                "kb_existing",
                "mit",
                "MIT",
            )

        self.assertEqual(resolved, ("kb_existing", "MIT KB"))
        service._set_run_status.assert_called_once_with("run_1", "weknora_preparing")
        service._resolve_weknora_knowledge_base.assert_called_once_with(
            "reuse",
            "kb_existing",
            "mit",
            "MIT",
        )

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
        self.assertIn("jobs.knowledge_base_id IS NOT NULL", source)

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
