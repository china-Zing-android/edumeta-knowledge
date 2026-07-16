from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import urlopen

from apply_postgres_migrations import apply_migrations

REQUIRED_FILES = ("source_registry.jsonl", "catalog_entries.jsonl", "url_manifest.jsonl", "quick_facts.jsonl")
POSTGRES_TABLES = {
    "source_registry": "source_registry",
    "catalog_entries": "catalog_entries",
    "url_manifest": "source_registry",
    "quick_facts": "fact_store",
}


def wait_for_postgres(dsn: str, timeout_seconds: int) -> None:
    try:
        import psycopg
    except ImportError as exc:
        raise RuntimeError("psycopg is required for live Postgres gate.") from exc

    deadline = time.time() + timeout_seconds
    last_error: Exception | None = None
    while time.time() < deadline:
        try:
            with psycopg.connect(dsn, connect_timeout=3) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    cursor.fetchone()
                    return
        except Exception as exc:  # noqa: BLE001 - preserve last readiness error.
            last_error = exc
            time.sleep(2)
    raise RuntimeError(f"Postgres did not become ready within {timeout_seconds}s: {last_error}")


def wait_for_http(url: str, timeout_seconds: int) -> None:
    deadline = time.time() + timeout_seconds
    last_error: Exception | None = None
    while time.time() < deadline:
        try:
            with urlopen(url, timeout=3) as response:
                if 200 <= response.status < 500:
                    return
        except Exception as exc:  # noqa: BLE001 - preserve last readiness error.
            last_error = exc
            time.sleep(2)
    raise RuntimeError(f"HTTP endpoint did not become ready within {timeout_seconds}s: {url}: {last_error}")


def load_jsonl_count(path: Path) -> int:
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())


def expected_counts(data_dir: Path) -> dict[str, int]:
    return {
        file_name.removesuffix(".jsonl"): load_jsonl_count(data_dir / file_name)
        for file_name in REQUIRED_FILES
    }


def discover_data_dirs(data_root: Path) -> dict[str, Path]:
    if not data_root.exists():
        return {}
    return {
        path.name: path
        for path in sorted(data_root.iterdir())
        if path.is_dir() and all((path / file_name).exists() for file_name in REQUIRED_FILES)
    }


def postgres_counts(dsn: str, university_id: str) -> dict[str, int]:
    import psycopg

    counts: dict[str, int] = {}
    with psycopg.connect(dsn) as connection:
        with connection.cursor() as cursor:
            for key, table in POSTGRES_TABLES.items():
                cursor.execute(postgres_count_sql(table), (university_id, university_id))
                counts[key] = cursor.fetchone()[0]
    return counts


def postgres_count_sql(table: str) -> str:
    if table not in set(POSTGRES_TABLES.values()):
        raise ValueError(f"unsupported bootstrap table: {table}")
    return (
        f"SELECT count(*) FROM {table} WHERE university_id = %s AND version_id = ("
        "SELECT version_id FROM school_versions "
        "WHERE university_id = %s AND publication_state='current'"
        ")"
    )


def opensearch_count_query(university_id: str, dataset_version: str) -> dict[str, Any]:
    return {"query": {"bool": {"filter": [
        {"term": {"university_id": university_id}},
        {"term": {"dataset_version": dataset_version}},
    ]}}}


def opensearch_alias_counts(
    opensearch_url: str,
    aliases: list[str],
    *,
    university_id: str | None = None,
    dataset_version: str | None = None,
) -> dict[str, int]:
    try:
        from opensearchpy import OpenSearch
    except ImportError as exc:
        raise RuntimeError("opensearch-py is required for live OpenSearch gate.") from exc

    client = OpenSearch(opensearch_url)
    counts: dict[str, int] = {}
    body = (
        opensearch_count_query(university_id, dataset_version)
        if university_id and dataset_version
        else None
    )
    for alias in aliases:
        result = client.count(index=alias, body=body) if body else client.count(index=alias)
        counts[alias] = int(result["count"])
    return counts


