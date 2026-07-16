from __future__ import annotations

import json
import inspect
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable


@dataclass
class QACaseResult:
    qa_case_id: str
    passed: bool
    failures: list[str]
    trace_id: str | None


def load_qa_cases(path: Path) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                cases.append(json.loads(line))
    return cases


def evaluate_case(case: dict[str, Any], response: dict[str, Any]) -> QACaseResult:
    text = json.dumps(response, ensure_ascii=False).lower()
    failures: list[str] = []
    for item in case.get("must_include", []):
        if item and str(item).lower() not in text:
            failures.append(f"missing must_include: {item}")
    for item in case.get("must_not_include", []):
        if item and str(item).lower() in text:
            failures.append(f"contains must_not_include: {item}")
    expected_route = case.get("expected_route")
    if expected_route and response.get("route") != expected_route:
        # deep_required is acceptable for deep QA because evidence can be unavailable before WeKnora import.
        if not (expected_route == "deep" and response.get("route") == "deep"):
            failures.append(f"route mismatch: expected {expected_route}, got {response.get('route')}")
    if case.get("risk_level") == "P0" and response.get("mode") == "fast" and not response.get("evidence") and response.get("route") == "deep":
        failures.append("P0 deep answer lacks evidence")
    return QACaseResult(
        qa_case_id=case["qa_case_id"],
        passed=not failures,
        failures=failures,
        trace_id=response.get("trace_id"),
    )


def run_qa_cases(path: Path, answer_func: Callable[[str], dict[str, Any]]) -> dict[str, Any]:
    results = []
    for case in load_qa_cases(path):
        response = answer_func(case["question"])
        results.append(evaluate_case(case, response))
    return {
        "total": len(results),
        "passed": sum(1 for r in results if r.passed),
        "failed": sum(1 for r in results if not r.passed),
        "results": [r.__dict__ for r in results],
    }


def _call_answer(answer_func: Callable[..., dict[str, Any]], question: str, context: dict[str, Any]) -> dict[str, Any]:
    parameters = inspect.signature(answer_func).parameters
    if len(parameters) >= 2:
        return answer_func(question, context)
    return answer_func(question)


def _turn_case(parent_case: dict[str, Any], turn: dict[str, Any], index: int) -> dict[str, Any]:
    return {
        "qa_case_id": f"{parent_case['qa_case_id']}::turn_{index}",
        "expected_route": turn.get("expected_route", parent_case.get("expected_route")),
        "must_include": turn.get("must_include", []),
        "must_not_include": turn.get("must_not_include", parent_case.get("must_not_include", [])),
        "risk_level": turn.get("risk_level", parent_case.get("risk_level")),
    }


def run_conversation_cases(path: Path, answer_func: Callable[..., dict[str, Any]]) -> dict[str, Any]:
    results: list[QACaseResult] = []
    conversations: list[dict[str, Any]] = []
    for case in load_qa_cases(path):
        transcript: list[dict[str, Any]] = []
        turns = [
            turn if isinstance(turn, dict) else {"role": "user", "content": str(turn)}
            for turn in case.get("conversation_context", [])
        ]
        turns.append({"role": "user", "content": case["question"], "final": True})
        for index, turn in enumerate(turns, start=1):
            if turn.get("role", "user") != "user":
                transcript.append(turn)
                continue
            context = {
                "qa_case_id": case["qa_case_id"],
                "persona": case.get("persona"),
                "transcript": transcript,
            }
            response = _call_answer(answer_func, turn["content"], context)
            transcript.append({"role": "user", "content": turn["content"]})
            transcript.append({"role": "assistant", "content": response})
            evaluated_case = case if turn.get("final") else _turn_case(case, turn, index)
            result = evaluate_case(evaluated_case, response)
            results.append(result)
        conversations.append(
            {
                "qa_case_id": case["qa_case_id"],
                "turns": len([turn for turn in turns if turn.get("role", "user") == "user"]),
                "trace_ids": [item.trace_id for item in results if item.qa_case_id == case["qa_case_id"] or item.qa_case_id.startswith(f"{case['qa_case_id']}::")],
            }
        )
    return {
        "total": len(results),
        "passed": sum(1 for r in results if r.passed),
        "failed": sum(1 for r in results if not r.passed),
        "conversation_count": len(conversations),
        "conversations": conversations,
        "results": [r.__dict__ for r in results],
    }


def evaluate_qa_gate(
    report: dict[str, Any],
    cases: list[dict[str, Any]],
    *,
    min_total: int,
    min_conversations: int | None = None,
    require_all_passed: bool = True,
    require_trace_id: bool = True,
) -> dict[str, Any]:
    cases_by_id = {case["qa_case_id"]: case for case in cases}
    failures: list[str] = []
    if report.get("total", 0) < min_total:
        failures.append(f"total below threshold: expected >= {min_total}, got {report.get('total', 0)}")
    if min_conversations is not None and report.get("conversation_count", 0) < min_conversations:
        failures.append(
            f"conversation_count below threshold: expected >= {min_conversations}, got {report.get('conversation_count', 0)}"
        )
    if require_all_passed and report.get("failed", 0) != 0:
        failures.append(f"failed cases present: {report.get('failed', 0)}")
    p0_failed = []
    for result in report.get("results", []):
        base_case_id = str(result.get("qa_case_id", "")).split("::", 1)[0]
        case = cases_by_id.get(base_case_id)
        if case and case.get("risk_level") == "P0" and not result.get("passed"):
            p0_failed.append(result.get("qa_case_id"))
        if require_trace_id and not result.get("trace_id"):
            failures.append(f"missing trace_id: {result.get('qa_case_id')}")
    if p0_failed:
        failures.append(f"P0 failures: {', '.join(str(item) for item in p0_failed)}")
    return {
        "status": "passed" if not failures else "failed",
        "failures": failures,
        "total": report.get("total", 0),
        "conversation_count": report.get("conversation_count"),
        "passed": report.get("passed", 0),
        "failed": report.get("failed", 0),
    }


def write_qa_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
