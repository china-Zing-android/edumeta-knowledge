from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class GateSpec:
    name: str
    path: Path
    accepted_statuses: frozenset[str]
    detail_fn: Callable[[dict[str, Any]], list[str]] | None = None
    defer_allowed: bool = False


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def qa_detail(payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if payload.get("failed", 0) != 0:
        failures.append(f"failed={payload.get('failed')}")
    if payload.get("failures"):
        failures.extend(str(item) for item in payload["failures"][:5])
    return failures


def diff_detail(payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if payload.get("publishable") is not True:
        failures.append("publishable is not true")
    if payload.get("blocking_failures"):
        failures.extend(str(item) for item in payload["blocking_failures"][:5])
    return failures


def readiness_detail(payload: dict[str, Any]) -> list[str]:
    return [str(item) for item in payload.get("failures", [])[:10]]


def latest_report_path(reports: Path, pattern: str, fallback_name: str) -> Path:
    matches = [path for path in reports.glob(pattern) if path.is_file()]
    if not matches:
        return reports / fallback_name
    return max(matches, key=lambda path: path.stat().st_mtime)


def default_gate_specs(root: Path = ROOT) -> list[GateSpec]:
    reports = root / "qa/reports"
    return [
        GateSpec(
            "retrieval_acceptance",
            latest_report_path(reports, "retrieval-acceptance-*.json", "retrieval-acceptance-missing.json"),
            frozenset({"passed"}),
            qa_detail,
        ),
        GateSpec(
            "cross_university_acceptance",
            latest_report_path(reports, "cross-university-acceptance-*.json", "cross-university-acceptance-missing.json"),
            frozenset({"passed"}),
            qa_detail,
        ),
        GateSpec("mcp_benchmark", latest_report_path(reports, "mcp-benchmark-*.json", "mcp-benchmark-missing.json"), frozenset({"passed"})),
        GateSpec("incremental_update", latest_report_path(reports, "incremental-update-*.json", "incremental-update-missing.json"), frozenset({"passed"})),
        GateSpec(
            "runtime_compose",
            latest_report_path(reports, "runtime-compose-*.json", "runtime-compose-missing.json"),
            frozenset({"passed"}),
            readiness_detail,
        ),
    ]


def mit_gate_specs(root: Path = ROOT) -> list[GateSpec]:
    return default_gate_specs(root)


def gate_specs_for_profile(profile: str, root: Path = ROOT) -> list[GateSpec]:
    if profile == "full":
        return default_gate_specs(root)
    if profile == "mit":
        return mit_gate_specs(root)
    raise ValueError(f"Unsupported release profile {profile!r}.")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_gate(spec: GateSpec) -> dict[str, Any]:
    if not spec.path.exists():
        return {
            "name": spec.name,
            "path": str(spec.path),
            "status": "missing",
            "passed": False,
            "failures": ["report file missing"],
        }
    try:
        payload = load_json(spec.path)
    except Exception as exc:  # noqa: BLE001 - preserve malformed report as release failure.
        return {
            "name": spec.name,
            "path": str(spec.path),
            "status": "invalid_report",
            "passed": False,
            "failures": [str(exc)],
        }
    status = str(payload.get("status"))
    failures: list[str] = []
    if status not in spec.accepted_statuses:
        failures.append(f"status {status!r} not in accepted statuses {sorted(spec.accepted_statuses)}")
    if spec.detail_fn:
        failures.extend(spec.detail_fn(payload))
    return {
        "name": spec.name,
        "path": str(spec.path),
        "status": status,
        "passed": not failures,
        "failures": failures,
    }


def evaluate_release_gate(
    specs: list[GateSpec] | None = None,
    *,
    profile: str = "custom",
    manual_qa_mode: str = "required",
) -> dict[str, Any]:
    if manual_qa_mode not in {"required", "deferred"}:
        raise ValueError(f"Unsupported manual_qa_mode {manual_qa_mode!r}.")
    specs = specs or default_gate_specs()
    deferred_specs = [spec for spec in specs if manual_qa_mode == "deferred" and spec.defer_allowed]
    active_specs = [spec for spec in specs if spec not in deferred_specs]
    results = [evaluate_gate(spec) for spec in active_specs]
    failures = [f"{result['name']}: {failure}" for result in results for failure in result["failures"]]
    return {
        "status": "failed" if failures else ("passed_with_deferred_manual_qa" if deferred_specs else "passed"),
        "profile": profile,
        "manual_qa_mode": manual_qa_mode,
        "deferred_gates": [spec.name for spec in deferred_specs],
        "generated_at": utc_now_iso(),
        "total": len(results),
        "passed": sum(1 for result in results if result["passed"]),
        "failed": sum(1 for result in results if not result["passed"]),
        "failures": failures,
        "results": results,
    }


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate MVP release gates into one acceptance report.")
    parser.add_argument("--profile", choices=["full", "mit"], default="full")
    parser.add_argument("--manual-qa-mode", choices=["required", "deferred"], default="required")
    parser.add_argument("--output-path", default=None)
    parser.add_argument("--allow-failed", action="store_true")
    args = parser.parse_args()

    report = evaluate_release_gate(
        gate_specs_for_profile(args.profile),
        profile=args.profile,
        manual_qa_mode=args.manual_qa_mode,
    )
    if args.output_path:
        write_report(Path(args.output_path), report)
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    if report["status"] not in {"passed", "passed_with_deferred_manual_qa"} and not args.allow_failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
