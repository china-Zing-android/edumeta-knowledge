#!/usr/bin/env bash
set -euo pipefail

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

exec docker compose exec -T fast-router \
  python /app/scripts/university_md_batch.py ingest \
  --data-root /app/data/raw-md/universities \
  --manifest /app/data/raw-md/universities/manifest.jsonl \
  --preflight /app/data/raw-md/universities/preflight-results.jsonl \
  --state /app/data/import-state/university-md-batch.jsonl \
  "$@"
