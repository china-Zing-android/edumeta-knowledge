from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from catalog_parser.adapters import ParserAdapterNotFoundError, parse_school_markdown, registered_adapter_names, registered_university_ids
from catalog_parser.mit_parser import parse_mit_markdown
from catalog_parser.validation import validate_school


ROOT = Path(__file__).resolve().parents[1]
MIT_MD = ROOT / "docs" / "MIT_知识库_完整深度数据_v2.md"


class ParserContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = parse_mit_markdown(MIT_MD)

    def test_mit_catalog_reconciliation(self) -> None:
        self.assertEqual(self.result.summary["catalog_entries"], 157)
        self.assertTrue(self.result.summary["mit_reconciliation_pass"])

    def test_mit_parser_registers_every_markdown_url_once(self) -> None:
        from catalog_parser.markdown_sources import deduplicate_extracted, extract_urls_from_markdown

        expected = set(deduplicate_extracted(extract_urls_from_markdown(MIT_MD.read_text("utf-8"))))
        actual = [row["canonical_url"] for row in self.result.source_registry]
        self.assertTrue(expected.issubset(set(actual)))
        self.assertEqual(len(actual), len(set(actual)))

    def test_source_registry_required_fields(self) -> None:
        with open(ROOT / "docs/schemas/source_registry.schema.json", encoding="utf-8") as f:
            schema = json.load(f)
        required = schema["required"]
        for row in self.result.source_registry:
            missing = [key for key in required if key not in row or row[key] is None]
            self.assertEqual(missing, [], row)

    def test_normalized_jsonl_conforms_to_json_schemas(self) -> None:
        pairs = [
            ("source_registry.jsonl", "source_registry.schema.json"),
            ("catalog_entries.jsonl", "catalog_entries.schema.json"),
            ("url_manifest.jsonl", "url_manifest.schema.json"),
            ("quick_facts.jsonl", "quick_facts.schema.json"),
        ]
        for data_file, schema_file in pairs:
            with self.subTest(data_file=data_file):
                schema = json.loads((ROOT / "docs/schemas" / schema_file).read_text(encoding="utf-8"))
                validator = Draft202012Validator(schema)
                rows = [
                    json.loads(line)
                    for line in (ROOT / "data/normalized/mit" / data_file).read_text(encoding="utf-8").splitlines()
                    if line.strip()
                ]
                for row in rows:
                    errors = sorted(validator.iter_errors(row), key=lambda error: error.path)
                    self.assertEqual([], [error.message for error in errors], row)

    def test_catalog_entries_required_fields(self) -> None:
        with open(ROOT / "docs/schemas/catalog_entries.schema.json", encoding="utf-8") as f:
            schema = json.load(f)
        required = schema["required"]
        for row in self.result.catalog_entries:
            missing = [key for key in required if key not in row or row[key] is None]
            self.assertEqual(missing, [], row)

    def test_every_catalog_entry_has_controlled_discipline_relationships(self) -> None:
        for row in self.result.catalog_entries:
            self.assertTrue(row.get("discipline_ids"), row["entry_id"])
            self.assertEqual(len(row["discipline_ids"]), len(row.get("discipline_labels") or []))

    def test_primary_ids_are_unique(self) -> None:
        for rows, key in [
            (self.result.source_registry, "source_id"),
            (self.result.catalog_entries, "entry_id"),
            (self.result.url_manifest, "url_id"),
            (self.result.quick_facts, "fact_id"),
        ]:
            values = [row[key] for row in rows]
            self.assertEqual(len(values), len(set(values)), key)

    def test_high_risk_facts_are_extracted(self) -> None:
        fact_keys = {row["fact_key"] for row in self.result.quick_facts}
        self.assertIn("undergraduate_early_action_deadline", fact_keys)
        self.assertIn("undergraduate_tuition_2026_2027", fact_keys)
        self.assertIn("undergraduate_need_blind_full_need_international", fact_keys)
        eecs_toefl = [
            row for row in self.result.quick_facts
            if row["fact_key"] == "english_minimums"
            and "electrical_engineering_and_computer_science" in row["fact_id"]
        ]
        self.assertTrue(eecs_toefl)
        self.assertIn("TOEFL 100", eecs_toefl[0]["raw_value"])

    def test_parser_adapter_registry_routes_mit_without_changing_contract(self) -> None:
        self.assertIn("mit", registered_university_ids())

        result = parse_school_markdown("MIT", MIT_MD)

        self.assertEqual(result.summary, self.result.summary)
        self.assertEqual(len(result.catalog_entries), 157)

    def test_unknown_parser_adapter_fails_with_available_adapters(self) -> None:
        with self.assertRaises(ParserAdapterNotFoundError) as ctx:
            parse_school_markdown("stanford", MIT_MD)

        self.assertEqual(ctx.exception.university_id, "stanford")
        self.assertIn("mit", ctx.exception.available)

    def test_generic_structured_adapter_outputs_schema_valid_records(self) -> None:
        self.assertIn("generic_structured", registered_adapter_names())
        sample = """# Example University L1

**University ID**: exampleu
**University name**: Example University
**Data capture date**: 2026-07-09
**Dataset version**: exampleu_20260709_v1

## Catalog Entries

| school | department | level | degree_level | program_name | source_url | degree_full_name | course_code | topics | url_type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| School of Engineering | Computer Science | graduate | SM | Computer Science MS | https://example.edu/cs/ms | Master of Science | CS-MS | catalog,programs,admission_requirements | program_admission |
| School of Engineering | Computer Science | undergraduate | SB | Computer Science BS | https://example.edu/cs/bs | Bachelor of Science | CS-BS | catalog,programs,degree_chart | degree_chart |

## Quick Facts

| fact_type | fact_key | raw_value | source_url | program_name | term | admission_cycle | topics | url_type | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| deadline | application_deadline | December 15, 2026 | https://example.edu/cs/ms/admissions | Computer Science MS | Fall | 2026 | admission_requirements,deadline | deadline | E-EX-001 |
| application_fee | application_fee | $125 | https://example.edu/apply/fees |  |  | 2026 | application_fee | tuition_fee | E-EX-002 |
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            md_path = root / "exampleu.md"
            out_dir = root / "normalized/exampleu"
            out_dir.mkdir(parents=True)
            md_path.write_text(sample, encoding="utf-8")

            result = parse_school_markdown("exampleu", md_path, adapter_name="generic_structured")
            result.write_jsonl(out_dir)
            report = validate_school(out_dir, "exampleu")

        self.assertEqual(result.summary["parser_adapter"], "generic_structured")
        self.assertEqual(result.summary["catalog_entries"], 2)
        self.assertEqual(result.summary["quick_facts"], 2)
        self.assertEqual(report["status"], "passed", report["failures"])
        self.assertEqual(result.catalog_entries[0]["search_text"].startswith("Example University EXAMPLEU"), True)
        self.assertEqual(result.quick_facts[0]["entry_id"], result.catalog_entries[0]["entry_id"])


class MarkdownSourcesTests(unittest.TestCase):
    """Plan Task 3 Step 1: URL extraction, canonicalization, dedup, heading
    context, entry links, and invalid-URL rejection."""

    def test_canonicalize_normalizes_scheme_host_casing_and_drops_fragment(self) -> None:
        from catalog_parser.markdown_sources import canonicalize_url

        self.assertEqual(
            canonicalize_url("HTTPS://Catalog.MIT.EDU/degree-charts/x/#frag"),
            "https://catalog.mit.edu/degree-charts/x",
        )

    def test_canonicalize_drops_tracking_params_keeps_functional(self) -> None:
        from catalog_parser.markdown_sources import canonicalize_url

        out = canonicalize_url("https://example.edu/p?id=42&utm_source=newsletter&gclid=abc&q=deep")
        self.assertIn("id=42", out)
        self.assertIn("q=deep", out)
        self.assertNotIn("utm_source", out)
        self.assertNotIn("gclid", out)

    def test_canonicalize_strips_trailing_slash_for_non_root(self) -> None:
        from catalog_parser.markdown_sources import canonicalize_url

        self.assertEqual(canonicalize_url("https://example.edu/a/b/"), "https://example.edu/a/b")
        self.assertEqual(canonicalize_url("https://example.edu/"), "https://example.edu")

    def test_is_valid_http_url_rejects_non_http_localhost_private_malformed(self) -> None:
        from catalog_parser.markdown_sources import is_valid_http_url

        self.assertTrue(is_valid_http_url("https://example.edu/x"))
        self.assertFalse(is_valid_http_url("ftp://example.edu/x"))
        self.assertFalse(is_valid_http_url("http://localhost:8000/x"))
        self.assertFalse(is_valid_http_url("https://127.0.0.1/x"))
        self.assertFalse(is_valid_http_url("https://192.168.1.5/x"))
        self.assertFalse(is_valid_http_url("https://10.0.0.2/x"))
        self.assertFalse(is_valid_http_url("not a url"))
        self.assertFalse(is_valid_http_url(""))

    def test_source_id_is_deterministic_and_stable_for_netloc_path(self) -> None:
        from catalog_parser.markdown_sources import source_id_for

        # trailing slash and fragment differences must NOT change the id
        self.assertEqual(
            source_id_for("mit", "https://catalog.mit.edu/degree-charts/aero/"),
            source_id_for("mit", "https://catalog.mit.edu/degree-charts/aero"),
        )
        self.assertEqual(
            source_id_for("mit", "https://catalog.mit.edu/x#frag"),
            source_id_for("mit", "https://catalog.mit.edu/x"),
        )

    def test_source_id_matches_legacy_mit_derivation(self) -> None:
        # backward compatibility: existing MIT source_ids were
        # stable_id("src", "mit", netloc, path). source_id_for must reproduce it.
        from catalog_parser.markdown_sources import source_id_for, stable_id
        from urllib.parse import urlparse

        url = "https://catalog.mit.edu/degree-charts/aerospace-engineering-course-16/"
        parsed = urlparse(url)
        legacy = stable_id("src", "mit", parsed.netloc, parsed.path)
        self.assertEqual(source_id_for("mit", url), legacy)

    def test_source_id_distinguishes_functional_query_parameters(self) -> None:
        from catalog_parser.markdown_sources import source_id_for

        self.assertNotEqual(
            source_id_for("mit", "https://example.edu/program?degree=sm"),
            source_id_for("mit", "https://example.edu/program?degree=phd"),
        )

    def test_extract_captures_markdown_links_autolinks_and_bare_urls(self) -> None:
        from catalog_parser.markdown_sources import extract_urls_from_markdown

        text = "\n".join(
            [
                "# Title",
                "See [catalog](https://catalog.mit.edu/x) for details.",
                "Autolink: <https://oge.mit.edu/y>.",
                "Bare: https://sfs.mit.edu/z here.",
            ]
        )
        items = extract_urls_from_markdown(text)
        canonicals = {item.canonical for item in items}
        self.assertIn("https://catalog.mit.edu/x", canonicals)
        self.assertIn("https://oge.mit.edu/y", canonicals)
        self.assertIn("https://sfs.mit.edu/z", canonicals)

    def test_extract_rejects_invalid_urls(self) -> None:
        from catalog_parser.markdown_sources import extract_urls_from_markdown

        text = "\n".join(
            [
                "[bad](ftp://example.edu/x)",
                "<http://localhost:8000/y>",
                "https://192.168.0.1/z bare",
                "[good](https://catalog.mit.edu/ok)",
            ]
        )
        items = extract_urls_from_markdown(text)
        canonicals = {item.canonical for item in items}
        self.assertEqual(canonicals, {"https://catalog.mit.edu/ok"})

    def test_extract_carries_heading_context(self) -> None:
        from catalog_parser.markdown_sources import extract_urls_from_markdown

        text = "\n".join(
            [
                "## SECTION 1 — Undergraduate",
                "#### School of Engineering",
                "##### Aeronautics and Astronautics",
                "Read more at [Aero](https://catalog.mit.edu/aero).",
            ]
        )
        items = extract_urls_from_markdown(text)
        aero = next(i for i in items if i.canonical == "https://catalog.mit.edu/aero")
        self.assertTrue(aero.heading_path)

    def test_deduplicate_merges_repeated_urls(self) -> None:
        from catalog_parser.markdown_sources import deduplicate_extracted, extract_urls_from_markdown

        text = "\n".join(
            [
                "# H1",
                "## Sub A",
                "[x](https://example.edu/x)",
                "## Sub B",
                "again https://example.edu/x here",
            ]
        )
        merged = deduplicate_extracted(extract_urls_from_markdown(text))
        self.assertEqual(len(merged), 1)
        representative = next(iter(merged.values()))
        # merged heading paths from both occurrences
        self.assertIn("Sub A", representative.heading_path)
        self.assertIn("Sub B", representative.heading_path)

    def test_mit_parser_uses_canonicalized_canonical_url(self) -> None:
        # regression: the parsed MIT source_registry canonical_url must be the
        # canonicalized form (no trailing slash, no fragment), and source_id stable.
        rows = [r for r in ParserContractTests.result.source_registry if "catalog.mit.edu" in r["canonical_url"]]
        self.assertTrue(rows)
        for row in rows:
            self.assertFalse(row["canonical_url"].endswith("/"), row)
            self.assertNotIn("#", row["canonical_url"])

    def test_mit_existing_source_ids_remain_stable_when_prose_urls_are_added(self) -> None:
        existing_path = ROOT / "data/normalized/mit/source_registry.jsonl"
        existing = {}
        for line in existing_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                existing[row["source_id"]] = row["canonical_url"]
        reparsed = {row["source_id"]: row["canonical_url"] for row in ParserContractTests.result.source_registry}
        self.assertTrue(set(existing).issubset(set(reparsed)))
        for source_id, canonical_url in existing.items():
            self.assertEqual(reparsed[source_id], canonical_url.rstrip("/"))


if __name__ == "__main__":
    unittest.main()
