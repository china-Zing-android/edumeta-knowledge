from __future__ import annotations

import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from fast_router.admin import AdminControlPlane, MAX_UPLOAD_FILES
from fast_router.ingestion import MAX_MD_FILE_BYTES


class _Cursor:
    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def execute(self, *_args):
        return None

    def fetchall(self):
        return []


class _Connection:
    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def transaction(self):
        return self

    def cursor(self):
        return _Cursor()


class _LegacyRunCursor(_Cursor):
    def fetchall(self):
        return [
            (
                "mit",
                "ing_legacy_mit",
                "mit",
                "update",
                "published",
                "ver_mit_legacy",
                datetime.now(timezone.utc),
                True,
                "Massachusetts Institute of Technology",
            )
        ]


class _LegacyRunConnection(_Connection):
    def cursor(self):
        return _LegacyRunCursor()


class _VersionCursor(_Cursor):
    def fetchall(self):
        return [
            (
                "ver_mit_legacy",
                "mit_20260704_v2",
                "current",
                "input-hash",
                {"catalog_entries": 157},
                datetime.now(timezone.utc),
                datetime.now(timezone.utc),
                None,
                "ing_legacy_mit",
                "published",
                None,
                None,
                None,
                "Massachusetts Institute of Technology",
                "US",
                "Massachusetts",
                "mit",
            )
        ]


class _VersionConnection(_Connection):
    def cursor(self):
        return _VersionCursor()


class _Service:
    raw_root = Path(tempfile.gettempdir()) / "edumeta-admin-test"


class AdminControlPlaneTests(unittest.TestCase):
    def setUp(self) -> None:
        self.control = AdminControlPlane(_Service())
        self.control._existing_universities = lambda: {}
        self.control._connect = lambda: _Connection()

    def test_duplicate_university_mapping_is_blocked_with_impact(self) -> None:
        items = [
            {"university_id": "mit", "relative_path": "a.md", "issues": [], "ready": True},
            {"university_id": "mit", "relative_path": "b.md", "issues": [], "ready": True},
        ]

        self.control._mark_duplicate_ids(items)

        for item in items:
            issue = item["issues"][0]
            self.assertEqual(issue["code"], "duplicate_university_id")
            self.assertIn("current", issue["message"])
            self.assertIn("superseded", issue["message"])
            self.assertIn("OpenSearch current", issue["message"])
            self.assertFalse(item["ready"])

    def test_normal_upload_limits_are_enforced_before_preview_storage(self) -> None:
        with self.assertRaisesRegex(ValueError, "at most 20"):
            self.control.create_preview(
                mode="upload",
                uploaded_files=[(f"{index}.md", b"# University") for index in range(MAX_UPLOAD_FILES + 1)],
            )

    def test_exact_file_limit_is_not_rejected_by_preview_item(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "university.md"
            with path.open("wb") as handle:
                handle.write(b"# University\n")
                handle.truncate(MAX_MD_FILE_BYTES)
            item = self.control._make_item(path, root=Path(temp_dir), root_id="root", manifest=None, existing={})

        self.assertEqual(item["size_bytes"], MAX_MD_FILE_BYTES)
        self.assertTrue(item["ready"])

    def test_source_metadata_infers_region_from_markdown_when_manifest_is_empty(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            path = root / "uk" / "Cambridge.md"
            path.parent.mkdir(parents=True)
            path.write_text(
                "# University of Cambridge\n\ncountry: UK\nregion: England\n",
                encoding="utf-8",
            )
            item = self.control._make_item(
                path,
                root=root,
                root_id="universities",
                manifest={"university_id": "cambridge", "country_code": "UK", "region": None},
                existing={},
            )

        self.assertEqual(item["country_code"], "UK")
        self.assertEqual(item["region"], "England")

    def test_source_metadata_uses_existing_university_region_as_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            path = root / "us" / "MIT.md"
            path.parent.mkdir(parents=True)
            path.write_text("# Massachusetts Institute of Technology\n", encoding="utf-8")
            item = self.control._make_item(
                path,
                root=root,
                root_id="universities",
                manifest={"university_id": "mit", "country_code": "US", "region": None},
                existing={"mit": {"country_code": "US", "region": "Massachusetts"}},
            )

        self.assertEqual(item["region"], "Massachusetts")

    def test_source_file_links_to_legacy_run_without_source_relative_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "us" / "MIT.md"
            source.parent.mkdir(parents=True)
            source.write_text("# Massachusetts Institute of Technology\n", encoding="utf-8")
            self.control.roots = {"universities": root}
            self.control._connect = lambda: _LegacyRunConnection()
            self.control._latest_university_versions = lambda: {}

            payload = self.control.source_files()

        self.assertEqual(payload["items"][0]["run_id"], "ing_legacy_mit")
        self.assertEqual(payload["items"][0]["source_status"], "published")

    def test_source_file_links_to_school_version_without_ingestion_run(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "us" / "MIT.md"
            source.parent.mkdir(parents=True)
            source.write_text("# Massachusetts Institute of Technology\n", encoding="utf-8")
            self.control.roots = {"universities": root}
            self.control._latest_university_runs = lambda: {}
            self.control._latest_university_versions = lambda: {
                "mit": {
                    "version_id": "ver_mit_catalog",
                    "dataset_version": "mit_20260704_v2",
                    "publication_state": "current",
                    "created_at": "2026-07-04T00:00:00+00:00",
                    "published_at": "2026-07-04T00:00:00+00:00",
                }
            }

            payload = self.control.source_files()

        item = payload["items"][0]
        self.assertEqual(item["source_status"], "published")
        self.assertEqual(item["version_id"], "ver_mit_catalog")
        self.assertTrue(item["is_current"])
        self.assertIsNone(item["run_id"])

    def test_global_version_listing_returns_versions_without_opening_a_run(self) -> None:
        self.control._connect = lambda: _VersionConnection()

        payload = self.control.list_versions()

        self.assertEqual(payload["total_count"], 1)
        self.assertEqual(payload["items"][0]["version_id"], "ver_mit_legacy")
        self.assertEqual(payload["items"][0]["region"], "Massachusetts")

    def test_server_source_files_are_visible_before_they_create_a_run(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "us" / "mit.md"
            source.parent.mkdir(parents=True)
            source.write_text("# Massachusetts Institute of Technology\n", encoding="utf-8")
            self.control.roots = {"universities": root}

            payload = self.control.source_files()

        self.assertEqual(payload["total_count"], 1)
        self.assertEqual(payload["items"][0]["relative_path"], "us/mit.md")
        self.assertEqual(payload["items"][0]["source_status"], "not_submitted")
        self.assertIsNone(payload["items"][0]["run_id"])


if __name__ == "__main__":
    unittest.main()
