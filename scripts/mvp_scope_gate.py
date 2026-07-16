from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from collections import Counter


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = ("source_registry.jsonl", "catalog_entries.jsonl", "url_manifest.jsonl", "quick_facts.jsonl")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def normalized_school_ids(data_root: Path) -> list[str]:
    if not data_root.exists():
        return []
    return sorted(
        path.name
        for path in data_root.iterdir()
        if path.is_dir() and all((path / file_name).exists() for file_name in REQUIRED_FILES)
    )


def school_data_counts(data_root: Path, school_ids: list[str]) -> dict[str, dict[str, int]]:
    counts: dict[str, dict[str, int]] = {}
    for school_id in school_ids:
        school_dir = data_root / school_id
        counts[school_id] = {}
        for file_name in REQUIRED_FILES:
            key = file_name.removesuffix(".jsonl")
            counts[school_id][key] = len(load_jsonl(school_dir / file_name))
    return counts


def infer_university_id(case: dict[str, Any], known_school_ids: set[str]) -> str | None:
    explicit = case.get("university_id")
    if isinstance(explicit, str) and explicit:
        return explicit.lower()
    case_id = str(case.get("qa_case_id") or case.get("case_id") or "").lower()
    case_id_parts = [part for part in case_id.split("_") if part]
    if len(case_id_parts) >= 2 and case_id_parts[0] == "mvp" and case_id_parts[1] in known_school_ids:
        return case_id_parts[1]
    if case_id_parts and case_id_parts[0] in known_school_ids:
        return case_id_parts[0]
    text = " ".join(
        str(case.get(field, ""))
        for field in ("question", "expected_behavior", "required_source_url")
    ).lower()
    for school_id in sorted(known_school_ids):
        if school_id in text:
            return school_id
    return None


def qa_coverage(path: Path, known_school_ids: set[str]) -> dict[str, Any]:
    cases = load_jsonl(path) if path.exists() else []
    university_ids = sorted({value for case in cases if (value := infer_university_id(case, known_school_ids))})
    route_counts = Counter(str(case.get("expected_route") or "unknown") for case in cases)
    by_school: dict[str, Counter[str]] = {school_id: Counter() for school_id in known_school_ids}
    for case in cases:
        school_id = infer_university_id(case, known_school_ids)
        if school_id:
            by_school.setdefault(school_id, Counter())[str(case.get("expected_route") or "unknown")] += 1
    return {
        "path": str(path),
        "case_count": len(cases),
        "university_ids": university_ids,
        "university_count": len(university_ids),
        "route_counts": dict(sorted(route_counts.items())),
        "route_counts_by_school": {school_id: dict(counter) for school_id, counter in sorted(by_school.items()) if sum(counter.values()) > 0},
    }


def tool_case_coverage(path: Path) -> dict[str, Any]:
    cases = load_jsonl(path) if path.exists() else []
    return {
        "path": str(path),
        "case_count": len(cases),
        "case_ids": [str(case.get("case_id") or case.get("qa_case_id") or "") for case in cases],
    }


def batch_report_coverage(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "status": "missing", "total": 0, "succeeded": 0, "failed": 0}
    payload = load_json(path)
    return {
        "path": str(path),
        "status": payload.get("status"),
        "total": payload.get("total", 0),
        "succeeded": payload.get("succeeded", 0),
        "failed": payload.get("failed", 0),
    }


