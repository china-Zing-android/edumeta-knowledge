from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Fast Router QA/UAT suites and write a report.")
    parser.add_argument("--suite-path", required=True)
    parser.add_argument("--output-path", required=True)
    parser.add_argument("--mode", choices=["single", "conversation"], default="single")
    args = parser.parse_args()

    import sys

    root = Path(__file__).resolve().parents[1]
    fast_router_src = root / "apps/fast-router/src"
    if str(fast_router_src) not in sys.path:
        sys.path.insert(0, str(fast_router_src))

    from fast_router.main import FastAnswerRequest, fast_answer
    from fast_router.qa import run_conversation_cases, run_qa_cases, write_qa_report

    def answer(question: str, context: dict | None = None) -> dict:
        query = question
        if context and context.get("transcript"):
            previous_user_turns = [
                item["content"]
                for item in context["transcript"]
                if item.get("role") == "user" and isinstance(item.get("content"), str)
            ]
            if previous_user_turns:
                query = f"{previous_user_turns[-1]} {question}"
        return fast_answer(FastAnswerRequest(query=query)).model_dump()

    if args.mode == "conversation":
        report = run_conversation_cases(Path(args.suite_path), answer)
    else:
        report = run_qa_cases(Path(args.suite_path), lambda question: answer(question))
    payload = {
        "suite_path": args.suite_path,
        "mode": args.mode,
        **report,
    }
    write_qa_report(Path(args.output_path), payload)
    print(f"{payload['total']} {payload['passed']} {payload['failed']}")
    if payload["failed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
