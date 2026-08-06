from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

os.environ["TRACE_LOG_PATH"] = "off"

import fast_router.main as main  # noqa: E402


class FakeRetrievalEngine:
    weknora = None

    def retrieve(self, **kwargs):
        query = kwargs["query"]
        mode = "clarification" if "unknown" in query else "l1"
        return {
            "trace_id": "tr_test",
            "mode": mode,
            "scope": {"university_id": kwargs.get("university_id") or "mit", "dataset_version": "mit_v1"},
            "matches": [] if mode == "clarification" else [{"entry_id": "ent_1", "program_name": "Economics"}],
            "context": {
                "primary_entities": [{"entity_type": "program", "entity_id": "ent_1", "display_label": "14-1 Economics"}],
                "highlights": [],
                "sample_children": [],
                "related_entities": [],
                "available_topics": [],
                "presentation_hints": {},
                "provenance": {"origin": "md_projection", "dataset_version": "mit_v1"},
            },
            "evidence": [],
            "missing_slots": ["university_id"] if mode == "clarification" else [],
            "warnings": [],
            "timings": {"total_ms": 1.0, "l1_ms": 0.8, "weknora_ms": 0.0},
        }


class FakeIngestionService:
    last_submit = None

    def submit(self, **kwargs):
        self.last_submit = kwargs
        if not kwargs["content"].strip():
            raise ValueError("Markdown file is empty")
        return {
            "run_id": "ing_test",
            "university_id": kwargs["university_id"],
            "status": "accepted",
            "operation": "create",
            "input_hash": "abc",
        }

    def status(self, run_id):
        return None if run_id == "missing" else {"run_id": run_id, "status": "published", "counts": {"catalog_entries": 157}}


class FakeAdminControl:
    def source_files(self, **kwargs):
        return {
            "items": [{"relative_path": "us/mit.md", "source_status": "not_submitted"}],
            "total_count": 1,
            "limit": kwargs["limit"],
            "offset": kwargs["offset"],
        }

    def list_versions(self, **kwargs):
        return {
            "items": [{
                "university_id": "mit",
                "version_id": "ver_mit_1",
                "publication_state": "current",
            }],
            "total_count": 1,
            "limit": kwargs["limit"],
            "offset": kwargs["offset"],
        }

    def provenance(self, run_id, entity, record_id):
        return {
            "mapping": {
                "mapping_id": "prov_1",
                "jsonl": {"entity": entity, "record_id": record_id},
                "verification": {"status": "verified"},
            },
            "jsonl": {"artifact": entity, "line": 1, "record": {"entry_id": record_id}},
            "markdown": {
                "highlighted_range": {"line_start": 7, "line_end": 7},
                "items": [{"line": 7, "text": "| Computer Science |", "highlighted": True}],
            },
        }


class FastRouterApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.previous_engine = main.retrieval_engine
        self.previous_ingestion = main.ingestion_service
        self.previous_admin = main.admin_control
        main.retrieval_engine = FakeRetrievalEngine()
        main.ingestion_service = FakeIngestionService()
        main.admin_control = FakeAdminControl()
        self.client = TestClient(main.app)

    def tearDown(self) -> None:
        self.client.close()
        main.retrieval_engine = self.previous_engine
        main.ingestion_service = self.previous_ingestion
        main.admin_control = self.previous_admin

    def test_retrieve_contract(self) -> None:
        response = self.client.post("/v1/retrieve", json={"query": "MIT Economics", "university_id": "mit"})
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["mode"], "l1")
        self.assertEqual(payload["matches"][0]["program_name"], "Economics")
        self.assertEqual(payload["context"]["primary_entities"][0]["display_label"], "14-1 Economics")
        self.assertEqual(set(payload["timings"]), {"total_ms", "l1_ms", "weknora_ms"})

    def test_health_reports_multi_kb_weknora_without_legacy_default(self) -> None:
        with patch.dict(
            os.environ,
            {
                "WEKNORA_BASE_URL": "https://weknora.example/api/v1",
                "WEKNORA_API_KEY": "secret",
                "WEKNORA_KB_TEMPLATE_ID": "kb_template",
            },
            clear=False,
        ):
            os.environ.pop("WEKNORA_KNOWLEDGE_BASE_ID", None)
            payload = self.client.get("/health").json()["weknora"]

        self.assertTrue(payload["configured"])
        self.assertEqual(payload["routing_mode"], "per_source_knowledge_base")
        self.assertTrue(payload["template_knowledge_base_configured"])
        self.assertFalse(payload["legacy_fallback_knowledge_base_configured"])

    def test_health_reports_paused_weknora_import_gate(self) -> None:
        with patch.dict(
            os.environ,
            {
                "WEKNORA_BASE_URL": "https://weknora.example/api/v1",
                "WEKNORA_IMPORT_ENABLED": "false",
            },
            clear=False,
        ):
            payload = self.client.get("/health").json()["weknora"]

        self.assertFalse(payload["import_enabled"])
        self.assertFalse(payload["worker_alive"])

    def test_ingestion_upload_returns_202(self) -> None:
        response = self.client.post(
            "/v1/ingestions",
            data={"university_id": "mit", "school_tier": "core"},
            files={"file": ("mit.md", b"# MIT\n", "text/markdown")},
        )
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.json()["status"], "accepted")

    def test_preferred_university_ingestion_api_accepts_range_metadata(self) -> None:
        response = self.client.post(
            "/v1/university-ingestions",
            data={
                "university_id": "stanford",
                "school_tier": "core",
                "university_name": "Stanford University",
                "country_code": "US",
                "region": "California",
                "aliases": "Stanford,SU",
                "weknora_knowledge_base_id": "kb_stanford",
                "create_new_weknora_kb": "false",
            },
            files={"file": ("stanford.md", b"# Stanford\n", "text/markdown")},
        )

        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.json()["operation"], "create")
        self.assertEqual(main.ingestion_service.last_submit["country_code"], "US")
        self.assertEqual(main.ingestion_service.last_submit["aliases"], ["Stanford", "SU"])
        self.assertEqual(main.ingestion_service.last_submit["weknora_knowledge_base_id"], "kb_stanford")
        self.assertFalse(main.ingestion_service.last_submit["create_new_weknora_kb"])

    def test_ingestion_rejects_empty_markdown(self) -> None:
        response = self.client.post(
            "/v1/ingestions",
            data={"university_id": "mit", "school_tier": "core"},
            files={"file": ("mit.md", b"", "text/markdown")},
        )
        self.assertEqual(response.status_code, 422)

    def test_ingestion_status_and_not_found(self) -> None:
        self.assertEqual(self.client.get("/v1/ingestions/ing_test").status_code, 200)
        self.assertEqual(self.client.get("/v1/ingestions/missing").status_code, 404)

    def test_admin_source_files_exposes_unsubmitted_server_markdown(self) -> None:
        response = self.client.get("/v1/admin/source-files?source_root_id=universities&limit=20")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["items"][0]["source_status"], "not_submitted")

    def test_admin_versions_exposes_postgres_version_catalog(self) -> None:
        response = self.client.get("/v1/admin/versions?limit=20")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["items"][0]["version_id"], "ver_mit_1")

    def test_admin_provenance_exposes_jsonl_and_markdown_mapping(self) -> None:
        response = self.client.get("/v1/admin/ingestion-runs/ing_test/provenance/catalog_entries/ent_1")

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["mapping"]["verification"]["status"], "verified")
        self.assertEqual(payload["jsonl"]["line"], 1)
        self.assertTrue(payload["markdown"]["items"][0]["highlighted"])


if __name__ == "__main__":
    unittest.main()
