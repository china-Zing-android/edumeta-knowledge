from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate automated QA/UAT report against release gate thresholds.")
    parser.add_argument("--cases-path", required=True)
    parser.add_argument("--report-path", required=True)
    parser.add_argument("--min-total", type=int, required=True)
    parser.add_argument("--min-conversations", type=int, default=None)
    parser.add_argument("--allow-failures", action="store_true")
    parser.add_argument("--allow-missing-trace-id", action="store_true")
    parser.add_argument("--output-path", default=None)
    args = parser.parse_args()

    import sys

    root = Path(__file__).resolve().parents[1]
    fast_router_src = root / "apps/fast-router/src"
    if str(fast_router_src) not in sys.path:
        sys.path.insert(0, str(fast_router_src))

    from fast_router.qa import evaluate_qa_gate, load_qa_cases, write_qa_report

    cases = load_qa_cases(Path(args.cases_path))
    report = json.loads(Path(args.report_path).read_text(encoding="utf-8"))
    gate = evaluate_qa_gate(
        report,
        cases,
        min_total=args.min_total,
        min_conversations=args.min_conversations,
        require_all_passed=not args.allow_failures,
        require_trace_id=not args.allow_missing_trace_id,
    )
    print(json.dumps(gate, ensure_ascii=False, indent=2, sort_keys=True))
    if args.output_path:
        write_qa_report(Path(args.output_path), gate)
    if gate["status"] != "passed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
