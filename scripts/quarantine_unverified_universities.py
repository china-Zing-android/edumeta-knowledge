from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any


CURRENT_ALIASES = (
    "l1_universities_current",
    "l1_catalog_entries_current",
    "l1_entity_contexts_current",
)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text("utf-8").splitlines() if line.strip()]


def unverified_ids(rows: list[dict[str, Any]]) -> list[str]:
    return sorted(
        str(row["university_id"])
        for row in rows
        if row.get("status") in {"needs_review", "failed"}
    )


def chunks(values: list[str], size: int = 500) -> list[list[str]]:
    return [values[index:index + size] for index in range(0, len(values), size)]


def apply_quarantine(ids: list[str], postgres_dsn: str, opensearch_url: str) -> dict[str, Any]:
    import psycopg
    from opensearchpy import OpenSearch

    if not ids:
        return {"postgres_updates": 0, "opensearch_updates": {alias: 0 for alias in CURRENT_ALIASES}}

    client = OpenSearch(opensearch_url)
    opensearch_updates: dict[str, int] = {}
    for alias in CURRENT_ALIASES:
        updated = 0
        for batch in chunks(ids):
            response = client.update_by_query(
                index=alias,
                body={
                    "script": {"source": "ctx._source.is_current = false", "lang": "painless"},
                    "query": {"terms": {"university_id": batch}},
                },
                conflicts="proceed",
                refresh=True,
            )
            updated += int(response.get("updated") or 0)
        opensearch_updates[alias] = updated

    with psycopg.connect(postgres_dsn) as connection, connection.transaction(), connection.cursor() as cursor:
        cursor.execute(
            "UPDATE universities SET status='failed', updated_at=now() WHERE university_id = ANY(%s) AND status<>'failed'",
            (ids,),
        )
        postgres_updates = cursor.rowcount
    return {"postgres_updates": postgres_updates, "opensearch_updates": opensearch_updates}


def main() -> None:
    parser = argparse.ArgumentParser(description="Quarantine current universities that no longer pass the committed quality gate.")
    parser.add_argument("--preflight", type=Path, default=Path("data/raw-md/universities/preflight-results.jsonl"))
    parser.add_argument("--postgres-dsn", default=os.getenv("POSTGRES_DSN", ""))
    parser.add_argument("--opensearch-url", default=os.getenv("OPENSEARCH_URL", ""))
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    ids = unverified_ids(read_jsonl(args.preflight))
    report: dict[str, Any] = {"status": "dry_run", "count": len(ids), "university_ids": ids}
    if args.apply:
        if not args.postgres_dsn or not args.opensearch_url:
            raise SystemExit("POSTGRES_DSN and OPENSEARCH_URL are required with --apply")
        report.update(apply_quarantine(ids, args.postgres_dsn, args.opensearch_url))
        report["status"] = "applied"
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
