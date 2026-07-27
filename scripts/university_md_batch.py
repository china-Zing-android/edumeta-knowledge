from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
import time
import unicodedata
from pathlib import Path
from typing import Any

import httpx


ROOT = Path(__file__).resolve().parents[1]
for source_root in (
    ROOT / "apps/fast-router/src",
    ROOT / "pipelines/catalog-parser/src",
    ROOT / "pipelines/indexer/src",
):
    if str(source_root) not in sys.path:
        sys.path.insert(0, str(source_root))

DEFAULT_DATA_ROOT = ROOT / "data/raw-md/universities"
DEFAULT_MANIFEST = DEFAULT_DATA_ROOT / "manifest.jsonl"
DEFAULT_PREFLIGHT = DEFAULT_DATA_ROOT / "preflight-results.jsonl"
DEFAULT_STATE = ROOT / "data/import-state/university-md-batch.jsonl"
FILE_SUFFIX = "_知识库_完整深度数据_v2.md"
TERMINAL_INGESTION_STATUSES = {"published", "unchanged", "failed"}

KNOWN_IDS = {
    "mit": "mit",
    "harvard": "harvard",
    "stanford": "stanford",
    "princeton": "princeton",
    "ucberkeley": "berkeley",
    "caltech": "caltech",
    "duke": "duke",
    "asu": "asu",
}

NAME_OVERRIDES = {
    "us/duke_知识库_完整深度数据_v2.md": "Duke University",
    "us/纽约大学_知识库_完整深度数据_v2.md": "New York University",
}

SEMANTIC_OVERRIDES = {
    "us/nyu_知识库_完整深度数据_v2.md": "new_york_university",
    "us/纽约大学_知识库_完整深度数据_v2.md": "new_york_university",
}

PREFERRED_DUPLICATE_PATHS = {
    "new_york_university": "us/NYU_知识库_完整深度数据_v2.md",
}


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text("utf-8").splitlines() if line.strip()]


def ascii_slug(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", value)).strip("_")


def file_stem(path: Path) -> str:
    name = path.name
    return name[: -len(FILE_SUFFIX)] if name.endswith(FILE_SUFFIX) else path.stem


def first_heading(text: str) -> str:
    return next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), "")


def normalized_university_name(heading: str, stem: str, relative_path: str) -> str:
    if relative_path.lower() in NAME_OVERRIDES:
        return NAME_OVERRIDES[relative_path.lower()]
    value = re.split(r"\s+(?:Admissions|Knowledge Base|知识库|—|–)", heading, maxsplit=1)[0].strip()
    if not value or value.lower() in {"admissions", "admissions knowledge base"}:
        value = stem.replace("_", " ").strip()
    return value


def semantic_key(name: str, stem: str, relative_path: str) -> str:
    override = SEMANTIC_OVERRIDES.get(relative_path.lower())
    if override:
        return override
    without_acronym = re.sub(r"\s*\([^)]{1,16}\)\s*", " ", name)
    return ascii_slug(without_acronym) or ascii_slug(stem) or hashlib.sha256(relative_path.encode()).hexdigest()[:12]


def capture_date(text: str) -> str | None:
    head = "\n".join(text.splitlines()[:80])
    match = re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", head)
    return match.group(1) if match else None


def aliases_for(stem: str, name: str) -> list[str]:
    values = {stem.replace("_", " ").strip(), name}
    acronym = re.search(r"\(([A-Z][A-Z0-9&.-]{1,12})\)", name)
    if acronym:
        values.add(acronym.group(1))
    return sorted(value for value in values if value)


