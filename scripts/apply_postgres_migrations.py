from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any


def migration_files(migrations_dir: Path) -> list[Path]:
    return sorted(path for path in migrations_dir.glob("*.sql") if path.is_file())


def apply_migrations(dsn: str, migrations_dir: Path) -> dict[str, Any]:
    try:
        import psycopg
    except ImportError as exc:
        raise RuntimeError("psycopg is required to apply Postgres migrations.") from exc

    files = migration_files(migrations_dir)
    applied: list[str] = []
    skipped: list[str] = []

    with psycopg.connect(dsn) as connection:
        with connection.transaction():
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS schema_migrations (
                      version TEXT PRIMARY KEY,
                      applied_at TIMESTAMPTZ NOT NULL DEFAULT now()
                    )
                    """
                )
                cursor.execute("SELECT version FROM schema_migrations")
                existing = {row[0] for row in cursor.fetchall()}
                for path in files:
                    version = path.name
                    if version in existing:
                        skipped.append(version)
                        continue
                    cursor.execute(path.read_text(encoding="utf-8"))
                    cursor.execute("INSERT INTO schema_migrations (version) VALUES (%s)", (version,))
                    applied.append(version)

    return {
        "migrations_dir": str(migrations_dir),
        "applied": applied,
        "skipped": skipped,
        "status": "ok",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply SQL migrations to Postgres.")
    parser.add_argument("--postgres-dsn", required=True)
    parser.add_argument("--migrations-dir", default="infra/postgres")
    args = parser.parse_args()

    report = apply_migrations(args.postgres_dsn, Path(args.migrations_dir))
    import json

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
