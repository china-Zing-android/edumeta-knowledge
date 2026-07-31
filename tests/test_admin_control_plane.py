from __future__ import annotations

import tempfile
import unittest
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


class _Connection:
    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def transaction(self):
        return self

    def cursor(self):
        return _Cursor()


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


if __name__ == "__main__":
    unittest.main()
