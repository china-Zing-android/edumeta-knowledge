from __future__ import annotations

import json
import unittest

import httpx

from fast_router.weknora_client import WeknoraSearchClient, normalize_weknora_search_response


class WeknoraSearchClientTests(unittest.TestCase):
    def test_search_groups_scopes_by_knowledge_base(self) -> None:
        requests: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            body = json.loads(request.content)
            knowledge_id = body["knowledge_ids"][0]
            return httpx.Response(200, json={"data": [{"id": f"chunk_{knowledge_id}", "knowledge_id": knowledge_id, "content": knowledge_id}]})

        client = WeknoraSearchClient(
            base_url="https://weknora.example/api/v1",
            knowledge_base_id="kb_fallback",
            transport=httpx.MockTransport(handler),
        )
        evidence = client.search("mit", "question", [
            {
                "university_id": "mit", "source_id": "src_1", "source_url": "https://mit.edu/1",
                "capture_date": "2026-07-04", "dataset_version": "mit_v1", "import_status": "success",
                "weknora_collection_id": "kb_mit_1", "weknora_knowledge_id": "knowledge_1",
            },
            {
                "university_id": "mit", "source_id": "src_2", "source_url": "https://mit.edu/2",
                "capture_date": "2026-07-04", "dataset_version": "mit_v1", "import_status": "success",
                "weknora_collection_id": "kb_mit_2", "weknora_knowledge_id": "knowledge_2",
            },
        ], top_k=5)

        self.assertEqual(
            {request.url.path for request in requests},
            {
                "/api/v1/knowledge-bases/kb_mit_1/hybrid-search",
                "/api/v1/knowledge-bases/kb_mit_2/hybrid-search",
            },
        )
        self.assertEqual({item["source_id"] for item in evidence}, {"src_1", "src_2"})
    def test_normalize_search_response_maps_knowledge_id_to_local_scope(self) -> None:
        scopes = [
            {
                "source_id": "src_mit_eecs",
                "source_url": "https://mit.edu/eecs",
                "capture_date": "2026-07-04",
                "import_status": "success",
                "weknora_document_id": "doc_eecs",
                "weknora_knowledge_id": "doc_eecs",
                "dataset_version": "mit_v1",
                "topics": ["admission_requirements"],
            }
        ]
        payload = {
            "data": {
                "results": [
                    {
                        "id": "chk_1",
                        "content": "TOEFL 100",
                        "knowledge_id": "doc_eecs",
                    },
                    {
                        "id": "chk_2",
                        "content": "Wrong document",
                        "knowledge_id": "doc_stanford",
                    },
                    {
                        "id": "chk_3",
                        "content": "Missing document identity",
                    },
                ]
            }
        }

        evidence = normalize_weknora_search_response(payload, university_id="mit", scopes=scopes)

        self.assertEqual(len(evidence), 1)
        self.assertEqual(evidence[0]["source_id"], "src_mit_eecs")
        self.assertEqual(evidence[0]["chunk_id"], "chk_1")
        self.assertEqual(evidence[0]["chunk_text"], "TOEFL 100")

    def test_search_prefers_exact_knowledge_ids_over_broad_tag_filter(self) -> None:
        requests: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, json={"data": []})

        client = WeknoraSearchClient(
            base_url="https://weknora.example/api/v1",
            knowledge_base_id="kb_mit",
            transport=httpx.MockTransport(handler),
        )
        client.search("mit", "question", [{
            "source_id": "src", "source_url": "https://mit.edu/x", "capture_date": "2026-07-04",
            "dataset_version": "mit_v1", "import_status": "success",
            "weknora_knowledge_id": "doc_1", "weknora_tag_ids": ["tag_mit"],
        }])

        body = json.loads(requests[0].content)
        self.assertEqual(body["knowledge_ids"], ["doc_1"])
        self.assertNotIn("tag_ids", body)

    def test_search_posts_hybrid_contract_and_filters_response_client_side(self) -> None:
        requests: list[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            body = json.loads(request.content.decode("utf-8"))
            self.assertEqual(
                body,
                {
                    "query_text": "MIT EECS TOEFL",
                    "vector_threshold": 0,
                    "keyword_threshold": 0,
                    "match_count": 5,
                    "disable_keywords_match": False,
                    "disable_vector_match": False,
                    "knowledge_ids": ["doc_eecs"],
                },
            )
            return httpx.Response(
                200,
                json={
                    "data": [
                        {
                            "id": "chk_1",
                            "content": "TOEFL 100",
                            "knowledge_id": "doc_eecs",
                        }
                    ]
                },
            )

        client = WeknoraSearchClient(
            base_url="https://weknora.example/api/v1",
            knowledge_base_id="kb_mit",
            api_key="secret",
            transport=httpx.MockTransport(handler),
        )

        evidence = client.search(
            "mit",
            "MIT EECS TOEFL",
            [
                {
                    "source_id": "src_mit_eecs",
                    "source_url": "https://mit.edu/eecs",
                    "capture_date": "2026-07-04",
                    "import_status": "success",
                    "weknora_document_id": "doc_eecs",
                    "weknora_knowledge_id": "doc_eecs",
                    "dataset_version": "mit_v1",
                    "topics": ["admission_requirements"],
                }
            ],
        )

        self.assertEqual(str(requests[0].url), "https://weknora.example/api/v1/knowledge-bases/kb_mit/hybrid-search")
        self.assertEqual(requests[0].headers["x-api-key"], "secret")
        self.assertEqual(evidence[0]["chunk_text"], "TOEFL 100")


if __name__ == "__main__":
    unittest.main()
