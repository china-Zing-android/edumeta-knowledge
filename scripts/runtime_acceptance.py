from __future__ import annotations

import argparse
import json
from pathlib import Path

import httpx
import psycopg
from opensearchpy import OpenSearch


REQUIRED_ALIASES = {
    "l1_universities_current",
    "l1_catalog_entries_current",
    "l1_quick_facts_current",
    "l1_sources_current",
    "l1_entity_contexts_current",
}


def current_source_import_failures(source_counts: dict[str, int]) -> list[str]:
    return [
        f"current_sources_{status}={count}"
        for status in ("pending", "running", "failed")
        if (count := source_counts.get(status, 0))
    ]


def current_source_job_failures(missing_count: int) -> list[str]:
    return [f"current_success_sources_without_success_job={missing_count}"] if missing_count else []


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--postgres-dsn", default="postgresql://edumeta:edumeta@127.0.0.1:5432/edumeta")
    parser.add_argument("--opensearch-url", default="http://127.0.0.1:9200")
    parser.add_argument("--output-path", type=Path, required=True)
    args = parser.parse_args()
    failures: list[str] = []
    with httpx.Client(timeout=3) as client:
        router = client.get("http://127.0.0.1:8000/health").json()
        gateway = client.get("http://127.0.0.1:8765/health").json()
    if router.get("status") != "ok":
        failures.append("fast-router unhealthy")
    if gateway.get("status") != "ok":
        failures.append("tool-gateway unhealthy")
    aliases = REQUIRED_ALIASES
    client = OpenSearch(args.opensearch_url)
    missing_aliases = sorted(alias for alias in aliases if not client.indices.exists_alias(name=alias))
    if missing_aliases:
        failures.append(f"missing aliases: {missing_aliases}")
    with psycopg.connect(args.postgres_dsn) as connection, connection.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM school_versions WHERE publication_state='current'")
        current_versions = cursor.fetchone()[0]
        cursor.execute("SELECT status, count(*) FROM weknora_import_jobs GROUP BY status")
        job_counts = dict(cursor.fetchall())
        cursor.execute(
            """
            SELECT sources.weknora_import_status, count(*)
              FROM source_registry AS sources
              JOIN school_versions AS versions USING (university_id, version_id)
             WHERE versions.publication_state='current' AND sources.status='active'
             GROUP BY sources.weknora_import_status
            """
        )
        current_source_counts = dict(cursor.fetchall())
        cursor.execute("SELECT count(*) FROM source_registry s JOIN school_versions v USING (university_id, version_id) WHERE v.publication_state='current'")
        current_sources = cursor.fetchone()[0]
        cursor.execute(
            """
            SELECT count(*)
              FROM source_registry AS sources
              JOIN school_versions AS versions USING (university_id, version_id)
             WHERE versions.publication_state='current'
               AND sources.status='active'
               AND sources.weknora_import_status='success'
               AND NOT EXISTS (
                 SELECT 1
                   FROM weknora_import_jobs AS jobs
                  WHERE jobs.university_id=sources.university_id
                    AND jobs.version_id=sources.version_id
                    AND jobs.source_id=sources.source_id
                    AND jobs.status='success'
               )
            """
        )
        current_sources_without_success_job = cursor.fetchone()[0]
    if current_versions < 1:
        failures.append(f"current_versions={current_versions}")
    failures.extend(current_source_import_failures(current_source_counts))
    failures.extend(current_source_job_failures(current_sources_without_success_job))
    report = {
        "status": "passed" if not failures else "failed",
        "failures": failures,
        "router": router,
        "gateway": gateway,
        "aliases": sorted(aliases),
        "current_versions": current_versions,
        "current_sources": current_sources,
        "weknora_jobs": job_counts,
        "current_source_imports": current_source_counts,
        "current_success_sources_without_success_job": current_sources_without_success_job,
    }
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    args.output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["status"] == "passed" else 1)


if __name__ == "__main__":
    main()