def build_manifest(data_root: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    documents: list[dict[str, Any]] = []
    for path in sorted(data_root.glob("*/*.md")):
        relative = path.relative_to(data_root).as_posix()
        country = path.parent.name.upper()
        text = path.read_text("utf-8")
        stem = file_stem(path)
        heading = first_heading(text)
        name = normalized_university_name(heading, stem, relative)
        documents.append(
            {
                "relative_path": relative,
                "country_code": country,
                "stem": stem,
                "university_name": name,
                "aliases": aliases_for(stem, name),
                "semantic_key": semantic_key(name, stem, relative),
                "capture_date": capture_date(text),
                "size_bytes": path.stat().st_size,
                "content_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )

    semantic_groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for document in documents:
        semantic_groups.setdefault((document["country_code"], document["semantic_key"]), []).append(document)

    winners: dict[str, dict[str, Any]] = {}
    duplicate_of_path: dict[str, str] = {}
    for group in semantic_groups.values():
        preferred_path = PREFERRED_DUPLICATE_PATHS.get(group[0]["semantic_key"])
        winner = next(
            (row for row in group if row["relative_path"] == preferred_path),
            sorted(group, key=lambda row: (-row["size_bytes"], row["relative_path"]))[0],
        )
        winners[winner["relative_path"]] = winner
        for duplicate in group:
            if duplicate is not winner:
                duplicate_of_path[duplicate["relative_path"]] = winner["relative_path"]

    base_ids: dict[str, str] = {}
    for relative, document in winners.items():
        stem_key = ascii_slug(document["stem"])
        base_ids[relative] = KNOWN_IDS.get(stem_key, stem_key or document["semantic_key"])

    collisions: dict[str, list[str]] = {}
    for relative, base_id in base_ids.items():
        collisions.setdefault(base_id, []).append(relative)

    resolved_ids: dict[str, str] = {}
    for base_id, relatives in collisions.items():
        for relative in relatives:
            if len(relatives) == 1:
                resolved_ids[relative] = base_id
            else:
                country = winners[relative]["country_code"].lower()
                resolved_ids[relative] = f"{country}_{base_id}"

    rows: list[dict[str, Any]] = []
    for document in documents:
        relative = document["relative_path"]
        canonical_path = duplicate_of_path.get(relative, relative)
        canonical_id = resolved_ids[canonical_path]
        enabled = relative == canonical_path
        warnings: list[str] = []
        if not document["capture_date"]:
            warnings.append("capture_date_not_detected")
        if document["size_bytes"] < 5000:
            warnings.append("small_document_under_5kb")
        rows.append(
            {
                "university_id": canonical_id,
                "university_name": document["university_name"],
                "aliases": document["aliases"],
                "country_code": document["country_code"],
                "region": None,
                "school_tier": "core",
                "relative_path": relative,
                "parser_adapter": "auto",
                "enabled": enabled,
                "review_status": "ready" if enabled else "duplicate",
                "duplicate_of": None if enabled else canonical_id,
                "capture_date": document["capture_date"],
                "size_bytes": document["size_bytes"],
                "content_sha256": document["content_sha256"],
                "warnings": warnings,
            }
        )

    summary = {
        "documents": len(rows),
        "enabled": sum(1 for row in rows if row["enabled"]),
        "duplicates": sum(1 for row in rows if not row["enabled"]),
        "countries": {
            country: sum(1 for row in rows if row["country_code"] == country)
            for country in sorted({row["country_code"] for row in rows})
        },
        "warnings": sum(len(row["warnings"]) for row in rows),
    }
    return rows, summary


def selected_rows(rows: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    selected = [row for row in rows if row.get("enabled")]
    if args.country:
        countries = {value.upper() for value in args.country}
        selected = [row for row in selected if row["country_code"] in countries]
    if args.university_id:
        ids = set(args.university_id)
        selected = [row for row in selected if row["university_id"] in ids]
    if args.limit:
        selected = selected[: args.limit]
    return selected


def pending_rows(
    records: list[dict[str, Any]],
    state_by_id: dict[str, dict[str, Any]],
    preflight_by_id: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    pending: list[dict[str, Any]] = []
    for record in records:
        state = state_by_id.get(record["university_id"], {})
        preflight = preflight_by_id.get(record["university_id"], {})
        audit_version = (preflight.get("quality_audit") or {}).get("audit_version")
        reusable = (
            state.get("status") in {"published", "unchanged"}
            and state.get("content_sha256") == record.get("content_sha256")
            and state.get("audit_version") == audit_version
        )
        if not reusable:
            pending.append(record)
    return pending


def run_preflight(record: dict[str, Any], data_root: Path) -> dict[str, Any]:
    from catalog_parser.adapters import parse_school_markdown
    from catalog_parser.validation import validate_school

    started = time.perf_counter()
    try:
        with tempfile.TemporaryDirectory(prefix=f"edumeta-{record['university_id']}-") as temp_dir:
            result = parse_school_markdown(
                record["university_id"],
                data_root / record["relative_path"],
                fallback_adapter_name=record.get("parser_adapter") or "auto",
            )
            output = Path(temp_dir)
            result.write_jsonl(output)
            markdown_text = (data_root / record["relative_path"]).read_text("utf-8")
            validation = validate_school(
                output,
                record["university_id"],
                markdown_text=markdown_text,
                parser_summary=result.summary,
            )
        catalog_count = int(validation.get("counts", {}).get("catalog_entries") or 0)
        status = "passed" if validation["status"] == "passed" else "failed"
        review_reasons: list[str] = []
        if status == "passed" and catalog_count < 5:
            status = "needs_review"
            review_reasons.append("catalog_entries_below_5")
        quality = validation.get("checks", {}).get("catalog_quality", {})
        failures = list(validation.get("failures", []))
        failures.extend(name for name in quality.get("failures") or [] if name not in failures)
        if status == "passed" and quality.get("audit_status") == "needs_review":
            status = "needs_review"
            review_reasons.extend(quality.get("warnings") or [])
        return {
            "university_id": record["university_id"],
            "relative_path": record["relative_path"],
            "content_sha256": record.get("content_sha256"),
            "status": status,
            "parser_adapter": result.summary.get("parser_adapter", record.get("parser_adapter")),
            "counts": validation.get("counts", {}),
            "failures": failures,
            "review_reasons": review_reasons,
            "quality_audit": quality,
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
        }
    except Exception as exc:  # noqa: BLE001 - preflight must attribute every document failure.
        from catalog_parser.validation import parser_failure_audit

        quality = parser_failure_audit(str(exc))
        report = {
            "university_id": record["university_id"],
            "relative_path": record["relative_path"],
            "content_sha256": record.get("content_sha256"),
            "status": "failed",
            "error": str(exc),
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
        }
        if quality:
            report["failures"] = quality["failures"]
            report["quality_audit"] = quality
        return report


def upload_school(client: httpx.Client, base_url: str, data_root: Path, record: dict[str, Any]) -> dict[str, Any]:
    path = data_root / record["relative_path"]
    with path.open("rb") as handle:
        response = client.post(
            f"{base_url}/v1/university-ingestions",
            data={
                "university_id": record["university_id"],
                "school_tier": record["school_tier"],
                "university_name": record["university_name"],
                "country_code": record["country_code"],
                "region": record.get("region") or "",
                "aliases": ",".join(record.get("aliases") or []),
                "create_new_weknora_kb": "false",
            },
            files={"file": (path.name, handle, "text/markdown")},
        )
    response.raise_for_status()
    return response.json()


def poll_ingestion(client: httpx.Client, base_url: str, run_id: str, timeout_seconds: float) -> dict[str, Any]:
    deadline = time.monotonic() + timeout_seconds
    while True:
        response = client.get(f"{base_url}/v1/university-ingestions/{run_id}")
        response.raise_for_status()
        payload = response.json()
        if payload.get("status") in TERMINAL_INGESTION_STATUSES:
            return payload
        if time.monotonic() >= deadline:
            raise TimeoutError(f"ingestion {run_id} did not finish within {timeout_seconds}s")
        time.sleep(2)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build, preflight, and ingest a country-organized university Markdown batch.")
    sub = parser.add_subparsers(dest="command", required=True)

    manifest = sub.add_parser("manifest")
    manifest.add_argument("--data-root", type=Path, default=DEFAULT_DATA_ROOT)
    manifest.add_argument("--output", type=Path, default=DEFAULT_MANIFEST)

    preflight = sub.add_parser("preflight")
    preflight.add_argument("--data-root", type=Path, default=DEFAULT_DATA_ROOT)
    preflight.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    preflight.add_argument("--output", type=Path, default=DEFAULT_PREFLIGHT)

    ingest = sub.add_parser("ingest")
    ingest.add_argument("--data-root", type=Path, default=DEFAULT_DATA_ROOT)
    ingest.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    ingest.add_argument("--preflight", type=Path, default=DEFAULT_PREFLIGHT)
    ingest.add_argument("--state", type=Path, default=DEFAULT_STATE)
    ingest.add_argument("--base-url", default="http://127.0.0.1:8000")
    ingest.add_argument("--timeout-seconds", type=float, default=900)
    ingest.add_argument("--dry-run", action="store_true")
    ingest.add_argument("--allow-unverified", action="store_true")

    for command in (preflight, ingest):
        command.add_argument("--country", action="append", default=[])
        command.add_argument("--university-id", action="append", default=[])
        command.add_argument("--limit", type=int)

    args = parser.parse_args()
    if args.command == "manifest":
        rows, summary = build_manifest(args.data_root)
        write_jsonl(args.output, rows)
        print(json.dumps(summary | {"manifest": str(args.output)}, ensure_ascii=False, indent=2, sort_keys=True))
        return

    manifest_rows = read_jsonl(args.manifest)
    if not manifest_rows:
        raise SystemExit(f"manifest is empty or missing: {args.manifest}")
    records = selected_rows(manifest_rows, args)

    if args.command == "preflight":
        results: list[dict[str, Any]] = []
        for index, record in enumerate(records, start=1):
            result = run_preflight(record, args.data_root)
            results.append(result)
            print(f"[{index}/{len(records)}] {record['university_id']}: {result['status']}", file=sys.stderr)
        write_jsonl(args.output, results)
        summary = {
            "selected": len(results),
            "passed": sum(1 for row in results if row["status"] == "passed"),
            "needs_review": sum(1 for row in results if row["status"] == "needs_review"),
            "failed": sum(1 for row in results if row["status"] == "failed"),
            "output": str(args.output),
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
        if summary["failed"] or summary["needs_review"]:
            raise SystemExit(1)
        return

    preflight_by_id = {row["university_id"]: row for row in read_jsonl(args.preflight)}
    if not args.allow_unverified:
        records = [
            row
            for row in records
            if preflight_by_id.get(row["university_id"], {}).get("status") == "passed"
            and preflight_by_id[row["university_id"]].get("content_sha256") == row.get("content_sha256")
        ]
    state_by_id = {row["university_id"]: row for row in read_jsonl(args.state)}
    pending = pending_rows(records, state_by_id, preflight_by_id)
    if args.dry_run:
        print(json.dumps({"selected": len(records), "pending": len(pending), "university_ids": [row["university_id"] for row in pending]}, ensure_ascii=False, indent=2))
        return

    base_url = args.base_url.rstrip("/")
    with httpx.Client(timeout=60) as client:
        for index, record in enumerate(pending, start=1):
            started = time.perf_counter()
            try:
                accepted = upload_school(client, base_url, args.data_root, record)
                terminal = accepted if accepted.get("status") == "unchanged" else poll_ingestion(
                    client, base_url, accepted["run_id"], args.timeout_seconds
                )
                state_by_id[record["university_id"]] = {
                    "university_id": record["university_id"],
                    "relative_path": record["relative_path"],
                    "run_id": accepted["run_id"],
                    "operation": accepted.get("operation"),
                    "status": terminal.get("status"),
                    "content_sha256": record.get("content_sha256"),
                    "audit_version": (preflight_by_id.get(record["university_id"], {}).get("quality_audit") or {}).get("audit_version"),
                    "counts": terminal.get("counts", {}),
                    "weknora_jobs": terminal.get("weknora_jobs", {}),
                    "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                }
            except Exception as exc:  # noqa: BLE001 - persist progress before continuing.
                state_by_id[record["university_id"]] = {
                    "university_id": record["university_id"],
                    "relative_path": record["relative_path"],
                    "status": "failed",
                    "content_sha256": record.get("content_sha256"),
                    "audit_version": (preflight_by_id.get(record["university_id"], {}).get("quality_audit") or {}).get("audit_version"),
                    "error": str(exc),
                    "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
                }
            write_jsonl(args.state, sorted(state_by_id.values(), key=lambda row: row["university_id"]))
            result = state_by_id[record["university_id"]]
            print(f"[{index}/{len(pending)}] {record['university_id']}: {result['status']}", file=sys.stderr)

    selected_states = [state_by_id.get(row["university_id"], {}) for row in records]
    summary = {
        "selected": len(records),
        "published_or_unchanged": sum(1 for row in selected_states if row.get("status") in {"published", "unchanged"}),
        "failed": sum(1 for row in selected_states if row.get("status") == "failed"),
        "state": str(args.state),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    if any(state_by_id.get(row["university_id"], {}).get("status") == "failed" for row in records):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
