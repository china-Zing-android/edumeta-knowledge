from __future__ import annotations

import json
import unittest

import httpx

from catalog_parser.weknora_importer import (
    RealWeknoraUrlImporter,
    WeknoraImportConfig,
    _normalize_import_status,
)


class WeknoraImporterTests(unittest.TestCase):
    def test_import_can_target_a_job_specific_knowledge_base(self) -> None:
        requests: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(201, json={"data": {"id": "knowledge_1", "parse_status": "processing"}})

        importer = RealWeknoraUrlImporter(
            WeknoraImportConfig(base_url="https://weknora.example/api/v1", knowledge_base_id="kb_default"),
            transport=httpx.MockTransport(handler),
        )
        importer.import_url(
            "harvard",
            {"source_id": "src_harvard", "canonical_url": "https://harvard.edu/programs"},
            knowledge_base_id="kb_harvard",
        )

        self.assertEqual(
            str(requests[0].url),
            "https://weknora.example/api/v1/knowledge-bases/kb_harvard/knowledge/url",
        )
    def test_finalizing_parse_status_remains_running(self) -> None:
        self.assertEqual(_normalize_import_status("finalizing"), "running")

    def test_real_importer_uses_url_import_contract_and_tag_scope(self) -> None:
        requests: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            self.assertEqual(
                json.loads(request.content.decode("utf-8")),
                {
                    "url": "https://example.edu/program",
                    "title": "Example program",
                    "channel": "api",
                    "tag_ids": ["tag_mit"],
                },
            )
            return httpx.Response(
                200,
                json={"data": {"id": "wk_kn_real", "parse_status": "processing", "file_hash": "real_hash"}},
            )

        importer = RealWeknoraUrlImporter(
            WeknoraImportConfig(
                base_url="https://weknora.example/api/v1",
                knowledge_base_id="kb_mit",
                api_key="secret",
            ),
            transport=httpx.MockTransport(handler),
        )
        try:
            result = importer.import_url(
                "mit",
                {
                    "source_id": "src_example",
                    "canonical_url": "https://example.edu/program",
                    "title": "Example program",
                    "tag_ids": ["tag_mit"],
                },
            )
        finally:
            importer.close()

        self.assertEqual(str(requests[0].url), "https://weknora.example/api/v1/knowledge-bases/kb_mit/knowledge/url")
        self.assertEqual(requests[0].headers["x-api-key"], "secret")
        self.assertEqual(result["weknora_knowledge_id"], "wk_kn_real")
        self.assertEqual(result["weknora_document_id"], "wk_kn_real")
        self.assertEqual(result["import_status"], "running")

    def test_real_importer_polls_knowledge_status(self) -> None:
        requests: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(
                200,
                json={"data": {"id": "wk_kn_real", "parse_status": "completed", "file_hash": "real_hash"}},
            )

        importer = RealWeknoraUrlImporter(
            WeknoraImportConfig(
                base_url="https://weknora.example/api/v1",
                knowledge_base_id="kb_mit",
                api_key="secret",
            ),
            transport=httpx.MockTransport(handler),
        )
        try:
            result = importer.get_import_status(
                "mit",
                {"source_id": "src_example", "canonical_url": "https://example.edu/program"},
                "wk_kn_real",
            )
        finally:
            importer.close()

        self.assertEqual(str(requests[0].url), "https://weknora.example/api/v1/knowledge/wk_kn_real")
        self.assertEqual(result["import_status"], "success")
        self.assertEqual(result["weknora_import_job_id"], "wk_kn_real")

    def test_duplicate_url_reuses_existing_knowledge(self) -> None:
        def handler(_: httpx.Request) -> httpx.Response:
            return httpx.Response(
                409,
                json={"data": {"id": "wk_kn_existing", "parse_status": "completed", "file_hash": "existing_hash"}},
            )

        importer = RealWeknoraUrlImporter(
            WeknoraImportConfig(base_url="https://weknora.example/api/v1", knowledge_base_id="kb_mit"),
            transport=httpx.MockTransport(handler),
        )
        try:
            result = importer.import_url(
                "mit",
                {"source_id": "src_example", "canonical_url": "https://example.edu/program"},
            )
        finally:
            importer.close()

        self.assertEqual(result["weknora_knowledge_id"], "wk_kn_existing")
        self.assertEqual(result["import_status"], "success")


if __name__ == "__main__":
    unittest.main()
