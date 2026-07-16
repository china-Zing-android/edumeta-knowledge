from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def utc_date() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def gate_rows(release: dict[str, Any]) -> list[dict[str, Any]]:
    return list(release.get("results") or [])


def failures_by_gate(release: dict[str, Any]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = defaultdict(list)
    for item in release.get("failures", []):
        text = str(item)
        if ":" in text:
            gate, detail = text.split(":", 1)
            grouped[gate.strip()].append(detail.strip())
        else:
            grouped["unknown"].append(text)
    return dict(grouped)


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(cell).replace("\n", " ") for cell in row) + " |")
    return "\n".join(lines)


def qa_summary_rows(reports: dict[str, dict[str, Any]]) -> list[list[Any]]:
    rows: list[list[Any]] = []
    for name, report in reports.items():
        if not report:
            rows.append([name, "missing", "-", "-", "-"])
            continue
        rows.append(
            [
                name,
                report.get("status", "report"),
                report.get("total", "-"),
                report.get("passed", "-"),
                report.get("failed", "-"),
            ]
        )
    return rows


def review_failure_categories(reviews: list[dict[str, Any]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for review in reviews:
        scores = [
            review.get("answer_correctness"),
            review.get("evidence_match"),
            review.get("freshness", review.get("freshness_version_correctness")),
            review.get("clarification_quality"),
            review.get("task_completion"),
        ]
        flags = [review.get("hallucination_flag"), review.get("unsafe_or_overconfident_flag")]
        has_failure = any(isinstance(score, int) and score < 2 for score in scores) or any(bool(flag) for flag in flags)
        if has_failure:
            counts[str(review.get("failure_category") or "missing_failure_category")] += 1
    return counts


def build_scope_lines(*, profile: str, scope: dict[str, Any]) -> list[str]:
    if profile == "mit":
        mit = (scope.get("schools") or {}).get("mit", {})
        counts = mit.get("expected_counts", {})
        return [
            "Acceptance profile: MIT only",
            "Normalized scope: `mit`",
            f"MIT live data status: `{scope.get('status', 'missing')}`",
            f"MIT catalog entries: {counts.get('catalog_entries', '-')}",
            f"MIT URL manifest rows: {counts.get('url_manifest', '-')}",
            f"MIT quick facts: {counts.get('quick_facts', '-')}",
        ]
    return [
        f"Normalized schools: {scope.get('normalized_schools', {}).get('count', '-')}",
        f"UAT school coverage: {scope.get('uat_cases', {}).get('university_count', '-')}",
        f"Conversation school coverage: {scope.get('conversation_cases', {}).get('university_count', '-')}",
    ]


def build_acceptance_report(
    *,
    release: dict[str, Any],
    scope: dict[str, Any],
    human_review: dict[str, Any],
    generated_at: str,
    profile: str = "full",
) -> str:
    release_status = release.get("status", "missing")
    decision = {
        "passed": "RELEASE READY",
        "passed_with_deferred_manual_qa": "FUNCTIONAL READY; MANUAL QA DEFERRED",
    }.get(release_status, "NOT RELEASE READY")
    rows = [
        [
            row.get("name"),
            row.get("status"),
            "yes" if row.get("passed") else "no",
            "; ".join(str(item) for item in row.get("failures", [])[:3]),
        ]
        for row in gate_rows(release)
    ]
    sections = [
        "# MIT Acceptance Report" if profile == "mit" else "# MVP Acceptance Report",
        "",
        f"Generated at: {generated_at}",
        "",
        f"Decision: **{decision}**",
        "",
        f"Release status: `{release_status}`",
        f"Gate summary: {release.get('passed', 0)} passed / {release.get('failed', 0)} failed / {release.get('total', 0)} total",
        *( [f"Deferred gates: {', '.join(release.get('deferred_gates', []))}"] if release.get("deferred_gates") else [] ),
        "",
        "## Gate Results",
        "",
        markdown_table(["Gate", "Status", "Passed", "Failure sample"], rows) if rows else "No release gate report found.",
        "",
        "## Scope",
        "",
        *build_scope_lines(profile=profile, scope=scope),
        "",
        "## Human Review",
        "",
        f"Status: `{human_review.get('status', 'missing')}`",
        f"Reviewed base cases: {human_review.get('reviewed_case_count', 0)}",
        f"Reviewed conversations: {human_review.get('reviewed_conversation_count', 0)}",
    ]
    return "\n".join(sections).rstrip() + "\n"


def build_qa_report(*, qa_reports: dict[str, dict[str, Any]], human_review: dict[str, Any], generated_at: str) -> str:
    metrics = human_review.get("metrics", {}) if human_review else {}
    sections = [
        "# QA/UAT Report",
        "",
        f"Generated at: {generated_at}",
        "",
        "## Automated QA",
        "",
        markdown_table(["Suite", "Status", "Total", "Passed", "Failed"], qa_summary_rows(qa_reports)),
        "",
        "## Human Review Gate",
        "",
        f"Status: `{human_review.get('status', 'missing')}`",
        f"Reviewed cases: {human_review.get('reviewed_case_count', 0)}",
        f"Reviewed conversations: {human_review.get('reviewed_conversation_count', 0)}",
        f"Evidence match rate: {metrics.get('evidence_match_rate', '-')}",
        f"Clarification quality rate: {metrics.get('clarification_quality_rate', '-')}",
        f"Task completion rate: {metrics.get('task_completion_rate', '-')}",
        "",
        "Automated QA does not replace human UAT review.",
    ]
    return "\n".join(sections).rstrip() + "\n"


def build_failure_analysis(
    *,
    release: dict[str, Any],
    human_review: dict[str, Any],
    human_reviews: list[dict[str, Any]],
    generated_at: str,
    profile: str = "full",
) -> str:
    grouped = failures_by_gate(release)
    category_counts = review_failure_categories(human_reviews)
    lines = [
        "# Failure Analysis",
        "",
        f"Generated at: {generated_at}",
        "",
        "## Release Blockers",
        "",
    ]
    if grouped:
        for gate, failures in grouped.items():
            lines.extend([f"### {gate}", ""])
            for failure in failures:
                lines.append(f"- {failure}")
            lines.append("")
    else:
        lines.append("No release blockers in the release gate report.")
        lines.append("")

    lines.extend(["## Human Review Failures", ""])
    if human_review.get("status") == "not_ready":
        for failure in human_review.get("failures", []):
            lines.append(f"- {failure}")
    elif category_counts:
        for category, count in sorted(category_counts.items()):
            lines.append(f"- {category}: {count}")
    else:
        lines.append("No human review failure categories recorded.")
    lines.append("")

    lines.extend(["## Required Next Evidence", ""])
    if profile == "mit":
        lines.append("- MIT-only human QA/UAT review report with passing review coverage and failure attribution.")
    else:
        lines.append("- At least five normalized schools and successful batch validation/diff/index/WeKnora sync reports.")
    lines.extend(
        [
            "- Live WeKnora import/status/search, L0 resolve, Langfuse ingestion, and external MCP SDK smoke reports.",
            "- `qa/human-reviews.jsonl` with passing human review coverage and failure attribution.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def generate_artifacts(
    *,
    release_report_path: Path,
    scope_report_path: Path,
    human_review_gate_path: Path,
    human_reviews_path: Path,
    qa_report_paths: dict[str, Path],
    output_dir: Path,
    report_date: str,
    profile: str = "full",
) -> dict[str, Any]:
    generated_at = datetime.now(timezone.utc).isoformat()
    release = load_json(release_report_path)
    scope = load_json(scope_report_path)
    human_review = load_json(human_review_gate_path)
    human_reviews = load_jsonl(human_reviews_path)
    qa_reports = {name: load_json(path) for name, path in qa_report_paths.items()}

    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "acceptance_report": output_dir / f"acceptance-report-{report_date}.md",
        "qa_report": output_dir / f"qa-report-{report_date}.md",
        "failure_analysis": output_dir / f"failure-analysis-{report_date}.md",
    }
    paths["acceptance_report"].write_text(
        build_acceptance_report(
            release=release,
            scope=scope,
            human_review=human_review,
            generated_at=generated_at,
            profile=profile,
        ),
        encoding="utf-8",
    )
    paths["qa_report"].write_text(
        build_qa_report(qa_reports=qa_reports, human_review=human_review, generated_at=generated_at),
        encoding="utf-8",
    )
    paths["failure_analysis"].write_text(
        build_failure_analysis(
            release=release,
            human_review=human_review,
            human_reviews=human_reviews,
            generated_at=generated_at,
            profile=profile,
        ),
        encoding="utf-8",
    )
    return {
        "status": "written",
        "generated_at": generated_at,
        "paths": {key: str(path) for key, path in paths.items()},
        "release_status": release.get("status", "missing"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate MVP acceptance, QA, and failure-analysis Markdown artifacts.")
    parser.add_argument("--profile", choices=["full", "mit"], default="full")
    parser.add_argument("--release-report-path", default="qa/reports/mvp-release-gate-2026-07-09.json")
    parser.add_argument("--scope-report-path", default="qa/reports/mvp-scope-gate-2026-07-09.json")
    parser.add_argument("--human-review-gate-path", default="qa/reports/human-qa-review-gate-2026-07-09.json")
    parser.add_argument("--human-reviews-path", default="qa/human-reviews.jsonl")
    parser.add_argument("--mit-gold-report-path", default="qa/reports/mit-gold-report-2026-07-09.json")
    parser.add_argument("--mvp-uat-report-path", default="qa/reports/mvp-uat-report-2026-07-09.json")
    parser.add_argument("--mvp-conversation-report-path", default="qa/reports/mvp-uat-conversations-report-2026-07-09.json")
    parser.add_argument("--output-dir", default="qa")
    parser.add_argument("--report-date", default=utc_date())
    args = parser.parse_args()

    report = generate_artifacts(
        release_report_path=Path(args.release_report_path),
        scope_report_path=Path(args.scope_report_path),
        human_review_gate_path=Path(args.human_review_gate_path),
        human_reviews_path=Path(args.human_reviews_path),
        qa_report_paths={
            "mit_gold": Path(args.mit_gold_report_path),
            "mvp_uat": Path(args.mvp_uat_report_path),
            "mvp_conversations": Path(args.mvp_conversation_report_path),
        },
        output_dir=Path(args.output_dir),
        report_date=args.report_date,
        profile=args.profile,
    )
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
