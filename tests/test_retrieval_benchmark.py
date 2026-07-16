from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from retrieval_benchmark import request_payload, validate_case  # noqa: E402


class RetrievalBenchmarkTests(unittest.TestCase):
    def test_cross_university_case_builds_direction_and_filters(self) -> None:
        case = {
            "query": "医学专业的院校有哪些？",
            "direction": "upward",
            "filters": {"country_codes": ["US"]},
        }

        payload = request_payload(case)

        self.assertEqual(payload["direction"], "upward")
        self.assertEqual(payload["filters"], {"country_codes": ["US"]})

    def test_multi_turn_case_forwards_resolved_entry_context(self) -> None:
        case = {
            "query": "那课程设置呢？",
            "university_id": "mit",
            "context": {"entry_id": "ent_economics", "level": "undergraduate"},
        }

        payload = request_payload(case)

        self.assertEqual(payload["context"], case["context"])

    def test_nested_program_expectation_is_field_aware(self) -> None:
        case = {
            "expected_mode": "upward",
            "match_any": {"university_id": "mit"},
            "matched_program_any": {"program_name_contains": "Health Sciences"},
        }
        response = {
            "mode": "upward",
            "matches": [{"university_id": "mit", "matched_programs": [{"program_name": "Health Sciences and Technology"}]}],
        }

        self.assertEqual(validate_case(case, response), [])

    def test_cross_university_case_can_require_and_forbid_universities(self) -> None:
        case = {
            "expected_mode": "upward",
            "required_university_ids": ["mit", "stanford"],
            "forbidden_university_ids": ["harvard"],
        }
        response = {
            "mode": "upward",
            "matches": [{"university_id": "mit"}, {"university_id": "stanford"}],
        }

        self.assertEqual(validate_case(case, response), [])
        self.assertIn(
            "missing universities: ['stanford']",
            validate_case(case, {"mode": "upward", "matches": [{"university_id": "mit"}]}),
        )
        self.assertIn(
            "forbidden universities returned: ['harvard']",
            validate_case(case, {"mode": "upward", "matches": [{"university_id": "mit"}, {"university_id": "stanford"}, {"university_id": "harvard"}]}),
        )

    def test_discovery_case_validates_context_and_no_weknora(self) -> None:
        case = {
            "expected_mode": "l1",
            "expected_stage": "discovery",
            "context_primary_any": {"display_label": "14-1 Economics"},
            "context_related_labels": ["14-2 Mathematical Economics"],
            "require_context_provenance": True,
            "require_weknora_ms_zero": True,
            "forbid_related_primary_overlap": True,
        }
        response = {
            "mode": "l1",
            "scope": {"stage": "discovery"},
            "context": {
                "primary_entities": [{"entity_id": "ent_14_1", "display_label": "14-1 Economics"}],
                "related_entities": [{"entity_id": "ent_14_2", "display_label": "14-2 Mathematical Economics"}],
                "provenance": {"origin": "md_projection", "dataset_version": "mit_v2"},
            },
            "timings": {"weknora_ms": 0},
            "matches": [],
        }

        self.assertEqual(validate_case(case, response), [])

        response["timings"]["weknora_ms"] = 4
        self.assertIn("weknora_ms must be zero", validate_case(case, response))


if __name__ == "__main__":
    unittest.main()
