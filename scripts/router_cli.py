from __future__ import annotations

import argparse
import json
from pathlib import Path

import httpx


def main() -> None:
    parser = argparse.ArgumentParser(description="HTTP client for Edumeta retrieval and ingestion.")
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    sub = parser.add_subparsers(dest="command", required=True)

    retrieve = sub.add_parser("retrieve")
    retrieve.add_argument("--query", required=True)
    retrieve.add_argument("--university-id")
    retrieve.add_argument("--level")
    retrieve.add_argument("--program-id")
    retrieve.add_argument("--entry-id")
    retrieve.add_argument("--direction", choices=["auto", "downward", "range", "upward"], default="auto")
    retrieve.add_argument("--country-code", action="append", default=[])
    retrieve.add_argument("--region", action="append", default=[])
    retrieve.add_argument("--degree-level", action="append", default=[])
    retrieve.add_argument("--search-level", action="append", default=[])
    retrieve.add_argument("--school-tier-filter", action="append", choices=["core", "non_core"], default=[])
    retrieve.add_argument("--max-results", type=int, default=5)

    ingest = sub.add_parser("ingest-school")
    ingest.add_argument("--university-id", required=True)
    ingest.add_argument("--school-tier", choices=["core", "non_core"], required=True)
    ingest.add_argument("--university-name")
    ingest.add_argument("--country-code")
    ingest.add_argument("--region")
    ingest.add_argument("--aliases")
    ingest.add_argument("--weknora-knowledge-base-id")
    ingest.add_argument("--create-new-weknora-kb", action="store_true")
    ingest.add_argument("--file", type=Path, required=True)

    status = sub.add_parser("ingestion-status")
    status.add_argument("--run-id", required=True)

    args = parser.parse_args()
    base = args.base_url.rstrip("/")
    with httpx.Client(timeout=10) as client:
        if args.command == "retrieve":
            context = {key: value for key, value in {
                "level": args.level, "program_id": args.program_id, "entry_id": args.entry_id,
            }.items() if value}
            response = client.post(f"{base}/v1/retrieve", json={
                "query": args.query,
                "university_id": args.university_id,
                "context": context,
                "direction": args.direction,
                "filters": {
                    "country_codes": args.country_code,
                    "regions": args.region,
                    "degree_levels": args.degree_level,
                    "levels": args.search_level,
                    "school_tiers": args.school_tier_filter,
                },
                "max_results": args.max_results,
            })
        elif args.command == "ingest-school":
            with args.file.open("rb") as handle:
                response = client.post(
                    f"{base}/v1/university-ingestions",
                    data={
                        key: value for key, value in {
                            "university_id": args.university_id,
                            "school_tier": args.school_tier,
                            "university_name": args.university_name,
                            "country_code": args.country_code,
                            "region": args.region,
                            "aliases": args.aliases,
                            "weknora_knowledge_base_id": args.weknora_knowledge_base_id,
                            "create_new_weknora_kb": str(args.create_new_weknora_kb).lower(),
                        }.items() if value is not None
                    },
                    files={"file": (args.file.name, handle, "text/markdown")},
                )
        else:
            response = client.get(f"{base}/v1/university-ingestions/{args.run_id}")
    response.raise_for_status()
    print(json.dumps(response.json(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
