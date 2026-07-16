from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_mvp_uat_suite import build_conversation_cases, build_single_turn_cases, write_jsonl  # noqa: E402
from catalog_parser.structured_markdown_parser import parse_structured_markdown  # noqa: E402
from fast_router.knowledge import KnowledgeStore  # noqa: E402
from mvp_scope_gate import evaluate_mvp_scope  # noqa: E402


def _read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def write_structured_school(root: Path, university_id: str) -> None:
    name = f"Example University {university_id.upper()}"
    md_path = root / f"{university_id}.md"
    md_path.write_text(
        f"""# {name} L1

**University ID**: {university_id}
**University name**: {name}
**Data capture date**: 2026-07-09
**Dataset version**: {university_id}_20260709_v1

## Catalog Entries

| school | department | level | degree_level | program_name | source_url | topics | url_type |
| --- | --- | --- | --- | --- | --- | --- | --- |
| School of Engineering | Computer Science | graduate | SM | Computer Science MS | https://{university_id}.example.edu/cs/ms | catalog,programs,admission_requirements | program_admission |

## Quick Facts

| fact_type | fact_key | raw_value | source_url | program_name | term | admission_cycle | topics | url_type | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| english_requirement | english_minimums | TOEFL 100 | https://{university_id}.example.edu/cs/ms/admissions | Computer Science MS | Fall | 2026 | admission_requirements,english_requirement | program_admission | E-{university_id}-001 |
| application_fee | application_fee | $125 | https://{university_id}.example.edu/cs/ms/admissions | Computer Science MS | Fall | 2026 | application_fee | program_admission | E-{university_id}-002 |
""",
        encoding="utf-8",
    )
    out_dir = root / "normalized" / university_id
    out_dir.mkdir(parents=True)
    parse_structured_markdown(university_id, md_path).write_jsonl(out_dir)
    manifest = _read_jsonl(out_dir / "url_manifest.jsonl")
    for row in manifest:
        row["import_status"] = "success"
        row["weknora_document_id"] = f"doc_{row['source_id']}"
        row["weknora_chunk_ids"] = [f"chunk_{row['source_id']}"]
    _write_jsonl(out_dir / "url_manifest.jsonl", manifest)
    sources = _read_jsonl(out_dir / "source_registry.jsonl")
    for row in sources:
        row["weknora_import_status"] = "success"
        row["crawl_status"] = "success"
    _write_jsonl(out_dir / "source_registry.jsonl", sources)


class MvpUatBuilderTests(unittest.TestCase):
    def test_build_multi_school_uat_cases_with_scope_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for university_id in ["alpha", "bravo", "charlie", "delta", "echo"]:
                write_structured_school(root, university_id)

            data_root = root / "normalized"
            single = build_single_turn_cases(
                data_root,
                min_schools=5,
                catalog_target=5,
                fact_target=10,
                deep_target=5,
                clarification_target=5,
            )
            conversations = build_conversation_cases(data_root, min_schools=5, target=25)
            single_path = root / "qa/mvp-uat-cases.jsonl"
            conversation_path = root / "qa/mvp-uat-conversations.jsonl"
            write_jsonl(single_path, single)
            write_jsonl(conversation_path, conversations)
            tool_path = root / "qa/tool-consistency-cases.jsonl"
            write_jsonl(tool_path, [{"case_id": f"tool_{index:03d}", "query": "tool smoke"} for index in range(10)])

            reports = root / "reports"
            reports.mkdir()
            for name in ("all-validation-gate", "all-diff-gate", "all-index-gate", "all-weknora-sync-gate"):
                (reports / f"{name}-2026-07-09.json").write_text(
                    json.dumps({"status": "success", "total": 5, "succeeded": 5, "failed": 0}),
                    encoding="utf-8",
                )

            scope = evaluate_mvp_scope(
                data_root=data_root,
                uat_cases_path=single_path,
                conversation_cases_path=conversation_path,
                tool_cases_path=tool_path,
                reports_root=reports,
                min_schools=5,
                min_uat_cases=25,
                min_conversations=25,
                min_catalog_cases=5,
                min_fact_cases=10,
                min_deep_cases=5,
                min_clarification_cases=5,
                min_mcp_tool_cases=10,
            )

            self.assertEqual(len(single), 25)
            self.assertEqual(len(conversations), 25)
            self.assertEqual(scope["status"], "passed", scope["failures"])
            self.assertEqual(scope["uat_cases"]["university_count"], 5)
            self.assertEqual(scope["conversation_cases"]["university_count"], 5)
            self.assertTrue(all(case["case_source"] == "generated_from_normalized_data" for case in single))
            self.assertTrue(all(case["human_review_required"] is True for case in conversations))

    def test_knowledge_store_resolves_generic_school_alias_from_catalog_search_text(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_structured_school(root, "alpha")

            store = KnowledgeStore(root / "normalized")
            result = store.resolve_university("Example University ALPHA Computer Science MS deadline")

            self.assertEqual(result["university_id"], "alpha")
            self.assertEqual(result["confidence"], 1.0)


if __name__ == "__main__":
    unittest.main()
