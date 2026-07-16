from __future__ import annotations

import os
from typing import Any

import httpx


def _api_root(base_url: str) -> str:
    root = base_url.rstrip("/")
    return root if root.endswith("/api/v1") else f"{root}/api/v1"


class WeknoraKnowledgeBaseClient:
    TEMPLATE_FIELDS = (
        "type",
        "chunking_config",
        "image_processing_config",
        "embedding_model_id",
        "summary_model_id",
        "vlm_config",
        "asr_config",
        "storage_provider_config",
        "extract_config",
        "question_generation_config",
        "wiki_config",
        "indexing_strategy",
    )

    def __init__(
        self,
        *,
        base_url: str,
        api_key: str | None = None,
        api_key_header: str = "X-API-Key",
        template_knowledge_base_id: str | None = None,
        timeout_seconds: float = 30,
        transport: Any | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.api_key_header = api_key_header
        self.template_knowledge_base_id = template_knowledge_base_id
        self.client = httpx.Client(timeout=timeout_seconds, transport=transport)

    @classmethod
    def from_env(cls) -> "WeknoraKnowledgeBaseClient | None":
        base_url = os.getenv("WEKNORA_BASE_URL", "").strip()
        if not base_url:
            return None
        return cls(
            base_url=base_url,
            api_key=os.getenv("WEKNORA_API_KEY"),
            api_key_header=os.getenv("WEKNORA_API_KEY_HEADER", "X-API-Key"),
            template_knowledge_base_id=(
                os.getenv("WEKNORA_KB_TEMPLATE_ID", "").strip()
                or os.getenv("WEKNORA_KNOWLEDGE_BASE_ID", "").strip()
                or None
            ),
        )

    def close(self) -> None:
        self.client.close()

    def _headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers[self.api_key_header] = self.api_key
        return headers

    def validate_existing(self, knowledge_base_id: str) -> dict[str, Any]:
        response = self.client.get(
            f"{_api_root(self.base_url)}/knowledge-bases/{knowledge_base_id}",
            headers=self._headers(),
        )
        response.raise_for_status()
        data = response.json().get("data") or {}
        if str(data.get("id") or "") != knowledge_base_id:
            raise ValueError(f"WeKnora knowledge base {knowledge_base_id!r} was not returned by the service")
        return data

    def create_for_university(self, university_id: str, university_name: str) -> dict[str, Any]:
        template: dict[str, Any] = {}
        if self.template_knowledge_base_id:
            template = self.validate_existing(self.template_knowledge_base_id)
        payload = {
            key: template[key]
            for key in self.TEMPLATE_FIELDS
            if key in template and template[key] is not None
        }
        payload.update({
            "name": f"edumeta-{university_id}",
            "description": f"Edumeta university knowledge: {university_name}",
            "type": payload.get("type") or "document",
        })
        response = self.client.post(
            f"{_api_root(self.base_url)}/knowledge-bases",
            headers=self._headers(),
            json=payload,
        )
        response.raise_for_status()
        data = response.json().get("data") or {}
        if not data.get("id"):
            raise ValueError("WeKnora create knowledge base response did not include an id")
        return data