def default_report_path() -> Path:
    today = datetime.now(timezone.utc).date().isoformat()
    return Path("qa/reports") / f"live-data-gate-{today}.json"


def write_gate_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        **report,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_live_data_gate(
    *,
    postgres_dsn: str,
    opensearch_url: str,
    data_dirs: dict[str, Path],
    migrations_dir: Path,
    timeout_seconds: int,
) -> dict[str, Any]:
    from catalog_parser.postgres_loader import load_school_to_postgres
    from indexer.opensearch_publisher import publish_school

    wait_for_postgres(postgres_dsn, timeout_seconds)
    wait_for_http(opensearch_url, timeout_seconds)
    migration_report = apply_migrations(postgres_dsn, migrations_dir)
    if not data_dirs:
        return {
            "status": "failed",
            "failures": ["no data dirs discovered"],
            "migration": migration_report,
            "schools": {},
        }

    failures: list[str] = []
    schools: dict[str, Any] = {}
    for university_id, data_dir in sorted(data_dirs.items()):
        load_report = load_school_to_postgres(data_dir, university_id, postgres_dsn, run_id=f"live_gate_{university_id}")
        publish_report = publish_school(data_dir, university_id, opensearch_url)
        expected = expected_counts(data_dir)
        pg_counts = postgres_counts(postgres_dsn, university_id)
        published_indexes = publish_report["indexes"]
        aliases = [item["alias"] for item in published_indexes.values()]
        dataset_version = published_indexes["catalog_entries"]["dataset_version"]
        os_counts = opensearch_alias_counts(
            opensearch_url,
            aliases,
            university_id=university_id,
            dataset_version=dataset_version,
        )
        alias_expectations = {
            item["alias"]: item["count"]
            for item in published_indexes.values()
        }
        for key, expected_count in expected.items():
            if pg_counts.get(key) != expected_count:
                failures.append(f"{university_id} postgres {key}: expected {expected_count}, got {pg_counts.get(key)}")
        for alias, expected_count in alias_expectations.items():
            if os_counts.get(alias) != expected_count:
                failures.append(f"{university_id} opensearch {alias}: expected {expected_count}, got {os_counts.get(alias)}")
        schools[university_id] = {
            "data_dir": str(data_dir),
            "expected_counts": expected,
            "postgres_load": load_report,
            "opensearch_publish": publish_report,
            "postgres_counts": pg_counts,
            "opensearch_alias_counts": os_counts,
        }

    return {
        "status": "passed" if not failures else "failed",
        "failures": failures,
        "migration": migration_report,
        "schools": schools,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run live Postgres/OpenSearch data gate for MVP normalized data.")
    parser.add_argument("--postgres-dsn", default="postgresql://edumeta:edumeta@127.0.0.1:5432/edumeta")
    parser.add_argument("--opensearch-url", default="http://127.0.0.1:9200")
    parser.add_argument("--data-dir", default="data/normalized/mit")
    parser.add_argument("--university-id", default="mit")
    parser.add_argument("--data-root", default=None, help="When set, load/publish/verify every normalized school under this root.")
    parser.add_argument("--migrations-dir", default="infra/postgres")
    parser.add_argument("--timeout-seconds", type=int, default=180)
    parser.add_argument("--output-path", default=None)
    args = parser.parse_args()
    data_dirs = discover_data_dirs(Path(args.data_root)) if args.data_root else {args.university_id: Path(args.data_dir)}

    report = run_live_data_gate(
        postgres_dsn=args.postgres_dsn,
        opensearch_url=args.opensearch_url,
        data_dirs=data_dirs,
        migrations_dir=Path(args.migrations_dir),
        timeout_seconds=args.timeout_seconds,
    )
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    output_path = Path(args.output_path) if args.output_path else default_report_path()
    write_gate_report(output_path, report)
    print(f"report_path={output_path}")
    if report["status"] != "passed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
