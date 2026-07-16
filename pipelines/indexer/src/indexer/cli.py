from __future__ import annotations

import argparse
import json
from pathlib import Path

from .opensearch_publisher import dry_run_report, publish_school


def discover_data_dirs(data_root: Path) -> dict[str, Path]:
    if not data_root.exists():
        return {}
    return {
        path.name.lower(): path
        for path in sorted(data_root.iterdir())
        if path.is_dir() and (path / "catalog_entries.jsonl").exists()
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


def write_report(path: Path, report: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_batch(args: argparse.Namespace) -> dict:
    schools = discover_data_dirs(Path(args.data_root))
    if not schools:
        return batch_report(args.command, [], [{"university_id": None, "reason": "NO_SCHOOLS_DISCOVERED"}])
    results: list[dict] = []
    failures: list[dict] = []
    for university_id, data_dir in schools.items():
        try:
            if args.dry_run or args.command == "index-school":
                results.append(dry_run_report(data_dir, university_id))
            else:
                if not args.opensearch_url:
                    raise ValueError("--opensearch-url is required for publish-school unless --dry-run is set")
                results.append(publish_school(data_dir, university_id, args.opensearch_url))
        except Exception as exc:  # noqa: BLE001 - batch mode must attribute per-school failures.
            failures.append({"university_id": university_id, "reason": str(exc)})
            if not args.continue_on_error:
                break
    return batch_report(args.command, results, failures)


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish L1 JSONL data to OpenSearch staging indexes.")
    parser.add_argument("command", choices=["index-school", "publish-school"])
    parser.add_argument("--university-id", default=None)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--data-dir", default=None)
    parser.add_argument("--data-root", default="data/normalized")
    parser.add_argument("--opensearch-url", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output-path", default=None)
    parser.add_argument("--continue-on-error", action="store_true")
    args = parser.parse_args()

    if args.all:
        report = run_batch(args)
        if args.output_path:
            write_report(Path(args.output_path), report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report["status"] != "success":
            raise SystemExit(1)
        return
    if not args.university_id:
        raise SystemExit("--university-id is required unless --all is set")

    data_dir = Path(args.data_dir or f"data/normalized/{args.university_id}")
    if args.dry_run or args.command == "index-school":
        print(json.dumps(dry_run_report(data_dir, args.university_id), ensure_ascii=False, indent=2))
        return

    if not args.opensearch_url:
        raise SystemExit("--opensearch-url is required for publish-school unless --dry-run is set")
    print(json.dumps(publish_school(data_dir, args.university_id, args.opensearch_url), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
