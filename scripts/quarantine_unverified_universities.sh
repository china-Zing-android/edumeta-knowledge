#!/usr/bin/env bash
set -euo pipefail

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

exec docker compose exec -T fast-router \
  python /app/scripts/quarantine_unverified_universities.py \
  --preflight /app/data/raw-md/universities/preflight-results.jsonl \
  "$@"
