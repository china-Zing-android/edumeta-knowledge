from __future__ import annotations

import json
import unittest

import httpx

from fast_router.weknora_kb import WeknoraKnowledgeBaseClient


class WeknoraKnowledgeBaseClientTests(unittest.TestCase):
    def test_validate_existing_returns_requested_kb(self) -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            self.assertEqual(request.url.path, "/api/v1/knowledge-bases/kb_existing")
            return httpx.Response(200, json={"success": True, "data": {"id": "kb_existing", "name": "mit"}})

        client = WeknoraKnowledgeBaseClient(
            base_url="https://weknora.example/api/v1",
            api_key="secret",
            transport=httpx.MockTransport(handler),
        )

        self.assertEqual(client.validate_existing("kb_existing")["id"], "kb_existing")

    def test_create_clones_template_configuration_with_new_identity(self) -> None:
        requests: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            if request.method == "GET":
                return httpx.Response(200, json={"success": True, "data": {
                    "id": "kb_template",
                    "name": "template",
                    "type": "document",
                    "embedding_model_id": "embed_1",
                    "summary_model_id": "summary_1",
                    "chunking_config": {"chunk_size": 512, "chunk_overlap": 80, "separators": ["\n\n"]},
                    "indexing_strategy": {"vector_enabled": True, "keyword_enabled": True},
                    "storage_provider_config": {"provider": "minio"},
                }})
            body = json.loads(request.content)
            self.assertEqual(body["name"], "edumeta-harvard")
            self.assertEqual(body["description"], "Edumeta university knowledge: Harvard University")
            self.assertEqual(body["embedding_model_id"], "embed_1")
            self.assertNotIn("id", body)
            return httpx.Response(201, json={"success": True, "data": {"id": "kb_harvard", "name": body["name"]}})

        client = WeknoraKnowledgeBaseClient(
            base_url="https://weknora.example/api/v1",
            api_key="secret",
            template_knowledge_base_id="kb_template",
            transport=httpx.MockTransport(handler),
        )

        created = client.create_for_university("harvard", "Harvard University")

        self.assertEqual(created["id"], "kb_harvard")
        self.assertEqual([request.method for request in requests], ["GET", "POST"])


if __name__ == "__main__":
    unittest.main()
