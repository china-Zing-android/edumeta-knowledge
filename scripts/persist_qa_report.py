from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def score_from_result(result: dict[str, Any]) -> dict[str, Any]:
    passed = bool(result.get("passed"))
    score = 2 if passed else 0
    failures = " | ".join(result.get("failures", []))
    return {
        "answer_correctness": score,
        "evidence_match": score,
        "freshness": score,
        "clarification_quality": score,
        "task_completion": score,
        "hallucination_flag": not passed and "must_not_include" in failures,
        "unsafe_or_overconfident_flag": not passed and ("missing_evidence" in failures or "无证据" in failures),
        "reviewer_notes": "automated QA pass" if passed else f"automated QA failures: {failures}",
    }


def base_qa_case_id(qa_case_id: str) -> str:
    return qa_case_id.split("::", 1)[0]


def review_id_for_result(run_id: str, result: dict[str, Any]) -> str:
    qa_case_id = str(result["qa_case_id"]).replace("::", "__")
    return f"auto_{run_id}_{qa_case_id}"


def persist_qa_report(cases_path: Path, report_path: Path, run_id: str) -> dict[str, Any]:
    """Persist QA cases and automated QA reviews as a JSONL report.

    Plan §3 removes the PostgreSQL ``qa_cases`` / ``qa_reviews`` tables. QA result
    persistence now writes a self-contained JSONL report (consumed by Task 11's
    field-aware evaluation) instead of a control-plane table.
    """
    cases = {case["qa_case_id"]: case for case in load_jsonl(cases_path)}
    report = json.loads(report_path.read_text(encoding="utf-8"))
    results = report.get("results", [])
    reviews: list[dict[str, Any]] = []

    for result in results:
        qa_case_id = base_qa_case_id(result["qa_case_id"])
        if qa_case_id not in cases:
            raise ValueError(f"QA result references missing case: {result['qa_case_id']}")
        scores = score_from_result(result)
        review_id = review_id_for_result(run_id, result)
        reviews.append(
            {
                "review_id": review_id,
                "qa_case_id": qa_case_id,
                "trace_id": result.get("trace_id"),
                **scores,
            }
        )

    return {
        "status": "persisted",
        "run_id": run_id,
        "cases": len(cases),
        "reviews": len(reviews),
        "reviews_payload": reviews,
        "report_path": str(report_path),
    }


def write_persistence_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        **{k: v for k, v in report.items() if k != "reviews_payload"},
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_reviews_jsonl(path: Path, reviews: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(review, ensure_ascii=False, sort_keys=True) + "\n" for review in reviews),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Persist QA reviews as a JSONL report (no control-plane table).")
    parser.add_argument("--cases-path", default="qa/mit-gold-cases.jsonl")
    parser.add_argument("--report-path", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--output-path", default=None)
    args = parser.parse_args()

    report = persist_qa_report(
        Path(args.cases_path),
        Path(args.report_path),
        args.run_id,
    )
    print(json.dumps({k: v for k, v in report.items() if k != "reviews_payload"}, ensure_ascii=False, indent=2, sort_keys=True))
    if args.output_path:
        write_persistence_report(Path(args.output_path), report)
        write_reviews_jsonl(Path(args.output_path).with_suffix(".reviews.jsonl"), report.get("reviews_payload", []))


if __name__ == "__main__":
    main()
