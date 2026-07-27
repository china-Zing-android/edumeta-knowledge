from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from catalog_parser.postgres_loader import (
    build_upsert_sql,
    dry_run_report,
    load_dataset,
    read_jsonl,
    publish_school_version,
    stage_school_records,
)

# PG-backed tests are only run when a test DSN is available; otherwise the
# versioning/uniqueness/link helpers are skipped (Plan §11 perf/acceptance gates
# run the full suite against the local Docker stack).
TEST_DSN = os.getenv("EDUMETA_TEST_DSN", "").strip()


def _need_pg(testcase):
    if not TEST_DSN:
        raise testcase.skipTest("set EDUMETA_TEST_DSN to run PostgreSQL-backed tests")


class PostgresLoaderUnitTests(unittest.TestCase):
    def test_staging_uses_one_bulk_database_operation(self) -> None:
        class CopyContext:
            def __init__(self, cursor) -> None:
                self.cursor = cursor

            def __enter__(self):
                return self

            def write_row(self, row):
                self.cursor.copy_rows.append(row)

            def __exit__(self, exc_type, exc, traceback):
                return False

        class RecordingCursor:
            def __init__(self) -> None:
                self.execute_calls = []
                self.executemany_calls = []
                self.copy_calls = []
                self.copy_rows = []

            def execute(self, sql, params=None):
                self.execute_calls.append((sql, params))

            def executemany(self, sql, params):
                self.executemany_calls.append((sql, list(params)))

            def copy(self, sql):
                self.copy_calls.append(sql)
                return CopyContext(self)

        cursor = RecordingCursor()
        dataset = {
            "source_registry": [{
                "source_id": "src_example",
                "canonical_url": "https://example.edu/catalog",
                "source_url": "https://example.edu/catalog",
                "url_type": "catalog",
                "topics": ["catalog"],
                "official_source": True,
                "priority": 1,
                "capture_date": "2026-07-27",
                "dataset_version": "example_v1",
                "entry_ids": ["ent_example"],
            }],
            "url_manifest": [{
                "source_id": "src_example",
                "entry_ids": ["ent_example"],
                "topics": ["catalog"],
            }],
            "catalog_entries": [{
                "entry_id": "ent_example",
                "discipline_ids": ["computer_science"],
                "discipline_labels": ["Computer Science"],
            }],
            "quick_facts": [],
            "entity_contexts": [],
        }

        counts = stage_school_records(
            cursor,
            run_id="run_example",
            university_id="example",
            version_id="ver_example",
            dataset=dataset,
        )

        self.assertEqual(len(cursor.copy_calls), 1)
        self.assertEqual(cursor.executemany_calls, [])
        self.assertEqual(cursor.execute_calls, [])
        self.assertEqual(len(cursor.copy_rows), 4)
        self.assertEqual(counts["catalog_entries"], 1)

    def test_promotion_sends_independent_inserts_through_pipeline(self) -> None:
        class RecordingCursor:
            def __init__(self) -> None:
                self.execute_calls = []

            def execute(self, sql, params=None):
                self.execute_calls.append((sql, params))

            def fetchall(self):
                return []

        class PipelineContext:
            def __init__(self, connection) -> None:
                self.connection = connection

            def __enter__(self):
                self.connection.pipeline_entries += 1

            def __exit__(self, exc_type, exc, traceback):
                return False

        class RecordingConnection:
            def __init__(self) -> None:
                self.recording_cursor = RecordingCursor()
                self.pipeline_entries = 0

            def cursor(self):
                return self.recording_cursor

            def pipeline(self):
                return PipelineContext(self)

        connection = RecordingConnection()

        report = publish_school_version(
            connection,
            run_id="run_example",
            university_id="example",
            version_id="ver_example",
            input_hash="hash",
            activate=False,
        )

        self.assertEqual(connection.pipeline_entries, 1)
        self.assertEqual(report["promoted"]["catalog_entries"], 0)

    def test_active_weknora_job_uniqueness_is_scoped_by_knowledge_base(self) -> None:
        schema = (Path("infra/postgres/001_initial_schema.sql")).read_text("utf-8")

        self.assertIn(
            "ON weknora_import_jobs (university_id, knowledge_base_id, source_id)",
            schema,
        )

    def test_dry_run_validates_existing_mit_dataset(self) -> None:
        report = dry_run_report(Path("data/normalized/mit"), "mit")

        self.assertEqual(report["status"], "validated")
        self.assertEqual(report["counts"]["catalog_entries"], 157)
        self.assertGreaterEqual(report["counts"]["source_registry"], 100)
        self.assertGreaterEqual(report["counts"]["url_manifest"], 100)
        self.assertGreaterEqual(report["counts"]["quick_facts"], 200)
        self.assertEqual(report["counts"]["entity_contexts"], 158)
        self.assertEqual(report["tables"]["quick_facts"], "fact_store")
        self.assertEqual(report["tables"]["entity_contexts"], "entity_contexts")

    def test_initial_schema_contains_versioned_entity_context_table(self) -> None:
        schema = Path("infra/postgres/001_initial_schema.sql").read_text("utf-8")

        self.assertIn("CREATE TABLE IF NOT EXISTS entity_contexts", schema)
        self.assertIn("PRIMARY KEY (university_id, version_id, context_id)", schema)

    def test_ingestion_status_constraint_covers_observable_progress_stages(self) -> None:
        schema = Path("infra/postgres/001_initial_schema.sql").read_text("utf-8")

        self.assertIn("'parsing'", schema)
        self.assertIn("'weknora_preparing'", schema)

    def test_build_upsert_sql_targets_primary_key(self) -> None:
        sql = build_upsert_sql("catalog_entries", "entry_id", ["entry_id", "university_id", "program_name"])

        self.assertIn("INSERT INTO catalog_entries", sql)
        self.assertIn("ON CONFLICT (entry_id)", sql)
        self.assertIn("program_name=EXCLUDED.program_name", sql)
        self.assertNotIn("entry_id=EXCLUDED.entry_id", sql)

    def test_loader_rejects_wrong_university_id(self) -> None:
        with self.assertRaises(ValueError):
            load_dataset(Path("data/normalized/mit"), "stanford")

    def test_read_jsonl_rejects_non_object_line(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bad.jsonl"
            path.write_text("[1, 2, 3]\n", encoding="utf-8")

            with self.assertRaises(ValueError):
                read_jsonl(path)


def _apply_schema(cursor) -> None:
    schema = (Path(__file__).resolve().parents[1] / "infra" / "postgres" / "001_initial_schema.sql").read_text("utf-8")
    cursor.execute(schema)


def _mit_dataset():
    """A minimal hand-built dataset exercising source/link/fact/job relationships."""
    university_id = "unitu"
    return {
        "source_registry.jsonl": [
            {
                "source_id": f"src_{university_id}_catalog_example_edu_cs",
                "university_id": university_id,
                "program_id": None,
                "source_url": "https://catalog.example.edu/cs",
                "canonical_url": "https://catalog.example.edu/cs",
                "url_type": "degree_chart",
                "topics": ["catalog", "programs"],
                "official_source": True,
                "priority": 1,
                "content_hash": "abc",
                "weknora_content_hash": "abc",
                "crawl_status": "success",
                "parser_status": "parsed",
                "weknora_import_status": "pending",
                "status": "active",
                "capture_date": "2026-07-15",
                "last_verified": "2026-07-15",
                "dataset_version": "unitu_20260715_v1",
                "entry_ids": ["ent_unitu_undergraduate_sb_cs"],
            }
        ],
        "catalog_entries.jsonl": [
            {
                "entry_id": "ent_unitu_undergraduate_sb_cs",
                "university_id": university_id,
                "program_id": None,
                "school": "School of Engineering",
                "department": "Computer Science",
                "level": "undergraduate",
                "degree_level": "SB",
                "degree_full_name": None,
                "course_code": "6-3",
                "program_name": "Computer Science",
                "canonical_program_name": "Computer Science",
                "aliases": ["CS"],
                "source_id": f"src_{university_id}_catalog_example_edu_cs",
                "source_url": "https://catalog.example.edu/cs",
                "topics": ["catalog", "programs"],
                "search_text": "unitu Computer Science SB 6-3",
                "cross_school": False,
                "cross_school_names": [],
                "raw_section_path": "School of Engineering > Computer Science",
                "capture_date": "2026-07-15",
                "dataset_version": "unitu_20260715_v1",
                "source_version": None,
                "status": "active",
            }
        ],
        "quick_facts.jsonl": [
            {
                "fact_id": f"fact_{university_id}_cs_application_fee",
                "university_id": university_id,
                "program_id": None,
                "entry_id": "ent_unitu_undergraduate_sb_cs",
                "fact_type": "application_fee",
                "fact_key": "application_fee",
                "raw_value": "$75.00",
                "normalized_value": {"amount": 75.0, "currency": "USD"},
                "unit": None,
                "currency": "USD",
                "admission_cycle": None,
                "term": "Fall",
                "source_id": f"src_{university_id}_catalog_example_edu_cs",
                "source_url": "https://catalog.example.edu/cs",
                "evidence_ids": ["E-1"],
                "weknora_chunk_ids": [],
                "capture_date": "2026-07-15",
                "dataset_version": "unitu_20260715_v1",
                "source_version": None,
                "confidence": 0.9,
                "review_status": "review_required",
                "conflict_status": "none",
                "status": "active",
            }
        ],
        "url_manifest.jsonl": [
            {
                "url_id": f"url_{university_id}_catalog_example_edu_cs",
                "source_id": f"src_{university_id}_catalog_example_edu_cs",
                "university_id": university_id,
                "program_id": None,
                "entry_ids": ["ent_unitu_undergraduate_sb_cs"],
                "source_url": "https://catalog.example.edu/cs",
                "canonical_url": "https://catalog.example.edu/cs",
                "url_type": "degree_chart",
                "topics": ["catalog", "programs"],
                "official_source": True,
                "priority": 1,
                "weknora_collection_id": None,
                "weknora_knowledge_id": None,
                "weknora_document_id": None,
                "weknora_chunk_ids": [],
                "import_status": "pending",
                "import_error": None,
                "content_hash": "abc",
                "capture_date": "2026-07-15",
                "dataset_version": "unitu_20260715_v1",
                "source_version": None,
                "status": "active",
            }
        ],
    }


def _write_dataset(data_dir: Path, university_id: str) -> dict:
    from catalog_parser.postgres_loader import load_dataset
    from catalog_parser.disciplines import enrich_catalog_entries

    files = _mit_dataset()
    files = {name: [{**r, "university_id": university_id} for r in rows] for name, rows in files.items()}
    enrich_catalog_entries(files["catalog_entries.jsonl"])
    for name, rows in files.items():
        import json

        (data_dir / name).write_text(
            "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8"
        )
    return load_dataset(data_dir, university_id)


@unittest.skipUnless(TEST_DSN, "EDUMETA_TEST_DSN required")
class PostgresVersioningTests(unittest.TestCase):
    university_id = "unitu"

    def _clear_fixture_university(self) -> None:
        with self._conn.transaction(), self._conn.cursor() as cursor:
            _apply_schema(cursor)
            for table in [
                "catalog_entry_disciplines",
                "source_entry_links",
                "fact_store",
                "entity_contexts",
                "catalog_entries",
                "weknora_import_jobs",
                "ingestion_records",
                "source_registry",
                "ingestion_runs",
                "school_versions",
                "universities",
            ]:
                cursor.execute(f"DELETE FROM {table} WHERE university_id=%s", (self.university_id,))

    def setUp(self) -> None:
        _need_pg(self)
        import psycopg

        self._conn = psycopg.connect(TEST_DSN)
        # Isolate only this fixture university. Never drop shared Compose tables:
        # the same database may contain live local acceptance data.
        self._clear_fixture_university()
        self._tmp = tempfile.TemporaryDirectory()
        self._data_dir = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._conn.rollback()
        self._clear_fixture_university()
        self._tmp.cleanup()
        self._conn.close()

    def test_publish_sets_current_version_and_links(self) -> None:
        from catalog_parser.postgres_loader import (
            current_version,
            load_school_to_postgres,
        )

        _write_dataset(self._data_dir, self.university_id)
        report = load_school_to_postgres(self._data_dir, self.university_id, TEST_DSN, publish=True)

        self.assertEqual(report["status"], "published")
        self.assertEqual(current_version(self._conn, self.university_id), report["version_id"])

        with self._conn.cursor() as cursor:
            # canonical URL stored exactly once (Plan §3 uniqueness)
            cursor.execute(
                "SELECT count(*) FROM source_registry WHERE university_id=%s AND canonical_url=%s",
                (self.university_id, "https://catalog.example.edu/cs"),
            )
            self.assertEqual(cursor.fetchone()[0], 1)

            # source_entry_links carries the catalog relationship (no JSON-array link)
            cursor.execute(
                """
                SELECT count(*) FROM source_entry_links
                 WHERE source_id=%s AND target_entity='catalog_entry' AND target_id=%s
                """,
                (f"src_{self.university_id}_catalog_example_edu_cs", "ent_unitu_undergraduate_sb_cs"),
            )
            self.assertEqual(cursor.fetchone()[0], 1)

            # fact persisted with review state
            cursor.execute(
                "SELECT review_status, conflict_status FROM fact_store WHERE fact_id=%s",
                (f"fact_{self.university_id}_cs_application_fee",),
            )
            review, conflict = cursor.fetchone()
            self.assertEqual(review, "review_required")
            self.assertEqual(conflict, "none")

            cursor.execute(
                "SELECT discipline_id FROM catalog_entry_disciplines WHERE university_id=%s AND entry_id=%s",
                (self.university_id, "ent_unitu_undergraduate_sb_cs"),
            )
            self.assertIn("computer_science", {row[0] for row in cursor.fetchall()})

            cursor.execute(
                "SELECT university_name, school_tier, status FROM universities WHERE university_id=%s",
                (self.university_id,),
            )
            self.assertEqual(cursor.fetchone(), ("Unitu", "core", "active"))

            cursor.execute(
                "SELECT count(*) FROM entity_contexts WHERE university_id=%s",
                (self.university_id,),
            )
            self.assertEqual(cursor.fetchone()[0], 2)

            cursor.execute(
                "SELECT count(*) FROM ingestion_records WHERE run_id=%s",
                (report["run_id"],),
            )
            self.assertEqual(cursor.fetchone()[0], 0)

    def test_new_version_enqueues_continuation_for_nonterminal_weknora_source(self) -> None:
        from fast_router.ingestion import IngestionService

        with self._conn.transaction(), self._conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO universities (university_id, university_name, aliases, school_tier, status) VALUES (%s, 'Unitu', '[]', 'core', 'active')",
                (self.university_id,),
            )
            for version_id, state in (("ver_old", "superseded"), ("ver_new", "current")):
                cursor.execute(
                    "INSERT INTO school_versions (version_id, university_id, dataset_version, publication_state, input_hash, record_counts) VALUES (%s, %s, %s, %s, %s, '{}')",
                    (version_id, self.university_id, version_id, state, f"hash_{version_id}"),
                )
            cursor.execute(
                "INSERT INTO ingestion_runs (run_id, university_id, school_tier, operation, version_id, input_hash, status) VALUES ('run_new', %s, 'core', 'update', 'ver_new', 'hash_ver_new', 'publishing')",
                (self.university_id,),
            )
            for version_id in ("ver_old", "ver_new"):
                cursor.execute(
                    """
                    INSERT INTO source_registry
                      (source_id, university_id, version_id, canonical_url, url_type, topics,
                       official_source, priority, crawl_status, parser_status, weknora_import_status,
                       weknora_knowledge_base_id, weknora_knowledge_id, status, capture_date, last_verified, dataset_version)
                    VALUES ('src_unitu_catalog', %s, %s, 'https://example.edu/catalog', 'catalog', '[]',
                            true, 1, 'success', 'parsed', 'running', 'kb_unitu', 'knowledge_123', 'active',
                            '2026-07-16', '2026-07-16', %s)
                    """,
                    (self.university_id, version_id, version_id),
                )
            cursor.execute(
                """
                INSERT INTO weknora_import_jobs
                  (job_id, source_id, run_id, university_id, version_id, knowledge_id, status, source_url)
                VALUES ('job_old', 'src_unitu_catalog', NULL, %s, 'ver_old', 'knowledge_123', 'superseded', 'https://example.edu/catalog')
                """,
                (self.university_id,),
            )

            IngestionService._enqueue_weknora_jobs(cursor, "run_new", self.university_id, "ver_new")
            cursor.execute(
                "SELECT status, knowledge_id FROM weknora_import_jobs WHERE university_id=%s AND version_id='ver_new'",
                (self.university_id,),
            )

            self.assertEqual(cursor.fetchone(), ("queued", "knowledge_123"))

    def test_canonical_url_uniqueness_within_university(self) -> None:
        from catalog_parser.postgres_loader import load_school_to_postgres

        _write_dataset(self._data_dir, self.university_id)
        load_school_to_postgres(self._data_dir, self.university_id, TEST_DSN, publish=True)

        # a second source with the SAME canonical_url must violate the unique index
        from psycopg.errors import UniqueViolation

        with self._conn.cursor() as cursor:
            with self.assertRaises(UniqueViolation):
                cursor.execute(
                    """
                    INSERT INTO source_registry
                      (source_id, university_id, version_id, canonical_url, url_type,
                       topics, official_source, priority, crawl_status, parser_status,
                       weknora_import_status, status, capture_date, last_verified, dataset_version)
                    VALUES ('src_dup', %s,
                       (SELECT version_id FROM school_versions WHERE university_id=%s AND publication_state='current'),
                       'https://catalog.example.edu/cs', 'degree_chart', '[]'::jsonb, true, 1,
                       'success', 'parsed', 'pending', 'active', '2026-07-15', '2026-07-15', 'unitu_20260715_v1')
                    """,
                    (self.university_id, self.university_id),
                )

    def test_rollback_preserves_previous_current(self) -> None:
        from catalog_parser.postgres_loader import (
            current_version,
            load_school_to_postgres,
            rollback_school_version,
        )

        _write_dataset(self._data_dir, self.university_id)
        first = load_school_to_postgres(self._data_dir, self.university_id, TEST_DSN, publish=True)
        self.assertEqual(current_version(self._conn, self.university_id), first["version_id"])

        # promote a second version, then roll back to the first
        with self._conn.transaction():
            with self._conn.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE school_versions SET publication_state='current', published_at=now()
                     WHERE university_id=%s AND version_id<>%s
                    """,
                    (self.university_id, first["version_id"]),
                )
                cursor.execute(
                    """
                    UPDATE school_versions SET publication_state='superseded'
                     WHERE university_id=%s AND version_id=%s
                    """,
                    (self.university_id, first["version_id"]),
                )
        rollback_school_version(self._conn, university_id=self.university_id, to_version_id=first["version_id"])
        self.assertEqual(current_version(self._conn, self.university_id), first["version_id"])

    def test_new_version_retains_previous_authoritative_rows(self) -> None:
        from catalog_parser.postgres_loader import load_school_to_postgres

        _write_dataset(self._data_dir, self.university_id)
        first = load_school_to_postgres(self._data_dir, self.university_id, TEST_DSN, publish=True)

        catalog_path = self._data_dir / "catalog_entries.jsonl"
        import json

        rows = [json.loads(line) for line in catalog_path.read_text("utf-8").splitlines() if line]
        rows[0]["program_name"] = "Computer Science and Engineering"
        rows[0]["dataset_version"] = "unitu_20260715_v2"
        catalog_path.write_text("".join(json.dumps(row) + "\n" for row in rows), "utf-8")
        second = load_school_to_postgres(self._data_dir, self.university_id, TEST_DSN, publish=True)

        self.assertNotEqual(first["version_id"], second["version_id"])
        with self._conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT version_id, program_name FROM catalog_entries
                 WHERE university_id=%s AND entry_id=%s ORDER BY version_id
                """,
                (self.university_id, "ent_unitu_undergraduate_sb_cs"),
            )
            persisted = cursor.fetchall()
        self.assertEqual(len(persisted), 2)
        self.assertEqual({row[1] for row in persisted}, {"Computer Science", "Computer Science and Engineering"})

    def test_activating_new_version_supersedes_pending_jobs_from_old_version(self) -> None:
        from catalog_parser.postgres_loader import activate_school_version, load_school_to_postgres

        _write_dataset(self._data_dir, self.university_id)
        first = load_school_to_postgres(self._data_dir, self.university_id, TEST_DSN, publish=True)

        with self._conn.transaction():
            with self._conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO weknora_import_jobs
                      (job_id, source_id, run_id, university_id, version_id, status, source_url)
                    VALUES ('wkj_old', %s, %s, %s, %s, 'queued', 'https://catalog.example.edu/cs')
                    """,
                    (
                        f"src_{self.university_id}_catalog_example_edu_cs",
                        first["run_id"],
                        self.university_id,
                        first["version_id"],
                    ),
                )
                cursor.execute(
                    """
                    INSERT INTO school_versions
                      (version_id, university_id, dataset_version, publication_state, input_hash)
                    VALUES ('ver_unitu_next', %s, 'unitu_20260715_v2', 'staging', 'next-hash')
                    """,
                    (self.university_id,),
                )
                cursor.execute(
                    """
                    INSERT INTO ingestion_runs
                      (run_id, university_id, school_tier, version_id, input_hash, status)
                    VALUES ('ing_unitu_next', %s, 'core', 'ver_unitu_next', 'next-hash', 'publishing')
                    """,
                    (self.university_id,),
                )
                activate_school_version(
                    cursor,
                    university_id=self.university_id,
                    version_id="ver_unitu_next",
                    run_id="ing_unitu_next",
                )

        with self._conn.cursor() as cursor:
            cursor.execute("SELECT status, failure_reason FROM weknora_import_jobs WHERE job_id='wkj_old'")
            status, reason = cursor.fetchone()

        self.assertEqual(status, "superseded")
        self.assertEqual(reason, "dataset_version_superseded")

    def test_weknora_worker_claims_jobs_only_from_current_version(self) -> None:
        from catalog_parser.postgres_loader import load_school_to_postgres
        from fast_router.weknora_worker import WeknoraJobWorker

        _write_dataset(self._data_dir, self.university_id)
        current = load_school_to_postgres(self._data_dir, self.university_id, TEST_DSN, publish=True)

        with self._conn.transaction():
            with self._conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO weknora_import_jobs
                      (job_id, source_id, run_id, university_id, version_id,
                       knowledge_base_id, status, source_url)
                    VALUES ('wkj_current', %s, %s, %s, %s, 'kb_unitu', 'queued',
                            'https://catalog.example.edu/cs')
                    """,
                    (
                        f"src_{self.university_id}_catalog_example_edu_cs",
                        current["run_id"],
                        self.university_id,
                        current["version_id"],
                    ),
                )
                cursor.execute(
                    """
                    INSERT INTO school_versions
                      (version_id, university_id, dataset_version, publication_state, input_hash)
                    VALUES ('ver_unitu_old', %s, 'unitu_old', 'superseded', 'old-hash')
                    """,
                    (self.university_id,),
                )
                cursor.execute(
                    """
                    INSERT INTO source_registry
                      (source_id, university_id, version_id, canonical_url, url_type,
                       topics, official_source, priority, crawl_status, parser_status,
                       weknora_import_status, status, capture_date, last_verified, dataset_version)
                    VALUES ('src_unitu_old', %s, 'ver_unitu_old', 'https://catalog.example.edu/old',
                            'catalog', '[]'::jsonb, true, 1, 'success', 'parsed', 'pending',
                            'active', '2026-07-15', '2026-07-15', 'unitu_old')
                    """,
                    (self.university_id,),
                )
                cursor.execute(
                    """
                    INSERT INTO weknora_import_jobs
                      (job_id, source_id, run_id, university_id, version_id,
                       knowledge_base_id, status, source_url)
                    VALUES ('wkj_old', %s, %s, %s, 'ver_unitu_old', 'kb_unitu', 'queued',
                            'https://catalog.example.edu/old')
                    """,
                    (
                        "src_unitu_old",
                        current["run_id"],
                        self.university_id,
                    ),
                )

        worker = WeknoraJobWorker.__new__(WeknoraJobWorker)
        worker.postgres_dsn = TEST_DSN
        worker.batch_size = 4
        claimed = worker._claim_jobs()

        self.assertEqual([job["job_id"] for job in claimed], ["wkj_current"])


if __name__ == "__main__":
    unittest.main()
