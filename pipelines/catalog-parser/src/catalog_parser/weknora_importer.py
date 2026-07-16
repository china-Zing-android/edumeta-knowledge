from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from typing import Any


def _digest(value: str, length: int = 16) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:length]


def _first_present(payload: dict[str, Any], keys: list[str]) -> Any:
    for key in keys:
        if key in payload and payload[key] not in (None, ""):
            return payload[key]
    return None


def _extract_chunk_ids(data: dict[str, Any]) -> list[str]:
    chunk_ids = _first_present(data, ["weknora_chunk_ids", "chunk_ids", "chunks_ids"])
    if isinstance(chunk_ids, list):
        return [str(item) for item in chunk_ids if item]
    chunks = data.get("chunks")
    if isinstance(chunks, list):
        result: list[str] = []
        for chunk in chunks:
            if isinstance(chunk, dict):
                chunk_id = _first_present(chunk, ["id", "chunk_id", "weknora_chunk_id"])
                if chunk_id:
                    result.append(str(chunk_id))
            elif chunk:
                result.append(str(chunk))
        return result
    return []


def _weknora_api_root(base_url: str) -> str:
    root = base_url.rstrip("/")
    return root if root.endswith("/api/v1") else f"{root}/api/v1"


def _normalize_weknora_response(
    *,
    university_id: str,
    source: dict[str, Any],
    knowledge_base_id: str,
    payload: dict[str, Any],
) -> dict[str, Any]:
    data = payload.get("data") if isinstance(payload.get("data"), dict) else payload
    document = data.get("document") if isinstance(data.get("document"), dict) else {}
    knowledge = data.get("knowledge") if isinstance(data.get("knowledge"), dict) else {}
    source_id = source["source_id"]
    url = source["canonical_url"]
    content_hash = _first_present(data, ["content_hash", "weknora_content_hash", "file_hash"]) or source.get("content_hash") or _digest(f"{source_id}:{url}", 32)
    job_id = _first_present(data, ["weknora_import_job_id", "import_job_id", "job_id", "task_id"])
    knowledge_id = _first_present(data, ["weknora_knowledge_id", "knowledge_id", "id"]) or _first_present(knowledge, ["id", "knowledge_id"])
    document_id = _first_present(data, ["weknora_document_id", "document_id", "doc_id"]) or _first_present(document, ["id", "document_id", "doc_id"]) or knowledge_id
    remote_status = _first_present(data, ["parse_status", "import_status", "status"]) or "success"
    return {
        "content_hash": str(content_hash),
        "weknora_content_hash": str(_first_present(data, ["weknora_content_hash", "content_hash"]) or content_hash),
        "weknora_collection_id": str(_first_present(data, ["weknora_collection_id", "collection_id", "knowledge_base_id"]) or knowledge_base_id),
        "weknora_knowledge_id": str(knowledge_id or f"wk_kn_{university_id}_{_digest(source_id, 12)}"),
        "weknora_document_id": str(document_id or ""),
        "weknora_chunk_ids": _extract_chunk_ids(data),
        # WeKnora exposes parsing state by knowledge ID rather than a separate import-job resource.
        "weknora_import_job_id": str(job_id or knowledge_id) if (job_id or knowledge_id) else None,
        "import_status": _normalize_import_status(remote_status),
    }


