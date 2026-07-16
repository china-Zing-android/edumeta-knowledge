Status: done

# Retrieval Quality And One-Command Deploy Handoff

## Goal

Fix the systemic retrieval/Agent issues revealed by human QA, then make a fresh GitHub clone deploy a usable L1 stack with one Docker Compose command.

## Confirmed Root Causes

- Fact/source lookup uses URL substring matching before exact entity scope, so Economics also returns DEDP.
- Query planning gives fact terms precedence over explicit deep requests; Agent-expanded materials queries containing TOEFL/IELTS incorrectly stay on L1.
- Auto direction treats any discipline phrase as upward search before respecting a named known university.
- Agent rewrites user questions and may add topics not requested; MCP needs server instructions to pass the original question verbatim and distinguish facts from inference.
- Fresh Compose creates empty PostgreSQL/OpenSearch because there is no migration/data/index bootstrap service.

## Constraints

- No runtime LLM, Redis, graph DB, or Gateway business logic.
- Scope resolution remains OpenSearch-based and deterministic.
- PostgreSQL remains control plane; Fast Router hot path does not query it.
- WeKnora remains optional for L1 startup.

## Current Verification Baseline

- Python 171 passed, TypeScript 8 passed before this task.
- Five current schools and 169 source/job audit pairs.
- Git is not initialized. GitHub CLI is authenticated as `china-Zing-android` with repo scope.

## Delivered

- Detail intent now takes precedence over incidental fact terms, including Agent-expanded materials queries containing TOEFL/IELTS/GRE.
- Auto direction resolves a known university first and requires explicit school-list wording for upward search.
- Program context triggers an exact `source_id` scoped second OpenSearch query for facts and sources, preventing cross-program contamination.
- Materials Science no longer collides with application-material intent; ingested university aliases are cached for runtime resolution; invalid explicit university scope cannot broaden to range search.
- Bootstrap PostgreSQL verification counts only the current school version, so retained historical versions do not block later deployments.
- MCP initialization instructs Agents to pass the original question verbatim, avoid adding topics, preserve scope, distinguish context from evidence, and avoid unsupported qualitative inference.
- Root `compose.yaml` starts PostgreSQL, OpenSearch, an idempotent bootstrap gate, Fast Router, and the TypeScript MCP Gateway with one command.
- Fresh volumes and a repeated bootstrap both passed for five schools; Fast Router and MCP reached healthy state.

## Verification

- Python: 177 passed, 7 skipped, 11 subtests passed.
- TypeScript Gateway: 9 passed.
- Fresh Compose bootstrap: exit 0; version cache size 5.
- Tuition returned only tuition; Economics deadline returned only the Economics fact source; materials + TOEFL/IELTS/GRE remained `stage=detail` and degraded explicitly without WeKnora.
- Production-configured local Compose returned five EECS-only WeKnora evidence rows for the materials query; L1 was about 0.2 seconds and the external WeKnora call about 0.9 seconds.

## Residual Boundary

- WeKnora deep evidence requires deployment-specific credentials in an ignored `.env` file.
- `context.related_entities` may mention a related program, but the Agent must not present it as part of the direct fact answer.
