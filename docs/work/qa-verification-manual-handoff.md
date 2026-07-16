Status: done

# QA Verification Manual Handoff

## Goal

Provide an objective multi-university QA sheet, independent review key, and an executable operations manual for HTTP, MCP/Agent, L2 readiness, incremental MD, PostgreSQL, and per-university WeKnora KB validation.

## Delivered

- `qa/manual/multikb-qa-question-sheet-v1.md`
- `qa/manual/multikb-qa-review-key-v1.md`
- `docs/operations/multikb-testing-and-verification-runbook.md`
- Linked the existing short manual to the full runbook.

## Current Baseline

- Compose services healthy on HTTP `8000` and MCP `8765/mcp`.
- D01 about 62 ms; upward CS about 25 ms; California range about 32 ms.
- MIT EECS L2 returned scoped evidence in about 692 ms.
- Caltech CS PhD and Duke CS MS L2 remain known diagnostic failures.
- L2 formal acceptance requires the exact current source to have `weknora_import_status=success`.

## Verification

Commands and field names were checked against the live CLI, FastAPI contract, PostgreSQL schema, compose file, and current runtime responses on 2026-07-16.

`scripts/retrieval_benchmark.py` passed 9 cross-university cases across 5 runs with no failures or nondeterministic responses. Observed HTTP p95: L1 `28.783 ms`, upward `12.055 ms`, range `14.2 ms`. Report: `qa/reports/cross-university-manual-baseline.json`.

Codex global MCP `edumeta-local` was added at `http://127.0.0.1:8765/mcp`, restricted to `retrieve_university_knowledge`, and configured with approval mode `approve`. A fresh `codex exec` session completed a real MIT Economics tool call and returned `mode=l1`, `Economics / 14-1`, `total_ms=28.396`.
