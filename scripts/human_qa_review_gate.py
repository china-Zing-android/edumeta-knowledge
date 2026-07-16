from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ALLOWED_FAILURE_CATEGORIES = {
    "data_missing",
    "parser_error",
    "l1_retrieval",
    "weknora_import",
    "evidence_gate",
    "llm_generation",
    "mcp_calling",
    "ux_clarification",
    "external_dependency",
    "qa_case_issue",
}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def base_qa_case_id(value: str) -> str:
    return value.split("::", 1)[0]


def load_cases(paths: list[Path]) -> dict[str, dict[str, Any]]:
    cases: dict[str, dict[str, Any]] = {}
    for path in paths:
        for row in load_jsonl(path):
            cases[row["qa_case_id"]] = row
    return cases


def _score(review: dict[str, Any], key: str) -> int | None:
    if key == "freshness":
        value = review.get("freshness", review.get("freshness_version_correctness"))
    else:
        value = review.get(key)
    if value is None:
        return None
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return None
    return parsed if 0 <= parsed <= 2 else None


def _bool(review: dict[str, Any], key: str) -> bool:
    value = review.get(key)
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y"}
    return bool(value)


def _reviewed_case_ids(reviews: list[dict[str, Any]]) -> set[str]:
    return {base_qa_case_id(str(row.get("qa_case_id") or "")) for row in reviews if row.get("qa_case_id")}


