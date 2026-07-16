from __future__ import annotations

import argparse
import json
import statistics
import time
from pathlib import Path
from typing import Any

import httpx


def read_cases(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text("utf-8").splitlines() if line.strip()]


def contains(value: Any, expected: str) -> bool:
    return expected.lower() in str(value or "").lower()


def row_matches(row: dict[str, Any], expected_fields: dict[str, Any]) -> bool:
    for key, expected in expected_fields.items():
        if key.endswith("_contains"):
            if not contains(row.get(key.removesuffix("_contains")), expected):
                return False
        elif row.get(key) != expected:
            return False
    return True


def validate_case(case: dict[str, Any], response: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if response.get("mode") != case["expected_mode"]:
        failures.append(f"mode={response.get('mode')} expected={case['expected_mode']}")
    expected_match = case.get("match_any")
    if expected_match:
        matched = False
        for row in response.get("matches", []):
            matched = matched or row_matches(row, expected_match)
        if not matched:
            failures.append(f"no match satisfies {expected_match}")
    expected_program = case.get("matched_program_any")
    if expected_program:
        matched_program = False
        for group in response.get("matches", []):
            for row in group.get("matched_programs") or []:
                matched_program = matched_program or row_matches(row, expected_program)
        if not matched_program:
            failures.append(f"no grouped program satisfies {expected_program}")
    if case.get("missing_slot") not in (response.get("missing_slots") or []):
        if case.get("missing_slot"):
            failures.append(f"missing slot {case['missing_slot']}")
    if case.get("evidence_source_contains"):
        if not any(contains(item.get("source_url"), case["evidence_source_contains"]) and item.get("chunk_text") for item in response.get("evidence", [])):
            failures.append("required scoped evidence missing")
    returned_university_ids = {row.get("university_id") for row in response.get("matches", []) if row.get("university_id")}
    missing_universities = sorted(set(case.get("required_university_ids") or []) - returned_university_ids)
    if missing_universities:
        failures.append(f"missing universities: {missing_universities}")
    forbidden_universities = sorted(set(case.get("forbidden_university_ids") or []) & returned_university_ids)
    if forbidden_universities:
        failures.append(f"forbidden universities returned: {forbidden_universities}")
    expected_stage = case.get("expected_stage")
    if expected_stage and response.get("scope", {}).get("stage") != expected_stage:
        failures.append(f"stage={response.get('scope', {}).get('stage')} expected={expected_stage}")
    context = response.get("context") if isinstance(response.get("context"), dict) else {}
    expected_primary = case.get("context_primary_any")
    if expected_primary and not any(row_matches(row, expected_primary) for row in context.get("primary_entities") or []):
        failures.append(f"no context primary satisfies {expected_primary}")
    related_labels = {str(row.get("display_label")) for row in context.get("related_entities") or []}
    for label in case.get("context_related_labels") or []:
        if label not in related_labels:
            failures.append(f"missing related context: {label}")
    if case.get("require_context_provenance"):
        provenance = context.get("provenance") or {}
        if provenance.get("origin") != "md_projection" or not provenance.get("dataset_version"):
            failures.append("context provenance missing")
    if case.get("require_weknora_ms_zero") and response.get("timings", {}).get("weknora_ms") != 0:
        failures.append("weknora_ms must be zero")
    if case.get("forbid_related_primary_overlap"):
        primary_ids = {row.get("entity_id") for row in context.get("primary_entities") or []}
        related_ids = {row.get("entity_id") for row in context.get("related_entities") or []}
        if (primary_ids - {None}) & (related_ids - {None}):
            failures.append("related context overlaps primary entities")
    return failures


def request_payload(case: dict[str, Any]) -> dict[str, Any]:
    return {
        "query": case["query"],
        "university_id": case.get("university_id"),
        "direction": case.get("direction", "auto"),
        "filters": case.get("filters", {}),
        "context": case.get("context", {}),
        "max_results": case.get("max_results", 5),
    }


def percentile(values: list[float], p: float) -> float:
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, int(round((len(ordered) - 1) * p))))
    return ordered[index]


