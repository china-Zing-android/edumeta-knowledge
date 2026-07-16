from __future__ import annotations

import hashlib
import json
import os
import threading
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any


PARSER_CONTRACT_VERSION = "5"


def merge_university_metadata(parsed: dict[str, Any], requested: dict[str, Any]) -> dict[str, Any]:
    merged = dict(parsed)
    for key in ("university_name", "country_code", "region"):
        if requested.get(key):
            merged[key] = requested[key]
    merged["aliases"] = sorted(set((parsed.get("aliases") or []) + (requested.get("aliases") or [])))
    return merged


def build_ingestion_input_hash(content: bytes, requested_metadata: dict[str, Any]) -> str:
    metadata_bytes = json.dumps(requested_metadata, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(PARSER_CONTRACT_VERSION.encode("ascii") + b"\0" + metadata_bytes + b"\0" + content).hexdigest()


def resolve_weknora_kb_request(
    existing_knowledge_base_id: str | None,
    requested_knowledge_base_id: str | None,
    create_new: bool,
) -> tuple[str, str | None]:
    requested = (requested_knowledge_base_id or "").strip() or None
    if requested and create_new:
        raise ValueError("weknora_knowledge_base_id and create_new_weknora_kb are mutually exclusive")
    if requested:
        return "explicit", requested
    if create_new or not existing_knowledge_base_id:
        return "create", None
    return "reuse", existing_knowledge_base_id


class IngestionService:
    def __init__(
        self,
        *,
        postgres_dsn: str,
        opensearch_url: str,
        raw_root: Path,
        workers: int = 2,
        on_published: Any | None = None,
    ) -> None:
        self.postgres_dsn = postgres_dsn
        self.opensearch_url = opensearch_url
        self.raw_root = raw_root
        self.executor = ThreadPoolExecutor(max_workers=workers, thread_name_prefix="ingestion")
        self.on_published = on_published
        self._futures: dict[str, Any] = {}
        self._lock = threading.Lock()

    @classmethod
    def from_env(cls) -> "IngestionService | None":
        dsn = os.getenv("POSTGRES_DSN", "").strip()
        opensearch_url = os.getenv("OPENSEARCH_URL", "").strip()
        if not dsn or not opensearch_url:
            return None
        return cls(
            postgres_dsn=dsn,
            opensearch_url=opensearch_url,
            raw_root=Path(os.getenv("INGESTION_DATA_ROOT", "data/ingestions")),
            workers=int(os.getenv("INGESTION_WORKERS", "2")),
        )

    def submit(
        self,
        *,
        university_id: str,
        school_tier: str,
        filename: str,
        content: bytes,
        university_name: str | None = None,
        country_code: str | None = None,
        region: str | None = None,
        aliases: list[str] | None = None,
        weknora_knowledge_base_id: str | None = None,
        create_new_weknora_kb: bool = False,
    ) -> dict[str, Any]:
        if school_tier not in {"core", "non_core"}:
            raise ValueError("school_tier must be core or non_core")
        if not filename.lower().endswith(".md"):
            raise ValueError("file must be Markdown (.md)")
        if not content.strip():
            raise ValueError("Markdown file is empty")
        university_id = university_id.strip().lower()
        if not university_id or not university_id.replace("_", "").replace("-", "").isalnum():
            raise ValueError("invalid university_id")

        run_id = f"ing_{uuid.uuid4().hex}"
        import psycopg
        from psycopg.types.json import Jsonb
        from catalog_parser.postgres_loader import upsert_university

        with psycopg.connect(self.postgres_dsn) as connection, connection.cursor() as cursor:
            cursor.execute(
                "SELECT weknora_knowledge_base_id FROM universities WHERE university_id=%s",
                (university_id,),
            )
            existing_row = cursor.fetchone()
        kb_operation, target_kb_id = resolve_weknora_kb_request(
            existing_row[0] if existing_row else None,
            weknora_knowledge_base_id,
            create_new_weknora_kb,
        )
        requested_metadata = {
            "university_name": university_name,
            "country_code": country_code.upper() if country_code else None,
            "region": region,
            "aliases": sorted(set(aliases or [])),
            "weknora_knowledge_base_id": target_kb_id or f"create:{run_id}",
        }
        input_hash = build_ingestion_input_hash(content, requested_metadata)
        version_id = f"ver_{university_id}_{input_hash[:16]}"
        run_dir = self.raw_root / university_id / run_id
        run_dir.mkdir(parents=True, exist_ok=False)
        raw_path = run_dir / "input.md"
        raw_path.write_bytes(content)

        with psycopg.connect(self.postgres_dsn) as connection:
            with connection.transaction():
                cursor = connection.cursor()
                operation = "update" if existing_row else "create"
                upsert_university(
                    cursor,
                    university_id=university_id,
                    university_name=university_name,
                    aliases=aliases,
                    country_code=requested_metadata["country_code"],
                    region=region,
                    school_tier=school_tier,
                    status="pending",
                )
                cursor.execute(
                    "SELECT version_id FROM school_versions WHERE university_id=%s AND publication_state='current' AND input_hash=%s",
                    (university_id, input_hash),
                )
                unchanged = cursor.fetchone()
                if unchanged:
                    operation = "unchanged"
                target_version = unchanged[0] if unchanged else version_id
                cursor.execute(
                    """
                    INSERT INTO school_versions
                      (version_id, university_id, dataset_version, publication_state, input_hash, record_counts)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (university_id, version_id) DO NOTHING
                    """,
                    (
                        target_version,
                        university_id,
                        target_version,
                        "current" if unchanged else "staging",
                        input_hash,
                        Jsonb({}),
                    ),
                )
                cursor.execute(
                    """
                    INSERT INTO ingestion_runs
                      (run_id, university_id, school_tier, operation, version_id, input_hash, status,
                       weknora_knowledge_base_id, weknora_kb_operation)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        run_id, university_id, school_tier, operation, target_version, input_hash,
                        "unchanged" if unchanged else "accepted", target_kb_id, kb_operation,
                    ),
                )
        if unchanged:
            return {"run_id": run_id, "university_id": university_id, "status": "unchanged", "operation": operation, "input_hash": input_hash}

        future = self.executor.submit(
            self._process,
            run_id,
            university_id,
            school_tier,
            version_id,
            input_hash,
            raw_path,
            run_dir,
            requested_metadata,
            kb_operation,
            target_kb_id,
        )
        with self._lock:
            self._futures[run_id] = future
        return {"run_id": run_id, "university_id": university_id, "status": "accepted", "operation": operation, "input_hash": input_hash}

    def _process(
        self,
        run_id: str,
        university_id: str,
        school_tier: str,
        version_id: str,
        input_hash: str,
        raw_path: Path,
        run_dir: Path,
        requested_metadata: dict[str, Any],
        kb_operation: str,
        target_kb_id: str | None,
    ) -> None:
        import psycopg
        from psycopg.types.json import Jsonb
        from catalog_parser.adapters import parse_school_markdown
        from catalog_parser.postgres_loader import load_dataset, publish_school_version, stage_school_records, activate_school_version, upsert_university
        from indexer.opensearch_publisher import publish_school

        normalized_dir = run_dir / "normalized"
        normalized_dir.mkdir(parents=True, exist_ok=True)
        try:
            result = parse_school_markdown(university_id, raw_path, fallback_adapter_name="auto")
            metadata = merge_university_metadata(result.summary, requested_metadata)
            resolved_kb_id, resolved_kb_name = self._resolve_weknora_knowledge_base(
                kb_operation,
                target_kb_id,
                university_id,
                str(metadata.get("university_name") or university_id),
            )
            for source in result.source_registry:
                source["weknora_knowledge_base_id"] = resolved_kb_id
                source["weknora_import_status"] = "pending"
                source["weknora_knowledge_id"] = None
                source["weknora_document_id"] = None
                source["weknora_chunk_ids"] = []
                source["weknora_tag_ids"] = []
                source["weknora_import_job_id"] = None
            for manifest in result.url_manifest:
                manifest["weknora_collection_id"] = resolved_kb_id
                manifest["import_status"] = "pending"
                manifest["weknora_knowledge_id"] = None
                manifest["weknora_document_id"] = None
                manifest["weknora_chunk_ids"] = []
                manifest["weknora_tag_ids"] = []
                manifest["weknora_import_job_id"] = None
            declared_version = next(
                (str(row.get("dataset_version")) for rows in (
                    result.source_registry, result.catalog_entries, result.url_manifest, result.quick_facts,
                    result.entity_contexts,
                ) for row in rows if row.get("dataset_version")),
                version_id,
            )
            effective_version = self._effective_dataset_version(
                university_id=university_id,
                version_id=version_id,
                declared_version=declared_version,
                input_hash=input_hash,
            )
            for rows in (
                result.source_registry, result.catalog_entries, result.url_manifest,
                result.quick_facts, result.entity_contexts,
            ):
                for row in rows:
                    row["dataset_version"] = effective_version
            result.write_jsonl(normalized_dir)
            dataset = load_dataset(normalized_dir, university_id)
            counts = {name: len(rows) for name, rows in dataset.items()}
            with psycopg.connect(self.postgres_dsn) as connection:
                with connection.transaction():
                    cursor = connection.cursor()
                    upsert_university(
                        cursor,
                        university_id=university_id,
                        university_name=metadata.get("university_name"),
                        aliases=metadata.get("aliases") or [],
                        country_code=metadata.get("country_code"),
                        region=metadata.get("region"),
                        school_tier=school_tier,
                        status="pending",
                    )
                    cursor.execute("UPDATE ingestion_runs SET status='validating', updated_at=now() WHERE run_id=%s", (run_id,))
                    cursor.execute(
                        "UPDATE ingestion_runs SET weknora_knowledge_base_id=%s WHERE run_id=%s",
                        (resolved_kb_id, run_id),
                    )
                    parsed_dataset_version = next(
                        (str(row.get("dataset_version")) for rows in dataset.values() for row in rows if row.get("dataset_version")),
                        version_id,
                    )
                    cursor.execute(
                        "UPDATE school_versions SET dataset_version=%s, record_counts=%s WHERE university_id=%s AND version_id=%s",
                        (parsed_dataset_version, Jsonb(counts), university_id, version_id),
                    )
                    stage_school_records(cursor, run_id=run_id, university_id=university_id, version_id=version_id, dataset=dataset)
                    publish_school_version(
                        connection,
                        run_id=run_id,
                        university_id=university_id,
                        version_id=version_id,
                        input_hash=input_hash,
                        activate=False,
                    )
                    self._carry_forward_weknora_state(cursor, university_id, version_id)
                    cursor.execute("UPDATE ingestion_runs SET status='publishing', updated_at=now() WHERE run_id=%s", (run_id,))

            self._enrich_normalized_sources(normalized_dir, university_id, version_id)
            publish_school(
                normalized_dir,
                university_id,
                self.opensearch_url,
                university_metadata={
                    "university_name": metadata.get("university_name"),
                    "aliases": metadata.get("aliases") or [],
                    "country_code": metadata.get("country_code"),
                    "region": metadata.get("region"),
                    "school_tier": school_tier,
                },
            )

            with psycopg.connect(self.postgres_dsn) as connection:
                with connection.transaction():
                    cursor = connection.cursor()
                    activate_school_version(cursor, university_id=university_id, version_id=version_id, run_id=run_id)
                    self._enqueue_weknora_jobs(cursor, run_id, university_id, version_id)
                    cursor.execute(
                        """
                        UPDATE universities
                           SET weknora_knowledge_base_id=%s, weknora_knowledge_base_name=%s, updated_at=now()
                         WHERE university_id=%s
                        """,
                        (resolved_kb_id, resolved_kb_name, university_id),
                    )
            if self.on_published:
                self.on_published()
        except Exception as exc:  # noqa: BLE001 - failure is persisted for status polling.
            with psycopg.connect(self.postgres_dsn) as connection:
                with connection.transaction():
                    cursor = connection.cursor()
                    cursor.execute(
                        "UPDATE ingestion_runs SET status='failed', error_message=%s, stage_failures=%s, updated_at=now() WHERE run_id=%s",
                        (str(exc), Jsonb([{"stage": "pipeline", "reason": str(exc)}]), run_id),
                    )
                    cursor.execute(
                        "UPDATE school_versions SET publication_state='failed' WHERE university_id=%s AND version_id=%s AND publication_state='staging'",
                        (university_id, version_id),
                    )
                    cursor.execute(
                        """
                        UPDATE universities SET status=CASE
                          WHEN EXISTS (SELECT 1 FROM school_versions WHERE university_id=%s AND publication_state='current')
                          THEN 'active' ELSE 'failed' END,
                          updated_at=now()
                        WHERE university_id=%s
                        """,
                        (university_id, university_id),
                    )

    def _resolve_weknora_knowledge_base(
        self,
        operation: str,
        target_kb_id: str | None,
        university_id: str,
        university_name: str,
    ) -> tuple[str, str]:
        from .weknora_kb import WeknoraKnowledgeBaseClient

        client = WeknoraKnowledgeBaseClient.from_env()
        if client is None:
            raise RuntimeError("WEKNORA_BASE_URL is required for ingestion")
        try:
            if operation == "create":
                kb = client.create_for_university(university_id, university_name)
            else:
                if not target_kb_id:
                    raise ValueError(f"{operation} requires a WeKnora knowledge base id")
                kb = client.validate_existing(target_kb_id)
            return str(kb["id"]), str(kb.get("name") or f"edumeta-{university_id}")
        finally:
            client.close()

    @staticmethod
    def _enqueue_weknora_jobs(cursor: Any, run_id: str, university_id: str, version_id: str) -> None:
        cursor.execute(
            """
            INSERT INTO weknora_import_jobs
              (job_id, source_id, run_id, university_id, version_id, knowledge_base_id,
               knowledge_id, document_id, chunk_ids, status, source_url, tags)
            SELECT 'wkj_' || md5(%s || ':' || source_id), source_id, %s, university_id, version_id,
                   weknora_knowledge_base_id, weknora_knowledge_id, weknora_document_id,
                   COALESCE(weknora_chunk_ids, '[]'::jsonb), 'queued', canonical_url,
                   jsonb_build_array('university:' || university_id)
             FROM source_registry
             WHERE university_id=%s AND version_id=%s AND status='active'
               AND COALESCE(weknora_import_status, 'pending')<>'success'
               AND NOT EXISTS (
                 SELECT 1 FROM weknora_import_jobs AS existing_job
                  WHERE existing_job.university_id=source_registry.university_id
                    AND existing_job.version_id=source_registry.version_id
                    AND existing_job.source_id=source_registry.source_id
                    AND existing_job.status IN ('queued', 'running', 'success')
               )
            ON CONFLICT (job_id) DO NOTHING
            """,
            (run_id, run_id, university_id, version_id),
        )

    def _effective_dataset_version(
        self,
        *,
        university_id: str,
        version_id: str,
        declared_version: str,
        input_hash: str,
    ) -> str:
        import psycopg

        with psycopg.connect(self.postgres_dsn) as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT 1 FROM school_versions
                 WHERE university_id=%s AND version_id<>%s
                   AND dataset_version=%s AND input_hash<>%s
                 LIMIT 1
                """,
                (university_id, version_id, declared_version, input_hash),
            )
            collision = cursor.fetchone() is not None
        return f"{declared_version}__{input_hash[:8]}" if collision else declared_version

    @staticmethod
    def _carry_forward_weknora_state(cursor: Any, university_id: str, version_id: str) -> None:
        cursor.execute(
            """
            SELECT current.source_id, previous.weknora_import_status,
                   previous.weknora_knowledge_base_id, previous.weknora_knowledge_id,
                   previous.weknora_document_id, previous.weknora_chunk_ids,
                   previous.weknora_tag_ids, previous.weknora_import_job_id,
                   previous.weknora_content_hash
              FROM source_registry AS current
              JOIN LATERAL (
                SELECT old.* FROM source_registry AS old
                 WHERE old.university_id=current.university_id
                   AND old.version_id<>current.version_id
                   AND old.canonical_url=current.canonical_url
                   AND old.weknora_knowledge_base_id=current.weknora_knowledge_base_id
                   AND old.weknora_import_status IN ('success', 'running', 'pending')
                 ORDER BY old.updated_at DESC LIMIT 1
              ) AS previous ON true
             WHERE current.university_id=%s AND current.version_id=%s
            """,
            (university_id, version_id),
        )
        for row in cursor.fetchall():
            from psycopg.types.json import Jsonb

            values = list(row[1:])
            values[4] = Jsonb(values[4] or [])
            values[5] = Jsonb(values[5] or [])
            cursor.execute(
                """
                UPDATE source_registry SET
                  weknora_import_status=%s, weknora_knowledge_base_id=%s,
                  weknora_knowledge_id=%s, weknora_document_id=%s,
                  weknora_chunk_ids=%s, weknora_tag_ids=%s,
                  weknora_import_job_id=%s, weknora_content_hash=%s, updated_at=now()
                 WHERE university_id=%s AND version_id=%s AND source_id=%s
                """,
                (*values, university_id, version_id, row[0]),
            )

    def _enrich_normalized_sources(self, normalized_dir: Path, university_id: str, version_id: str) -> None:
        import psycopg

        with psycopg.connect(self.postgres_dsn) as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT source_id, weknora_import_status, weknora_knowledge_base_id,
                       weknora_knowledge_id, weknora_document_id, weknora_chunk_ids,
                       weknora_tag_ids, weknora_import_job_id
                  FROM source_registry WHERE university_id=%s AND version_id=%s
                """,
                (university_id, version_id),
            )
            state = {row[0]: row[1:] for row in cursor.fetchall()}
        for filename in ("source_registry.jsonl", "url_manifest.jsonl"):
            path = normalized_dir / filename
            records = [json.loads(line) for line in path.read_text("utf-8").splitlines() if line]
            for record in records:
                values = state.get(record["source_id"])
                if not values:
                    continue
                status, kb_id, knowledge_id, document_id, chunk_ids, tag_ids, job_id = values
                if filename == "source_registry.jsonl":
                    record.update({
                        "weknora_import_status": status,
                        "weknora_knowledge_base_id": kb_id,
                        "weknora_knowledge_id": knowledge_id,
                        "weknora_document_id": document_id,
                        "weknora_chunk_ids": chunk_ids,
                        "weknora_tag_ids": tag_ids,
                        "weknora_import_job_id": job_id,
                    })
                else:
                    record.update({
                        "import_status": status,
                        "weknora_collection_id": kb_id,
                        "weknora_knowledge_id": knowledge_id,
                        "weknora_document_id": document_id,
                        "weknora_chunk_ids": chunk_ids,
                        "weknora_tag_ids": tag_ids,
                        "weknora_import_job_id": job_id,
                    })
            path.write_text("".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records), "utf-8")

    def status(self, run_id: str) -> dict[str, Any] | None:
        import psycopg

        with psycopg.connect(self.postgres_dsn) as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT run_id, university_id, school_tier, operation, version_id, input_hash, status,
                       stage_failures, error_message, created_at, updated_at,
                       weknora_knowledge_base_id, weknora_kb_operation
                  FROM ingestion_runs WHERE run_id=%s
                """,
                (run_id,),
            )
            row = cursor.fetchone()
            if not row:
                return None
            cursor.execute(
                "SELECT entity_name, count(*) FROM ingestion_records WHERE run_id=%s GROUP BY entity_name",
                (run_id,),
            )
            counts = dict(cursor.fetchall())
            cursor.execute(
                "SELECT status, count(*) FROM weknora_import_jobs WHERE run_id=%s GROUP BY status",
                (run_id,),
            )
            jobs = dict(cursor.fetchall())
        return {
            "run_id": row[0], "university_id": row[1], "school_tier": row[2], "operation": row[3], "version_id": row[4],
            "input_hash": row[5], "status": row[6], "counts": counts,
            "stage_failures": row[7], "error_message": row[8],
            "opensearch_published": row[6] == "published", "weknora_jobs": jobs,
            "created_at": row[9].isoformat(), "updated_at": row[10].isoformat(),
            "weknora_knowledge_base_id": row[11], "weknora_kb_operation": row[12],
        }
