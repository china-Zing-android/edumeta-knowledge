from __future__ import annotations

import os
from typing import Any

import httpx


def _api_root(base_url: str) -> str:
    root = base_url.rstrip("/")
    return root if root.endswith("/api/v1") else f"{root}/api/v1"


class WeknoraSearchClient:
    def __init__(
        self,
        *,
        base_url: str,
        knowledge_base_id: str | None = None,
        api_key: str | None = None,
        api_key_header: str = "X-API-Key",
        search_path_template: str = "/knowledge-bases/{knowledge_base_id}/hybrid-search",
        timeout_seconds: float = 2.8,
        transport: Any | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.knowledge_base_id = knowledge_base_id
        self.api_key = api_key
        self.api_key_header = api_key_header
        self.search_path_template = search_path_template
        self.client = httpx.Client(timeout=timeout_seconds, transport=transport)

    @classmethod
    def from_env(cls) -> "WeknoraSearchClient | None":
        base_url = os.getenv("WEKNORA_BASE_URL", "").strip()
        kb_id = os.getenv("WEKNORA_KNOWLEDGE_BASE_ID", "").strip()
        if not base_url:
            return None
        return cls(
            base_url=base_url,
            knowledge_base_id=kb_id,
            api_key=os.getenv("WEKNORA_API_KEY"),
            api_key_header=os.getenv("WEKNORA_API_KEY_HEADER", "X-API-Key"),
            search_path_template=os.getenv("WEKNORA_SEARCH_PATH_TEMPLATE", "/knowledge-bases/{knowledge_base_id}/hybrid-search"),
            timeout_seconds=float(os.getenv("WEKNORA_SEARCH_TIMEOUT_SECONDS", "2.8")),
        )

    def close(self) -> None:
        self.client.close()

    def search(self, university_id: str, question: str, scopes: list[dict[str, Any]], top_k: int = 5) -> list[dict[str, Any]]:
        eligible = [
            scope for scope in scopes
            if scope.get("import_status") == "success"
            and scope.get("weknora_knowledge_id")
            and scope.get("dataset_version")
        ]
        if not eligible:
            return []
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers[self.api_key_header] = self.api_key
        scopes_by_kb: dict[str, list[dict[str, Any]]] = {}
        for scope in eligible:
            kb_id = scope.get("weknora_collection_id") or scope.get("weknora_knowledge_base_id") or self.knowledge_base_id
            if kb_id:
                scopes_by_kb.setdefault(str(kb_id), []).append(scope)
        evidence: list[dict[str, Any]] = []
        for kb_id, kb_scopes in scopes_by_kb.items():
            knowledge_ids = sorted({str(scope["weknora_knowledge_id"]) for scope in kb_scopes})
            payload: dict[str, Any] = {
                "query_text": question,
                "vector_threshold": 0,
                "keyword_threshold": 0,
                "match_count": top_k,
                "disable_keywords_match": False,
                "disable_vector_match": False,
                "knowledge_ids": knowledge_ids,
            }
            path = self.search_path_template.format(knowledge_base_id=kb_id)
            response = self.client.post(f"{_api_root(self.base_url)}{path}", headers=headers, json=payload)
            response.raise_for_status()
            evidence.extend(normalize_weknora_search_response(response.json(), university_id=university_id, scopes=kb_scopes))
        evidence.sort(key=lambda item: float(item.get("score") or 0), reverse=True)
        return evidence[:top_k]


def _items(payload: dict[str, Any]) -> list[dict[str, Any]]:
    data = payload.get("data")
    if isinstance(data, list):
        values = data
    elif isinstance(data, dict):
        values = data.get("results") or data.get("chunks") or data.get("items") or []
    else:
        values = payload.get("results") or []
    return [item for item in values if isinstance(item, dict)]


def _first(*values: Any) -> Any:
    return next((value for value in values if value not in (None, "")), None)


def normalize_weknora_search_response(payload: dict[str, Any], *, university_id: str, scopes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_knowledge: dict[str, dict[str, Any]] = {}
    for scope in scopes:
        for value in (scope.get("weknora_knowledge_id"), scope.get("weknora_document_id")):
            if value:
                by_knowledge[str(value)] = scope
    evidence: list[dict[str, Any]] = []
    for item in _items(payload):
        metadata = item.get("metadata") if isinstance(item.get("metadata"), dict) else {}
        knowledge_id = _first(item.get("knowledge_id"), item.get("document_id"), metadata.get("knowledge_id"), metadata.get("document_id"))
        scope = by_knowledge.get(str(knowledge_id)) if knowledge_id else None
        if not scope or scope.get("university_id") not in (None, university_id):
            continue
        chunk_text = str(_first(item.get("content"), item.get("chunk_text"), item.get("text"), item.get("snippet"), "")).strip()
        if not chunk_text:
            continue
        chunk_id = _first(item.get("chunk_id"), item.get("id"), metadata.get("chunk_id"), metadata.get("id"))
        evidence.append({
            "evidence_id": str(_first(item.get("evidence_id"), chunk_id, f"ev_{scope['source_id']}_{len(evidence)}")),
            "source_id": scope["source_id"],
            "source_url": scope["source_url"],
            "knowledge_id": str(scope.get("weknora_knowledge_id") or knowledge_id),
            "document_id": str(scope.get("weknora_document_id") or knowledge_id),
            "chunk_id": str(chunk_id) if chunk_id else None,
            "chunk_text": chunk_text,
            "score": item.get("score"),
            "capture_date": scope.get("capture_date"),
            "dataset_version": scope.get("dataset_version"),
        })
    return evidence