def evaluate_mvp_scope(
    *,
    data_root: Path,
    uat_cases_path: Path,
    conversation_cases_path: Path,
    reports_root: Path,
    tool_cases_path: Path | None = None,
    min_schools: int = 5,
    min_uat_cases: int = 200,
    min_conversations: int = 50,
    min_catalog_cases: int = 60,
    min_fact_cases: int = 60,
    min_deep_cases: int = 50,
    min_clarification_cases: int = 20,
    min_mcp_tool_cases: int = 10,
) -> dict[str, Any]:
    school_ids = normalized_school_ids(data_root)
    known_school_ids = set(school_ids) | {"mit"}
    data_counts = school_data_counts(data_root, school_ids)
    uat = qa_coverage(uat_cases_path, known_school_ids)
    conversations = qa_coverage(conversation_cases_path, known_school_ids)
    tool_cases = tool_case_coverage(tool_cases_path) if tool_cases_path else {"path": None, "case_count": 0, "case_ids": []}
    batch_reports = {
        "validation": batch_report_coverage(reports_root / "all-validation-gate-2026-07-09.json"),
        "diff": batch_report_coverage(reports_root / "all-diff-gate-2026-07-09.json"),
        "index": batch_report_coverage(reports_root / "all-index-gate-2026-07-09.json"),
        "weknora_sync": batch_report_coverage(reports_root / "all-weknora-sync-gate-2026-07-09.json"),
    }
    failures: list[str] = []
    if len(school_ids) < min_schools:
        failures.append(f"normalized school count below threshold: expected >= {min_schools}, got {len(school_ids)}")
    for school_id, counts in data_counts.items():
        for entity_name, count in counts.items():
            if count <= 0:
                failures.append(f"{school_id} {entity_name} has no records")
    for name, report in batch_reports.items():
        if report["status"] != "success":
            failures.append(f"batch {name} status is {report['status']!r}")
        if int(report.get("succeeded") or 0) < min_schools:
            failures.append(f"batch {name} succeeded below threshold: expected >= {min_schools}, got {report.get('succeeded')}")
    if uat["case_count"] < min_uat_cases:
        failures.append(f"UAT case count below threshold: expected >= {min_uat_cases}, got {uat['case_count']}")
    if uat["university_count"] < min_schools:
        failures.append(f"UAT university coverage below threshold: expected >= {min_schools}, got {uat['university_count']}")
    route_thresholds = {
        "catalog": min_catalog_cases,
        "fact": min_fact_cases,
        "deep": min_deep_cases,
        "clarification": min_clarification_cases,
    }
    for route, threshold in route_thresholds.items():
        actual = int(uat["route_counts"].get(route, 0))
        if actual < threshold:
            failures.append(f"UAT {route} case count below threshold: expected >= {threshold}, got {actual}")
    if conversations["case_count"] < min_conversations:
        failures.append(f"conversation count below threshold: expected >= {min_conversations}, got {conversations['case_count']}")
    if conversations["university_count"] < min_schools:
        failures.append(
            f"conversation university coverage below threshold: expected >= {min_schools}, got {conversations['university_count']}"
        )
    conversation_routes = conversations["route_counts"]
    for route in ("catalog", "fact", "deep", "clarification"):
        if int(conversation_routes.get(route, 0)) <= 0:
            failures.append(f"conversation suite has no {route} cases")
    if int(tool_cases.get("case_count") or 0) < min_mcp_tool_cases:
        failures.append(f"MCP/tool calling case count below threshold: expected >= {min_mcp_tool_cases}, got {tool_cases.get('case_count')}")
    return {
        "status": "passed" if not failures else "failed",
        "generated_at": utc_now_iso(),
        "failures": failures,
        "thresholds": {
            "min_schools": min_schools,
            "min_uat_cases": min_uat_cases,
            "min_conversations": min_conversations,
            "min_catalog_cases": min_catalog_cases,
            "min_fact_cases": min_fact_cases,
            "min_deep_cases": min_deep_cases,
            "min_clarification_cases": min_clarification_cases,
            "min_mcp_tool_cases": min_mcp_tool_cases,
        },
        "normalized_schools": {
            "data_root": str(data_root),
            "school_ids": school_ids,
            "count": len(school_ids),
            "data_counts": data_counts,
        },
        "uat_cases": uat,
        "conversation_cases": conversations,
        "tool_cases": tool_cases,
        "batch_reports": batch_reports,
    }


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify MVP scope coverage: 5 schools, 200 UAT cases, and 50 conversations.")
    parser.add_argument("--data-root", default=str(ROOT / "data/normalized"))
    parser.add_argument("--uat-cases-path", default=str(ROOT / "qa/mvp-uat-cases.jsonl"))
    parser.add_argument("--conversation-cases-path", default=str(ROOT / "qa/mvp-uat-conversations.jsonl"))
    parser.add_argument("--tool-cases-path", default=str(ROOT / "qa/tool-consistency-cases.jsonl"))
    parser.add_argument("--reports-root", default=str(ROOT / "qa/reports"))
    parser.add_argument("--min-schools", type=int, default=5)
    parser.add_argument("--min-uat-cases", type=int, default=200)
    parser.add_argument("--min-conversations", type=int, default=50)
    parser.add_argument("--min-catalog-cases", type=int, default=60)
    parser.add_argument("--min-fact-cases", type=int, default=60)
    parser.add_argument("--min-deep-cases", type=int, default=50)
    parser.add_argument("--min-clarification-cases", type=int, default=20)
    parser.add_argument("--min-mcp-tool-cases", type=int, default=10)
    parser.add_argument("--output-path", default=None)
    parser.add_argument("--allow-failed", action="store_true")
    args = parser.parse_args()

    report = evaluate_mvp_scope(
        data_root=Path(args.data_root),
        uat_cases_path=Path(args.uat_cases_path),
        conversation_cases_path=Path(args.conversation_cases_path),
        tool_cases_path=Path(args.tool_cases_path),
        reports_root=Path(args.reports_root),
        min_schools=args.min_schools,
        min_uat_cases=args.min_uat_cases,
        min_conversations=args.min_conversations,
        min_catalog_cases=args.min_catalog_cases,
        min_fact_cases=args.min_fact_cases,
        min_deep_cases=args.min_deep_cases,
        min_clarification_cases=args.min_clarification_cases,
        min_mcp_tool_cases=args.min_mcp_tool_cases,
    )
    if args.output_path:
        write_report(Path(args.output_path), report)
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    if report["status"] != "passed" and not args.allow_failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