@dataclass(frozen=True)
class WeknoraImportConfig:
    base_url: str
    knowledge_base_id: str
    api_key: str | None = None
    api_key_header: str = "X-API-Key"
    import_channel: str = "api"
    process_config: dict[str, Any] | None = None
    timeout_seconds: float = 60
    import_status_path_template: str = "/knowledge/{knowledge_id}"

    @classmethod
    def from_env(
        cls,
        *,
        base_url: str | None = None,
        api_key: str | None = None,
        knowledge_base_id: str | None = None,
        import_status_path_template: str | None = None,
    ) -> "WeknoraImportConfig":
        resolved_base_url = base_url or os.getenv("WEKNORA_BASE_URL")
        resolved_knowledge_base_id = knowledge_base_id or os.getenv("WEKNORA_KNOWLEDGE_BASE_ID")
        if not resolved_base_url:
            raise ValueError("WEKNORA_BASE_URL is required for real WeKnora import mode.")
        if not resolved_knowledge_base_id:
            raise ValueError("WEKNORA_KNOWLEDGE_BASE_ID is required for real WeKnora import mode.")
        raw_process_config = os.getenv("WEKNORA_PROCESS_CONFIG_JSON", "").strip()
        process_config = None
        if raw_process_config:
            decoded = json.loads(raw_process_config)
            if not isinstance(decoded, dict):
                raise ValueError("WEKNORA_PROCESS_CONFIG_JSON must be a JSON object.")
            process_config = decoded
        return cls(
            base_url=resolved_base_url.rstrip("/"),
            knowledge_base_id=resolved_knowledge_base_id,
            api_key=api_key or os.getenv("WEKNORA_API_KEY"),
            api_key_header=os.getenv("WEKNORA_API_KEY_HEADER", "X-API-Key"),
            import_channel=os.getenv("WEKNORA_IMPORT_CHANNEL", "api"),
            process_config=process_config,
            import_status_path_template=import_status_path_template
            or os.getenv("WEKNORA_IMPORT_STATUS_PATH_TEMPLATE", "/knowledge/{knowledge_id}"),
        )


class RealWeknoraUrlImporter:
    def __init__(self, config: WeknoraImportConfig, *, transport: Any | None = None):
        self.config = config
        self.transport = transport
        try:
            import httpx
        except ImportError as exc:
            raise RuntimeError("httpx is required for real WeKnora import mode.") from exc
        self.client = httpx.Client(timeout=self.config.timeout_seconds, transport=self.transport)

    def close(self) -> None:
        self.client.close()

    def _headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.config.api_key:
            headers[self.config.api_key_header] = self.config.api_key
        return headers

    def import_url(
        self,
        university_id: str,
        source: dict[str, Any],
        *,
        knowledge_base_id: str | None = None,
    ) -> dict[str, Any]:
        target_kb_id = knowledge_base_id or self.config.knowledge_base_id
        url = f"{_weknora_api_root(self.config.base_url)}/knowledge-bases/{target_kb_id}/knowledge/url"
        request_payload: dict[str, Any] = {"url": source["canonical_url"]}
        title = source.get("title") or source.get("source_title")
        if title:
            request_payload["title"] = str(title)
        if self.config.import_channel:
            request_payload["channel"] = self.config.import_channel
        if self.config.process_config:
            request_payload["process_config"] = self.config.process_config
        tag_ids = source.get("tag_ids") or source.get("weknora_tag_ids")
        if tag_ids:
            request_payload["tag_ids"] = [str(value) for value in tag_ids]
        response = self.client.post(url, headers=self._headers(), json=request_payload)
        if response.status_code != 409:
            response.raise_for_status()
        payload = response.json()
        return _normalize_weknora_response(
            university_id=university_id,
            source=source,
            knowledge_base_id=target_kb_id,
            payload=payload,
        )

    def get_import_status(
        self,
        university_id: str,
        source: dict[str, Any],
        job_id: str,
        *,
        knowledge_base_id: str | None = None,
    ) -> dict[str, Any]:
        target_kb_id = knowledge_base_id or self.config.knowledge_base_id
        path = self.config.import_status_path_template.format(
            knowledge_base_id=target_kb_id,
            knowledge_id=job_id,
            job_id=job_id,
        )
        response = self.client.get(f"{_weknora_api_root(self.config.base_url)}{path}", headers=self._headers())
        response.raise_for_status()
        payload = response.json()
        result = _normalize_weknora_response(
            university_id=university_id,
            source=source,
            knowledge_base_id=target_kb_id,
            payload=payload,
        )
        result["weknora_import_job_id"] = job_id
        return result


def _normalize_import_status(status: Any) -> str:
    value = str(status or "success").lower()
    aliases = {
        "completed": "success",
        "complete": "success",
        "done": "success",
        "succeeded": "success",
        "queued": "pending",
        "created": "pending",
        "processing": "running",
        "in_progress": "running",
        "parsing": "running",
        "finalizing": "running",
        "parsed": "success",
        "error": "failed",
        "failure": "failed",
    }
    return aliases.get(value, value)
