from __future__ import annotations

import json
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from typing import Any

import httpx

from catalog_parser.weknora_importer import RealWeknoraUrlImporter, WeknoraImportConfig


def weknora_import_enabled() -> bool:
    return os.getenv("WEKNORA_IMPORT_ENABLED", "true").strip().lower() not in {"0", "false", "no", "off"}


class WeknoraJobWorker:
    def __init__(
        self,
        *,
        postgres_dsn: str,
        opensearch_url: str,
        config: WeknoraImportConfig,
        concurrency: int = 2,
        batch_size: int = 4,
    ) -> None:
        self.postgres_dsn = postgres_dsn
        self.config = config
        self.concurrency = concurrency
        self.batch_size = batch_size
        self.importer = RealWeknoraUrlImporter(config)
        self.api_client = httpx.Client(timeout=config.timeout_seconds)
        from opensearchpy import OpenSearch

        self.opensearch = OpenSearch(opensearch_url, timeout=2, max_retries=0)
        self._tag_cache: dict[tuple[str, str], str] = {}
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self.iterations = 0
        self.last_run_count = 0
        self.last_error: str | None = None

    @classmethod
    def from_env(cls) -> "WeknoraJobWorker | None":
        if not weknora_import_enabled():
            return None
        required = [os.getenv("POSTGRES_DSN"), os.getenv("OPENSEARCH_URL"), os.getenv("WEKNORA_BASE_URL")]
        if not all(required):
            return None
        fallback_kb_id = os.getenv("WEKNORA_KB_TEMPLATE_ID") or os.getenv("WEKNORA_KNOWLEDGE_BASE_ID") or "job-specific"
        return cls(
            postgres_dsn=str(required[0]),
            opensearch_url=str(required[1]),
            config=WeknoraImportConfig.from_env(knowledge_base_id=fallback_kb_id),
            concurrency=int(os.getenv("WEKNORA_WORKER_CONCURRENCY", "2")),
            batch_size=int(os.getenv("WEKNORA_WORKER_BATCH_SIZE", "4")),
        )

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._thread = threading.Thread(target=self.run_forever, name="weknora-worker", daemon=True)
        self._thread.start()

    def close(self) -> None:
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=5)
        self.importer.close()
        self.api_client.close()

    def run_forever(self) -> None:
        while not self._stop.is_set():
            try:
                count = self.run_once()
                self.last_error = None
            except Exception as exc:  # startup races or transient DB errors must not kill the worker thread.
                count = 0
                self.last_error = str(exc)
            self.iterations += 1
            self.last_run_count = count
            self._stop.wait(1 if count else 3)

    @property
    def alive(self) -> bool:
        return bool(self._thread and self._thread.is_alive())

    def run_once(self) -> int:
        jobs = self._claim_jobs()
        if not jobs:
            return 0
        with ThreadPoolExecutor(max_workers=self.concurrency, thread_name_prefix="weknora-import") as executor:
            list(executor.map(self._process_job, jobs))
        return len(jobs)

    def _headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.config.api_key:
            headers[self.config.api_key_header] = self.config.api_key
        return headers

    def _claim_jobs(self) -> list[dict[str, Any]]:
        import psycopg

        with psycopg.connect(self.postgres_dsn) as connection, connection.transaction(), connection.cursor() as cursor:
            cursor.execute(
                """
                WITH claimed AS (
                  SELECT jobs.job_id
                    FROM weknora_import_jobs AS jobs
                    JOIN school_versions AS versions
                      ON versions.university_id=jobs.university_id
                     AND versions.version_id=jobs.version_id
                     AND versions.publication_state='current'
                   WHERE jobs.status='queued'
                     AND (jobs.next_attempt_at IS NULL OR jobs.next_attempt_at<=now())
                   ORDER BY jobs.updated_at, jobs.created_at
                   FOR UPDATE OF jobs SKIP LOCKED
                   LIMIT %s
                )
                UPDATE weknora_import_jobs AS jobs
                   SET status='running', started_at=COALESCE(started_at, now()), updated_at=now()
                  FROM claimed WHERE jobs.job_id=claimed.job_id
                RETURNING jobs.job_id, jobs.source_id, jobs.university_id, jobs.version_id,
                          jobs.source_url, jobs.knowledge_base_id, jobs.knowledge_id, jobs.retry_count
                """,
                (self.batch_size,),
            )
            rows = cursor.fetchall()
        return [
            {"job_id": row[0], "source_id": row[1], "university_id": row[2], "version_id": row[3],
             "source_url": row[4], "knowledge_base_id": row[5], "knowledge_id": row[6], "retry_count": row[7]}
            for row in rows
        ]

    def _ensure_university_tag(self, university_id: str, knowledge_base_id: str) -> str:
        cache_key = (knowledge_base_id, university_id)
        if cache_key in self._tag_cache:
            return self._tag_cache[cache_key]
        name = f"university:{university_id}"
        root = self.config.base_url.rstrip("/")
        if not root.endswith("/api/v1"):
            root += "/api/v1"
        endpoint = f"{root}/knowledge-bases/{knowledge_base_id}/tags"
        response = self.api_client.get(endpoint, headers=self._headers(), params={"page": 1, "page_size": 100, "keyword": name})
        response.raise_for_status()
        data = response.json().get("data")
        items = data if isinstance(data, list) else (
            (data or {}).get("items") or (data or {}).get("list") or (data or {}).get("data") or []
        )
        for item in items:
            if item.get("name") == name:
                self._tag_cache[cache_key] = str(item["id"])
                return str(item["id"])
        response = self.api_client.post(endpoint, headers=self._headers(), json={"name": name, "color": "#3B82F6", "sort_order": 0})
        if response.status_code == 409:
            self._tag_cache.pop(cache_key, None)
            retry = self.api_client.get(endpoint, headers=self._headers(), params={"page": 1, "page_size": 100, "keyword": name})
            retry.raise_for_status()
            retry_data = retry.json().get("data") or {}
            retry_items = retry_data if isinstance(retry_data, list) else (retry_data.get("data") or retry_data.get("items") or [])
            tag_id = next(str(item["id"]) for item in retry_items if item.get("name") == name)
        else:
            response.raise_for_status()
            tag_id = str(response.json()["data"]["id"])
        self._tag_cache[cache_key] = tag_id
        return tag_id

    def _fetch_job_result(self, job: dict[str, Any], tag_id: str) -> dict[str, Any]:
        source = {
            "source_id": job["source_id"],
            "canonical_url": job["source_url"],
            "tag_ids": [tag_id],
        }
        if job.get("knowledge_id"):
            return self.importer.get_import_status(
                job["university_id"], source, job["knowledge_id"],
                knowledge_base_id=job["knowledge_base_id"],
            )
        return self.importer.import_url(
            job["university_id"], source,
            knowledge_base_id=job["knowledge_base_id"],
        )

    def _process_job(self, job: dict[str, Any]) -> None:
        try:
            tag_id = self._ensure_university_tag(job["university_id"], job["knowledge_base_id"])
            result = self._fetch_job_result(job, tag_id)
            self._persist_result(job, result, tag_id)
        except Exception as exc:  # noqa: BLE001 - queue state must capture remote failures.
            self._persist_failure(job, str(exc))

    def _persist_result(self, job: dict[str, Any], result: dict[str, Any], tag_id: str) -> None:
        import psycopg
        from psycopg.types.json import Jsonb

        remote_status = result.get("import_status", "running")
        terminal = remote_status == "success"
        queue_status = "success" if terminal else "queued"
        next_attempt = None if terminal else datetime.now(timezone.utc) + timedelta(seconds=5)
        knowledge_id = result.get("weknora_knowledge_id") or job.get("knowledge_id")
        document_id = result.get("weknora_document_id") or knowledge_id
        chunk_ids = result.get("weknora_chunk_ids") or []
        with psycopg.connect(self.postgres_dsn) as connection, connection.transaction(), connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE weknora_import_jobs
                   SET status=%s, knowledge_base_id=%s, knowledge_id=%s, document_id=%s,
                       chunk_ids=%s, tags=%s, next_attempt_at=%s,
                       finished_at=CASE WHEN %s THEN now() ELSE NULL END,
                       failure_reason=NULL, updated_at=now()
                 WHERE job_id=%s
                """,
                (queue_status, job["knowledge_base_id"], knowledge_id, document_id, Jsonb(chunk_ids), Jsonb([tag_id]), next_attempt, terminal, job["job_id"]),
            )
            cursor.execute(
                """
                UPDATE source_registry
                   SET weknora_import_status=%s, weknora_knowledge_base_id=%s,
                       weknora_knowledge_id=%s, weknora_document_id=%s,
                       weknora_chunk_ids=%s, weknora_tag_ids=%s,
                       weknora_import_job_id=%s, error_message=NULL, updated_at=now()
                 WHERE university_id=%s AND version_id=%s AND source_id=%s
                """,
                (remote_status, job["knowledge_base_id"], knowledge_id, document_id, Jsonb(chunk_ids), Jsonb([tag_id]), job["job_id"], job["university_id"], job["version_id"], job["source_id"]),
            )
            cursor.execute(
                """
                UPDATE source_registry SET
                  weknora_import_status=%s, weknora_knowledge_base_id=%s,
                  weknora_knowledge_id=%s, weknora_document_id=%s,
                  weknora_chunk_ids=%s, weknora_tag_ids=%s,
                  weknora_import_job_id=%s, error_message=NULL, updated_at=now()
                 WHERE university_id=%s AND source_id=%s AND version_id<>%s
                   AND weknora_knowledge_base_id=%s
                """,
                (remote_status, job["knowledge_base_id"], knowledge_id, document_id, Jsonb(chunk_ids), Jsonb([tag_id]), job["job_id"], job["university_id"], job["source_id"], job["version_id"], job["knowledge_base_id"]),
            )
            cursor.execute(
                "SELECT dataset_version FROM source_registry WHERE university_id=%s AND source_id=%s AND weknora_knowledge_base_id=%s",
                (job["university_id"], job["source_id"], job["knowledge_base_id"]),
            )
            dataset_versions = [row[0] for row in cursor.fetchall()]
        for dataset_version in dataset_versions:
            try:
                self.opensearch.update(
                    index="l1_sources_current",
                    id=f"{job['university_id']}:{dataset_version}:{job['source_id']}",
                    body={"doc": {
                        "import_status": remote_status,
                        "weknora_collection_id": job["knowledge_base_id"],
                        "weknora_knowledge_id": knowledge_id,
                        "weknora_document_id": document_id,
                        "weknora_chunk_ids": chunk_ids,
                        "weknora_tag_ids": [tag_id],
                    }},
                    refresh=True,
                )
            except Exception as exc:
                if getattr(exc, "status_code", None) != 404:
                    raise

    def _persist_failure(self, job: dict[str, Any], reason: str) -> None:
        import psycopg

        retry_count = int(job.get("retry_count") or 0) + 1
        retryable = retry_count < 3
        next_attempt = datetime.now(timezone.utc) + timedelta(seconds=2**retry_count) if retryable else None
        with psycopg.connect(self.postgres_dsn) as connection, connection.transaction(), connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE weknora_import_jobs
                   SET status=%s, retry_count=%s, next_attempt_at=%s, failure_reason=%s,
                       finished_at=CASE WHEN %s THEN NULL ELSE now() END, updated_at=now()
                 WHERE job_id=%s
                """,
                ("queued" if retryable else "failed", retry_count, next_attempt, reason[:2000], retryable, job["job_id"]),
            )
