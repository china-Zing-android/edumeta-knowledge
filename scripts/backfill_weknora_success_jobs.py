from __future__ import annotations

import argparse
import hashlib
import json
from typing import Any


def recovered_job_id(university_id: str, version_id: str, source_id: str) -> str:
    digest = hashlib.sha256(f"{university_id}|{version_id}|{source_id}".encode("utf-8")).hexdigest()[:24]
    return f"wkj_recovered_{digest}"


def backfill_success_jobs(dsn: str, university_id: str) -> dict[str, Any]:
    try:
        import psycopg
        from psycopg.types.json import Jsonb
    except ImportError as exc:
        raise RuntimeError("psycopg is required for WeKnora job backfill") from exc

    with psycopg.connect(dsn) as connection, connection.transaction(), connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT sources.source_id, sources.version_id, sources.weknora_knowledge_base_id,
                   sources.weknora_knowledge_id, sources.weknora_document_id,
                   sources.weknora_chunk_ids, sources.weknora_tag_ids, sources.source_url,
                   (
                     SELECT runs.run_id
                       FROM ingestion_runs AS runs
                      WHERE runs.university_id=sources.university_id
                        AND runs.version_id=sources.version_id
                      ORDER BY runs.created_at DESC
                      LIMIT 1
                   ) AS run_id
              FROM source_registry AS sources
              JOIN school_versions AS versions USING (university_id, version_id)
             WHERE sources.university_id=%s
               AND versions.publication_state='current'
               AND sources.status='active'
               AND sources.weknora_import_status='success'
               AND sources.weknora_knowledge_base_id IS NOT NULL
               AND sources.weknora_knowledge_id IS NOT NULL
             ORDER BY sources.source_id
            """,
            (university_id,),
        )
        candidates = cursor.fetchall()
        inserted = 0
        updated = 0
        for (
            source_id,
            version_id,
            knowledge_base_id,
            knowledge_id,
            document_id,
            chunk_ids,
            tags,
            source_url,
            run_id,
        ) in candidates:
            job_id = recovered_job_id(university_id, version_id, source_id)
            cursor.execute(
                """
                UPDATE weknora_import_jobs
                   SET run_id=%s, knowledge_base_id=%s, knowledge_id=%s,
                       document_id=%s, chunk_ids=%s, tags=%s, source_url=%s,
                       status='success', retry_count=0,
                       started_at=COALESCE(started_at, now()),
                       finished_at=COALESCE(finished_at, now()), updated_at=now()
                 WHERE job_id=%s
                """,
                (
                    run_id,
                    knowledge_base_id,
                    knowledge_id,
                    document_id or knowledge_id,
                    Jsonb(chunk_ids or []),
                    Jsonb(tags or []),
                    source_url,
                    job_id,
                ),
            )
            if cursor.rowcount:
                updated += cursor.rowcount
                continue
            cursor.execute(
                """
                INSERT INTO weknora_import_jobs
                  (job_id, source_id, run_id, university_id, version_id,
                   knowledge_base_id, knowledge_id, document_id, chunk_ids, tags,
                   status, retry_count, started_at, finished_at, source_url)
                SELECT %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                       'success', 0, now(), now(), %s
                 WHERE NOT EXISTS (
                   SELECT 1
                     FROM weknora_import_jobs
                    WHERE university_id=%s
                      AND version_id=%s
                      AND source_id=%s
                      AND status IN ('queued', 'running', 'success')
                 )
                ON CONFLICT DO NOTHING
                """,
                (
                    job_id,
                    source_id,
                    run_id,
                    university_id,
                    version_id,
                    knowledge_base_id,
                    knowledge_id,
                    document_id or knowledge_id,
                    Jsonb(chunk_ids or []),
                    Jsonb(tags or []),
                    source_url,
                    university_id,
                    version_id,
                    source_id,
                ),
            )
            inserted += cursor.rowcount

        cursor.execute(
            """
            SELECT count(*)
              FROM weknora_import_jobs AS jobs
              JOIN school_versions AS versions USING (university_id, version_id)
             WHERE jobs.university_id=%s
               AND versions.publication_state='current'
               AND jobs.status='success'
            """,
            (university_id,),
        )
        current_success_jobs = cursor.fetchone()[0]

    return {
        "status": "ok",
        "university_id": university_id,
        "eligible_sources": len(candidates),
        "inserted_jobs": inserted,
        "updated_jobs": updated,
        "current_success_jobs": current_success_jobs,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Backfill successful WeKnora audit jobs from current source registry state.")
    parser.add_argument("--postgres-dsn", required=True)
    parser.add_argument("--university-id", required=True)
    args = parser.parse_args()
    print(json.dumps(backfill_success_jobs(args.postgres_dsn, args.university_id), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
