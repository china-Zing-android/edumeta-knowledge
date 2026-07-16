# Failure Analysis

Generated at: 2026-07-09T15:01:49.301170+00:00

## Release Blockers

### human_qa_review

- status 'not_ready' not in accepted statuses ['passed']
- human review file is missing or empty

### external_readiness

- status 'not_ready' not in accepted statuses ['ready']
- weknora: missing_config
- l0: missing_config
- langfuse: missing_config
- agent_mcp_sdk: missing_config

### external_live_smoke

- status 'not_ready' not in accepted statuses ['passed']
- weknora: WEKNORA_BASE_URL is required for real WeKnora import mode.
- l0: L0_API_BASE_URL is required.
- langfuse: LANGFUSE_HOST, LANGFUSE_PUBLIC_KEY, and LANGFUSE_SECRET_KEY are required.

## Human Review Failures

- human review file is missing or empty

## Required Next Evidence

- At least five normalized schools and successful batch validation/diff/index/WeKnora sync reports.
- Live WeKnora import/status/search, L0 resolve, Langfuse ingestion, and external MCP SDK smoke reports.
- `qa/human-reviews.jsonl` with passing human review coverage and failure attribution.
