from __future__ import annotations

import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import httpx

from scripts.university_md_batch import build_manifest, pending_rows, poll_ingestion, run_preflight, upload_school
from catalog_parser.deep_v2_parser import parse_deep_v2_markdown
from catalog_parser.mit_parser import extract_capture_date


def write_document(path: Path, title: str, body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n\n> **Data capture date**: 2026-07-24\n\n{body}\n", encoding="utf-8")


class UniversityMarkdownBatchTests(unittest.TestCase):
    def test_resume_state_is_invalidated_by_content_or_audit_version_change(self) -> None:
        records = [{"university_id": "example", "content_sha256": "new-hash"}]
        preflight = {"example": {"quality_audit": {"audit_version": "rules-v2"}}}

        stale_hash = {"example": {"status": "published", "content_sha256": "old-hash", "audit_version": "rules-v2"}}
        stale_rules = {"example": {"status": "published", "content_sha256": "new-hash", "audit_version": "rules-v1"}}
        current = {"example": {"status": "published", "content_sha256": "new-hash", "audit_version": "rules-v2"}}

        self.assertEqual(pending_rows(records, stale_hash, preflight), records)
        self.assertEqual(pending_rows(records, stale_rules, preflight), records)
        self.assertEqual(pending_rows(records, current, preflight), [])

    def test_manifest_keeps_country_scoped_ids_for_same_acronym(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_document(root / "us/SMU_知识库_完整深度数据_v2.md", "Southern Methodist University (SMU) Admissions Knowledge Base")
            write_document(root / "sg/SMU_知识库_完整深度数据_v2.md", "Singapore Management University (SMU) Knowledge Base")

            rows, summary = build_manifest(root)

        self.assertEqual(summary["enabled"], 2)
        self.assertEqual({row["university_id"] for row in rows}, {"us_smu", "sg_smu"})

    def test_manifest_marks_smaller_same_school_document_as_duplicate(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_document(root / "us/BU_知识库_完整深度数据_v2.md", "Boston University (BU) Admissions Knowledge Base", "long" * 100)
            write_document(root / "us/BostonUniversity_知识库_完整深度数据_v2.md", "Boston University Admissions Knowledge Base", "short")

            rows, summary = build_manifest(root)

        active = next(row for row in rows if row["enabled"])
        duplicate = next(row for row in rows if not row["enabled"])
        self.assertEqual(summary["duplicates"], 1)
        self.assertEqual(active["university_id"], "bu")
        self.assertEqual(duplicate["duplicate_of"], "bu")

    def test_capture_date_supports_localized_metadata(self) -> None:
        self.assertEqual(extract_capture_date("> 生成日期: 2026-07-10"), "2026-07-10")
        self.assertEqual(extract_capture_date("> 采集日期：2026-07-11"), "2026-07-11")

    def test_deep_parser_accepts_unnumbered_program_table_and_relative_urls(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "example.md"
            path.write_text(
                """# Example University Knowledge Base

> **Data capture date**: 2026-07-24
> Official website: https://www.example.edu/about

## Undergraduate Education

| Program Name | Degree Type | School | URL |
| --- | --- | --- | --- |
| Computer Science | BS | School of Engineering | /programs/computer-science |
""",
                encoding="utf-8",
            )

            result = parse_deep_v2_markdown("example", path)

        self.assertEqual(len(result.catalog_entries), 1)
        self.assertEqual(result.catalog_entries[0]["program_name"], "Computer Science")
        self.assertEqual(result.catalog_entries[0]["school"], "School of Engineering")
        self.assertEqual(result.catalog_entries[0]["source_url"], "https://www.example.edu/programs/computer-science")

    def test_deep_parser_accepts_blank_lines_between_table_rows_and_late_base_url(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "example.md"
            path.write_text(
                """# Example University Knowledge Base
> **Data capture date**: 2026-07-24

## Undergraduate Education
| Program Name | Degree Type | URL |
| --- | --- | --- |

| Computer Science | BS | /programs/computer-science |

| Economics | BA | /programs/economics |

## Evidence
| Evidence ID | Data key | URL |
| --- | --- | --- |
| E-001 | institution.name | https://www.example.edu/about |
""",
                encoding="utf-8",
            )

            result = parse_deep_v2_markdown("example", path)

        self.assertEqual([row["program_name"] for row in result.catalog_entries], ["Computer Science", "Economics"])
        self.assertEqual(result.catalog_entries[0]["source_url"], "https://www.example.edu/programs/computer-science")

    def test_deep_parser_uses_official_document_base_when_catalog_has_no_url_column(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "example.md"
            path.write_text(
                """# Example University Knowledge Base
> **Data capture date**: 2026-07-24

| Program Name | Degree Type |
| --- | --- |
| Computer Science | BS |

## Evidence
Source: https://www.example.edu/about
""",
                encoding="utf-8",
            )

            result = parse_deep_v2_markdown("example", path)

        self.assertEqual(result.catalog_entries[0]["source_url"], "https://www.example.edu")

    def test_preflight_requires_review_for_implausibly_small_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            relative = "us/Small_知识库_完整深度数据_v2.md"
            path = root / relative
            path.parent.mkdir(parents=True)
            path.write_text(
                """# Small University Knowledge Base
> **Data capture date**: 2026-07-24
> Official website: https://small.example.edu/about

| Program Name | Degree Type | URL |
| --- | --- | --- |
| Example Program | BS | https://small.example.edu/program |
""",
                encoding="utf-8",
            )

            result = run_preflight(
                {"university_id": "small", "relative_path": relative, "parser_adapter": "auto"},
                root,
            )

        self.assertEqual(result["status"], "needs_review")
        self.assertEqual(result["review_reasons"], ["catalog_entries_below_5"])

    def test_preflight_fails_when_declared_complete_catalog_is_mostly_missing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            relative = "us/Incomplete_知识库_完整深度数据_v2.md"
            path = root / relative
            path.parent.mkdir(parents=True)
            path.write_text(
                """# Incomplete University Knowledge Base
> **Data capture date**: 2026-07-24
> Official website: https://incomplete.example.edu/about

| Dimension | Count |
| --- | --- |
| Total degree programs (including minors) | 120 |

| Program Name | Degree Type | URL |
| --- | --- | --- |
| Example Program | BS | https://incomplete.example.edu/program |
""",
                encoding="utf-8",
            )

            result = run_preflight(
                {"university_id": "incomplete", "relative_path": relative, "parser_adapter": "auto"},
                root,
            )

        self.assertEqual(result["status"], "failed")
        self.assertIn("catalog_completeness", result["failures"])

    def test_preflight_classifies_zero_catalog_as_coverage_gate_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            relative = "us/Empty_知识库_完整深度数据_v2.md"
            write_document(root / relative, "Empty University Knowledge Base", "No catalog table is present.")

            result = run_preflight(
                {"university_id": "empty", "relative_path": relative, "parser_adapter": "auto"},
                root,
            )

        self.assertEqual(result["status"], "failed")
        self.assertIn("catalog_completeness", result["failures"])
        self.assertIn("CAT-COVERAGE-001", result["quality_audit"]["matched_rule_ids"])

    def test_upload_and_poll_support_create_then_unchanged(self) -> None:
        class Handler(BaseHTTPRequestHandler):
            posts = 0

            def do_POST(self):  # noqa: N802
                Handler.posts += 1
                self.rfile.read(int(self.headers.get("Content-Length", "0")))
                payload = (
                    {"run_id": "run_1", "status": "accepted", "operation": "create"}
                    if Handler.posts == 1
                    else {"run_id": "run_2", "status": "unchanged", "operation": "unchanged"}
                )
                self.send_response(202)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(__import__("json").dumps(payload).encode())

            def do_GET(self):  # noqa: N802
                payload = {"run_id": "run_1", "status": "published", "counts": {"catalog_entries": 10}}
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(__import__("json").dumps(payload).encode())

            def log_message(self, format, *args):  # noqa: A002
                return

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            relative = "us/Example_知识库_完整深度数据_v2.md"
            path = root / relative
            path.parent.mkdir(parents=True)
            path.write_text("# Example\n", encoding="utf-8")
            record = {
                "university_id": "example",
                "university_name": "Example University",
                "aliases": ["Example"],
                "country_code": "US",
                "region": None,
                "school_tier": "core",
                "relative_path": relative,
            }
            server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            base_url = f"http://127.0.0.1:{server.server_address[1]}"
            try:
                with httpx.Client(timeout=5) as client:
                    first = upload_school(client, base_url, root, record)
                    terminal = poll_ingestion(client, base_url, first["run_id"], 5)
                    second = upload_school(client, base_url, root, record)
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=2)

        self.assertEqual(terminal["status"], "published")
        self.assertEqual(second["status"], "unchanged")


if __name__ == "__main__":
    unittest.main()
