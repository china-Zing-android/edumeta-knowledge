from __future__ import annotations

import argparse
import json
from pathlib import Path

from .adapters import ParserAdapterNotFoundError, parse_school_markdown
from .diff import diff_school, write_diff_report
from .postgres_loader import dry_run_report, load_school_to_postgres
from .validation import validate_school, write_validation_report


def discover_markdown_inputs(input_root: Path) -> dict[str, Path]:
    if not input_root.exists():
        return {}
    return {path.stem.lower(): path for path in sorted(input_root.glob("*.md")) if path.is_file()}


def discover_data_dirs(data_root: Path) -> dict[str, Path]:
    if not data_root.exists():
        return {}
    return {
        path.name.lower(): path
        for path in sorted(data_root.iterdir())
        if path.is_dir() and (path / "source_registry.jsonl").exists()
    }


def batch_report(command: str, results: list[dict], failures: list[dict]) -> dict:
    status = "success" if not failures else ("partial_failure" if results else "failed")
    return {
        "mode": "batch",
        "command": command,
        "status": status,
        "total": len(results) + len(failures),
        "succeeded": len(results),
        "failed": len(failures),
        "results": results,
        "failures": failures,
    }


def maybe_write_report(output_path: str | None, report: dict) -> None:
    if output_path:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_batch(args: argparse.Namespace) -> dict:
    results: list[dict] = []
    failures: list[dict] = []
    if args.command == "parse-school":
        schools = discover_markdown_inputs(Path(args.input_root))
    else:
        schools = discover_data_dirs(Path(args.data_root))
    if not schools:
        return batch_report(args.command, [], [{"university_id": None, "reason": "NO_SCHOOLS_DISCOVERED"}])

    for university_id, path in schools.items():
        try:
            if args.command == "parse-school":
                result = parse_school_markdown(university_id, path, fallback_adapter_name=args.default_adapter)
                out_dir = Path(args.out_root) / university_id
                out_dir.mkdir(parents=True, exist_ok=True)
                result.write_jsonl(out_dir)
                results.append(result.summary | {"university_id": university_id, "out_dir": str(out_dir)})
            elif args.command == "validate-school":
                report = validate_school(path, university_id)
                if report["status"] == "failed":
                    failures.append({"university_id": university_id, "reason": "VALIDATION_FAILED", "report": report})
                else:
                    results.append(report)
            elif args.command == "diff-school":
                if not args.previous_data_root:
                    raise ValueError("--previous-data-root is required for diff-school --all")
                previous_root = Path(args.previous_data_root)
                report = diff_school(
                    previous_root / university_id,
                    path,
                    university_id,
                    allow_active_removal=args.allow_active_removal,
                )
                if report["status"] == "failed":
                    failures.append({"university_id": university_id, "reason": "DIFF_FAILED", "report": report})
                else:
                    results.append(report)
            elif args.command == "load-school":
                if args.dry_run:
                    results.append(dry_run_report(path, university_id))
                else:
                    if not args.postgres_dsn:
                        raise ValueError("--postgres-dsn is required unless --dry-run is set")
                    results.append(load_school_to_postgres(path, university_id, args.postgres_dsn, run_id=args.run_id))
        except Exception as exc:  # noqa: BLE001 - batch mode must attribute per-school failures.
            failures.append({"university_id": university_id, "reason": str(exc)})
            if not args.continue_on_error:
                break
    return batch_report(args.command, results, failures)


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse school Markdown into MVP JSONL records.")
    parser.add_argument(
        "command",
        choices=[
            "parse-school",
            "validate-school",
            "diff-school",
            "load-school",
        ],
    )
    parser.add_argument("--university-id", default=None)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--input", default="docs/MIT_知识库_完整深度数据_v2.md")
    parser.add_argument("--input-root", default="data/raw-md")
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--out-root", default="data/normalized")
    parser.add_argument("--adapter", default=None, help="Explicit parser adapter for single-school parsing, e.g. generic_structured.")
    parser.add_argument("--default-adapter", default=None, help="Fallback parser adapter for parse-school --all when no school-specific adapter exists.")
    parser.add_argument("--data-dir", default=None)
    parser.add_argument("--data-root", default="data/normalized")
    parser.add_argument("--previous-data-dir", default=None)
    parser.add_argument("--previous-data-root", default=None)
    parser.add_argument("--output-path", default=None)
    parser.add_argument("--continue-on-error", action="store_true")
    parser.add_argument("--allow-active-removal", action="store_true")
    parser.add_argument("--postgres-dsn", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--run-id", default=None)
    args = parser.parse_args()

    if args.all:
        report = run_batch(args)
        maybe_write_report(args.output_path, report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report["status"] != "success":
            raise SystemExit(1)
        return
    if not args.university_id:
        raise SystemExit("--university-id is required unless --all is set")

    if args.command == "validate-school":
        data_dir = Path(args.data_dir or args.out_dir or f"data/normalized/{args.university_id}")
        report = validate_school(data_dir, args.university_id)
        if args.output_path:
            write_validation_report(Path(args.output_path), report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report["status"] == "failed":
            raise SystemExit(1)
        return

    if args.command == "diff-school":
        if not args.previous_data_dir:
            raise SystemExit("--previous-data-dir is required for diff-school")
        current_data_dir = Path(args.data_dir or args.out_dir or f"data/normalized/{args.university_id}")
        report = diff_school(
            Path(args.previous_data_dir),
            current_data_dir,
            args.university_id,
            allow_active_removal=args.allow_active_removal,
        )
        if args.output_path:
            write_diff_report(Path(args.output_path), report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report["status"] == "failed":
            raise SystemExit(1)
        return

    if args.command == "load-school":
        data_dir = Path(args.data_dir or args.out_dir or f"data/normalized/{args.university_id}")
        if args.dry_run:
            print(json.dumps(dry_run_report(data_dir, args.university_id), ensure_ascii=False, indent=2))
            return
        if not args.postgres_dsn:
            raise SystemExit("--postgres-dsn is required unless --dry-run is set")
        print(
            json.dumps(
                load_school_to_postgres(data_dir, args.university_id, args.postgres_dsn, run_id=args.run_id),
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    try:
        result = parse_school_markdown(args.university_id, Path(args.input), adapter_name=args.adapter)
    except (ParserAdapterNotFoundError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc

    out_dir = Path(args.out_dir or f"data/normalized/{args.university_id}")
    out_dir.mkdir(parents=True, exist_ok=True)
    result.write_jsonl(out_dir)
    print(json.dumps(result.summary | {"out_dir": str(out_dir)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