def stable_signature(payload: dict[str, Any]) -> str:
    return json.dumps({
        "mode": payload.get("mode"),
        "matches": [
            {
                **{key: row.get(key) for key in ("entry_id", "fact_id", "source_id", "course_code", "raw_value", "review_status", "conflict_status", "university_id")},
                "matched_programs": [
                    {key: program.get(key) for key in ("entry_id", "program_name", "degree_level", "source_id")}
                    for program in row.get("matched_programs") or []
                ],
            }
            for row in payload.get("matches", [])
        ],
        "context": {
            "primary_entities": [
                {key: row.get(key) for key in ("entity_type", "entity_id", "entry_id", "display_label")}
                for row in (payload.get("context") or {}).get("primary_entities") or []
            ],
            "related_entities": [
                {key: row.get(key) for key in ("entity_id", "display_label", "relation_type", "primary_entity_id")}
                for row in (payload.get("context") or {}).get("related_entities") or []
            ],
            "available_topics": [
                {key: row.get(key) for key in ("topic", "availability")}
                for row in (payload.get("context") or {}).get("available_topics") or []
            ],
            "provenance": (payload.get("context") or {}).get("provenance"),
        },
        "evidence": [
            {"source_id": row[0], "knowledge_id": row[1], "document_id": row[2]}
            for row in sorted(
                {(
                    item.get("source_id"), item.get("knowledge_id"), item.get("document_id"),
                ) for item in payload.get("evidence", [])}
            )
        ],
        "missing_slots": payload.get("missing_slots"),
        "warnings": payload.get("warnings"),
        "stage": (payload.get("scope") or {}).get("stage"),
    }, sort_keys=True, ensure_ascii=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    parser.add_argument("--cases", type=Path, default=Path("qa/retrieval-acceptance-cases.jsonl"))
    parser.add_argument("--runs", type=int, default=5)
    parser.add_argument("--allow-l2-pending", action="store_true")
    parser.add_argument("--output-path", type=Path)
    args = parser.parse_args()
    cases = read_cases(args.cases)
    failures: list[dict[str, Any]] = []
    timings: dict[str, list[float]] = {"l1": [], "l1_l2": [], "upward": [], "range": []}
    signatures: dict[str, set[str]] = {case["case_id"]: set() for case in cases}
    with httpx.Client(timeout=5) as client:
        for case in cases:
            client.post(f"{args.base_url.rstrip('/')}/v1/retrieve", json=request_payload(case)).raise_for_status()
        for run in range(args.runs):
            for case in cases:
                started = time.perf_counter()
                response = client.post(f"{args.base_url.rstrip('/')}/v1/retrieve", json=request_payload(case))
                elapsed = (time.perf_counter() - started) * 1000
                response.raise_for_status()
                payload = response.json()
                signatures[case["case_id"]].add(stable_signature(payload))
                if case["expected_mode"] in timings:
                    timings[case["expected_mode"]].append(elapsed)
                case_failures = validate_case(case, payload)
                if args.allow_l2_pending and case["expected_mode"] == "l1_l2" and payload.get("mode") in {"l1_l2", "not_found"}:
                    case_failures = [failure for failure in case_failures if failure != "required scoped evidence missing"]
                if case_failures:
                    failures.append({"run": run + 1, "case_id": case["case_id"], "failures": case_failures})
    nondeterministic = [case_id for case_id, values in signatures.items() if len(values) != 1]
    report = {
        "status": "passed" if not failures and not nondeterministic else "failed",
        "cases": len(cases), "runs": args.runs, "failures": failures,
        "nondeterministic_cases": nondeterministic,
        "http_l1_p50_ms": round(statistics.median(timings["l1"]), 3) if timings["l1"] else None,
        "http_l1_p95_ms": round(percentile(timings["l1"], 0.95), 3) if timings["l1"] else None,
        "http_l1_l2_p95_ms": round(percentile(timings["l1_l2"], 0.95), 3) if timings["l1_l2"] else None,
        "http_upward_p95_ms": round(percentile(timings["upward"], 0.95), 3) if timings["upward"] else None,
        "http_range_p95_ms": round(percentile(timings["range"], 0.95), 3) if timings["range"] else None,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.output_path:
        args.output_path.parent.mkdir(parents=True, exist_ok=True)
        args.output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", "utf-8")
    raise SystemExit(0 if report["status"] == "passed" else 1)


if __name__ == "__main__":
    main()
