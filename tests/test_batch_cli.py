from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MIT_MD = ROOT / "docs/MIT_知识库_完整深度数据_v2.md"
MIT_DATA = ROOT / "data/normalized/mit"


def subprocess_env() -> dict[str, str]:
    paths = [
        str(ROOT / "apps/fast-router/src"),
        str(ROOT / "pipelines/catalog-parser/src"),
        str(ROOT / "pipelines/indexer/src"),
    ]
    existing = os.environ.get("PYTHONPATH")
    if existing:
        paths.append(existing)
    return {**os.environ, "PYTHONPATH": os.pathsep.join(paths)}


class BatchCliTests(unittest.TestCase):
    def test_parse_school_all_discovers_markdown_and_writes_normalized_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_root = root / "raw-md"
            out_root = root / "normalized"
            input_root.mkdir()
            shutil.copyfile(MIT_MD, input_root / "mit.md")

            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "catalog_parser.cli",
                    "parse-school",
                    "--all",
                    "--input-root",
                    str(input_root),
                    "--out-root",
                    str(out_root),
                ],
                check=True,
                capture_output=True,
                text=True,
                cwd=ROOT,
                env=subprocess_env(),
            )

            report = json.loads(completed.stdout)
            self.assertEqual(report["status"], "success")
            self.assertEqual(report["succeeded"], 1)
            self.assertTrue((out_root / "mit/catalog_entries.jsonl").exists())

    def test_parse_school_all_can_use_generic_structured_fallback_for_unknown_schools(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_root = root / "raw-md"
            out_root = root / "normalized"
            input_root.mkdir()
            (input_root / "exampleu.md").write_text(
                """# Example University L1

**University ID**: exampleu
**University name**: Example University
**Data capture date**: 2026-07-09

## Catalog Entries

| school | department | level | degree_level | program_name | source_url |
| --- | --- | --- | --- | --- | --- |
| School of Engineering | Computer Science | graduate | SM | Computer Science MS | https://example.edu/cs/ms |

## Quick Facts

| fact_type | fact_key | raw_value | source_url | program_name |
| --- | --- | --- | --- | --- |
| deadline | application_deadline | December 15, 2026 | https://example.edu/cs/ms/admissions | Computer Science MS |
""",
                encoding="utf-8",
            )

            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "catalog_parser.cli",
                    "parse-school",
                    "--all",
                    "--input-root",
                    str(input_root),
                    "--out-root",
                    str(out_root),
                    "--default-adapter",
                    "generic_structured",
                ],
                check=True,
                capture_output=True,
                text=True,
                cwd=ROOT,
                env=subprocess_env(),
            )

            report = json.loads(completed.stdout)
            self.assertEqual(report["status"], "success")
            self.assertEqual(report["succeeded"], 1)
            self.assertTrue((out_root / "exampleu/catalog_entries.jsonl").exists())
            self.assertTrue((out_root / "exampleu/quick_facts.jsonl").exists())

    def test_validate_school_all_discovers_data_dirs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            data_root = Path(temp_dir) / "normalized"
            shutil.copytree(MIT_DATA, data_root / "mit")

            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "catalog_parser.cli",
                    "validate-school",
                    "--all",
                    "--data-root",
                    str(data_root),
                ],
                check=True,
                capture_output=True,
                text=True,
                cwd=ROOT,
                env=subprocess_env(),
            )

            report = json.loads(completed.stdout)
            self.assertEqual(report["status"], "success")
            self.assertEqual(report["results"][0]["status"], "passed")

    def test_index_school_all_discovers_data_dirs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            data_root = Path(temp_dir) / "normalized"
            shutil.copytree(MIT_DATA, data_root / "mit")

            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "indexer.cli",
                    "index-school",
                    "--all",
                    "--data-root",
                    str(data_root),
                ],
                check=True,
                capture_output=True,
                text=True,
                cwd=ROOT,
                env=subprocess_env(),
            )

            report = json.loads(completed.stdout)
            self.assertEqual(report["status"], "success")
            self.assertEqual(report["results"][0]["indexes"]["catalog_entries"]["count"], 157)


if __name__ == "__main__":
    unittest.main()