def _rate(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator else 1.0


def validate_review_shape(review: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    required = [
        "review_id",
        "qa_case_id",
        "trace_id",
        "reviewer_id",
        "answer_correctness",
        "evidence_match",
        "clarification_quality",
        "task_completion",
    ]
    for key in required:
        if review.get(key) in (None, ""):
            failures.append(f"missing required review field {key!r}")
    if _score(review, "answer_correctness") is None:
        failures.append("answer_correctness must be an integer 0-2")
    if _score(review, "evidence_match") is None:
        failures.append("evidence_match must be an integer 0-2")
    if _score(review, "freshness") is None:
        failures.append("freshness/freshness_version_correctness must be an integer 0-2")
    if _score(review, "clarification_quality") is None:
        failures.append("clarification_quality must be an integer 0-2")
    if _score(review, "task_completion") is None:
        failures.append("task_completion must be an integer 0-2")
    return failures


def review_has_failure(review: dict[str, Any]) -> bool:
    scores = [
        _score(review, "answer_correctness"),
        _score(review, "evidence_match"),
        _score(review, "freshness"),
        _score(review, "clarification_quality"),
        _score(review, "task_completion"),
    ]
    return any(score is not None and score < 2 for score in scores) or _bool(review, "hallucination_flag") or _bool(review, "unsafe_or_overconfident_flag")


def evaluate_human_reviews(
    *,
    cases: dict[str, dict[str, Any]],
    reviews: list[dict[str, Any]],
    min_reviewed_cases: int,
    min_reviewed_conversations: int,
    evidence_match_threshold: float = 0.95,
    clarification_threshold: float = 0.90,
    task_completion_threshold: float = 0.85,
) -> dict[str, Any]:
    failures: list[str] = []
    if not reviews:
        return {
            "status": "not_ready",
            "failures": ["human review file is missing or empty"],
            "review_count": 0,
            "reviewed_case_count": 0,
            "reviewed_conversation_count": 0,
        }

    reviews_by_case: dict[str, list[dict[str, Any]]] = {}
    shape_errors: list[str] = []
    for review in reviews:
        case_id = base_qa_case_id(str(review.get("qa_case_id") or ""))
        reviews_by_case.setdefault(case_id, []).append(review)
        for error in validate_review_shape(review):
            shape_errors.append(f"{review.get('review_id') or review.get('qa_case_id')}: {error}")
        if case_id not in cases:
            shape_errors.append(f"{review.get('review_id') or review.get('qa_case_id')}: references unknown qa_case_id {case_id!r}")
    failures.extend(shape_errors[:50])
    if len(shape_errors) > 50:
        failures.append(f"review shape errors truncated: {len(shape_errors)} total")

    reviewed_case_ids = _reviewed_case_ids(reviews)
    conversation_case_ids = {
        case_id
        for case_id, case in cases.items()
        if case.get("conversation_context")
    }
    reviewed_conversation_ids = reviewed_case_ids & conversation_case_ids
    if len(reviewed_case_ids) < min_reviewed_cases:
        failures.append(f"reviewed case count below threshold: expected >= {min_reviewed_cases}, got {len(reviewed_case_ids)}")
    if len(reviewed_conversation_ids) < min_reviewed_conversations:
        failures.append(
            f"reviewed conversation count below threshold: expected >= {min_reviewed_conversations}, got {len(reviewed_conversation_ids)}"
        )

    p0_blockers: list[str] = []
    hallucination_blockers: list[str] = []
    missing_failure_categories: list[str] = []
    evidence_match_pass = 0
    clarification_pass = 0
    clarification_total = 0
    task_completion_pass = 0
    valid_metric_reviews = 0

    for review in reviews:
        case_id = base_qa_case_id(str(review.get("qa_case_id") or ""))
        case = cases.get(case_id, {})
        risk_level = case.get("risk_level")
        answer_correctness = _score(review, "answer_correctness")
        evidence_match = _score(review, "evidence_match")
        freshness = _score(review, "freshness")
        clarification_quality = _score(review, "clarification_quality")
        task_completion = _score(review, "task_completion")
        if None not in {answer_correctness, evidence_match, freshness, clarification_quality, task_completion}:
            valid_metric_reviews += 1
            if evidence_match == 2:
                evidence_match_pass += 1
            if task_completion is not None and task_completion >= 1:
                task_completion_pass += 1
            if case.get("expected_route") == "clarification":
                clarification_total += 1
                if clarification_quality == 2:
                    clarification_pass += 1

        if risk_level == "P0":
            if answer_correctness != 2 or evidence_match != 2 or freshness != 2:
                p0_blockers.append(str(review.get("qa_case_id")))
        if risk_level in {"P0", "P1"} and _bool(review, "hallucination_flag"):
            hallucination_blockers.append(str(review.get("qa_case_id")))
        if review_has_failure(review):
            category = review.get("failure_category")
            if category not in ALLOWED_FAILURE_CATEGORIES:
                missing_failure_categories.append(str(review.get("qa_case_id")))

    if p0_blockers:
        failures.append(f"P0 blocking review failures: {', '.join(p0_blockers[:20])}")
    if hallucination_blockers:
        failures.append(f"hallucination_flag present in P0/P1 reviews: {', '.join(hallucination_blockers[:20])}")
    if missing_failure_categories:
        failures.append(f"failed/partial reviews missing valid failure_category: {', '.join(missing_failure_categories[:20])}")

    evidence_match_rate = _rate(evidence_match_pass, valid_metric_reviews)
    clarification_rate = _rate(clarification_pass, clarification_total)
    task_completion_rate = _rate(task_completion_pass, valid_metric_reviews)
    if evidence_match_rate < evidence_match_threshold:
        failures.append(f"evidence_match rate below threshold: expected >= {evidence_match_threshold:.2f}, got {evidence_match_rate:.2f}")
    if clarification_rate < clarification_threshold:
        failures.append(f"clarification quality rate below threshold: expected >= {clarification_threshold:.2f}, got {clarification_rate:.2f}")
    if task_completion_rate < task_completion_threshold:
        failures.append(f"task completion rate below threshold: expected >= {task_completion_threshold:.2f}, got {task_completion_rate:.2f}")

    return {
        "status": "passed" if not failures else "failed",
        "failures": failures,
        "review_count": len(reviews),
        "reviewed_case_count": len(reviewed_case_ids),
        "reviewed_conversation_count": len(reviewed_conversation_ids),
        "metrics": {
            "evidence_match_rate": evidence_match_rate,
            "clarification_quality_rate": clarification_rate,
            "task_completion_rate": task_completion_rate,
            "valid_metric_reviews": valid_metric_reviews,
        },
        "thresholds": {
            "min_reviewed_cases": min_reviewed_cases,
            "min_reviewed_conversations": min_reviewed_conversations,
            "evidence_match_threshold": evidence_match_threshold,
            "clarification_threshold": clarification_threshold,
            "task_completion_threshold": task_completion_threshold,
        },
    }


def build_gate_report(
    *,
    case_paths: list[Path],
    reviews_path: Path,
    min_reviewed_cases: int,
    min_reviewed_conversations: int,
    evidence_match_threshold: float = 0.95,
    clarification_threshold: float = 0.90,
    task_completion_threshold: float = 0.85,
) -> dict[str, Any]:
    cases = load_cases(case_paths)
    if not cases:
        report = {
            "status": "not_ready",
            "failures": ["QA cases are missing or empty"],
            "case_paths": [str(path) for path in case_paths],
            "reviews_path": str(reviews_path),
        }
    else:
        report = evaluate_human_reviews(
            cases=cases,
            reviews=load_jsonl(reviews_path),
            min_reviewed_cases=min_reviewed_cases,
            min_reviewed_conversations=min_reviewed_conversations,
            evidence_match_threshold=evidence_match_threshold,
            clarification_threshold=clarification_threshold,
            task_completion_threshold=task_completion_threshold,
        )
        report.update(
            {
                "case_paths": [str(path) for path in case_paths],
                "reviews_path": str(reviews_path),
                "case_count": len(cases),
            }
        )
    return {
        "generated_at": utc_now_iso(),
        **report,
    }


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate human QA/UAT review scores as a release-blocking gate.")
    parser.add_argument("--cases-path", action="append", required=True, help="QA case JSONL path. Can be repeated.")
    parser.add_argument("--reviews-path", default="qa/human-reviews.jsonl")
    parser.add_argument("--min-reviewed-cases", type=int, default=200)
    parser.add_argument("--min-reviewed-conversations", type=int, default=50)
    parser.add_argument("--evidence-match-threshold", type=float, default=0.95)
    parser.add_argument("--clarification-threshold", type=float, default=0.90)
    parser.add_argument("--task-completion-threshold", type=float, default=0.85)
    parser.add_argument("--output-path", default=None)
    parser.add_argument("--allow-not-ready", action="store_true")
    parser.add_argument("--allow-failed", action="store_true")
    args = parser.parse_args()

    report = build_gate_report(
        case_paths=[Path(path) for path in args.cases_path],
        reviews_path=Path(args.reviews_path),
        min_reviewed_cases=args.min_reviewed_cases,
        min_reviewed_conversations=args.min_reviewed_conversations,
        evidence_match_threshold=args.evidence_match_threshold,
        clarification_threshold=args.clarification_threshold,
        task_completion_threshold=args.task_completion_threshold,
    )
    if args.output_path:
        write_report(Path(args.output_path), report)
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    if report["status"] == "passed":
        return
    if report["status"] == "not_ready" and args.allow_not_ready:
        return
    if args.allow_failed:
        return
    raise SystemExit(1)


if __name__ == "__main__":
    main()
