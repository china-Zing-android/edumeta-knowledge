Status: done

# MD-First Discovery Context Handoff

## Goal

Add a small, long-lived challenge slice where university/program discovery returns MD-derived context and exploration topics, while WeKnora is used only for explicitly requested detail that L1 cannot answer.

## Plan

- `docs/plans/2026-07-16-md-first-discovery-context-challenge.md`

## Locked Boundaries

- Keep PostgreSQL, OpenSearch, external WeKnora, Fast Router, and one thin TypeScript MCP tool.
- Add one versioned `entity_contexts` projection and one OpenSearch alias.
- Discovery is MD-first and never calls WeKnora.
- Facts use Fact Store first; explicit missing detail may use scoped WeKnora.
- No graph database, Redis, vector database, runtime LLM, answer generation, ranking, or new MCP tools.
- MIT is the challenge acceptance dataset; the schema and builder remain adapter-neutral.
- Deterministic composition is allowed, but raw course codes must be paired with human-readable names and sourced relationship explanations.
- Agents retain multi-turn scope and pass it back in request context; Fast Router stays stateless.
- Review-required/conflicting facts return raw values plus warnings and do not automatically trigger WeKnora.
- Agent presentation follows direct answer -> context -> related entities -> available topics without Router prose generation.

## Current State

- Task 2 complete: `entity_contexts` schema validation, cross-reference gate, versioned PostgreSQL persistence, context diff, and no-WeKnora-reimport behavior are implemented.
- PostgreSQL migrations through `007_entity_contexts.sql` are applied to the local Compose database.
- Task 3 complete: `l1_entity_contexts_current` publishes 158 MIT contexts; live OpenSearch publish verified with existing index counts unchanged.
- Task 4 complete: conservative `QueryPlan`, fourth `_msearch` projection, response `context`, single/multi-entity composition, and strict discovery/fact/detail WeKnora gate are implemented.
- Real OpenSearch checks on July 16, 2026: MIT/Economics/tuition discovery and fact requests completed in roughly 20-62ms L1 time with `weknora_ms=0`.
- Focused Task 4 verification: 17 passed; only the existing Starlette/httpx deprecation warning remains.

## Next Step

Human QA can proceed using `qa/manual/md-first-l1-weknora-qa-guide.md`. The MCP endpoint is unchanged; start a new Agent session or reconnect MCP to reload the updated tool description.

## Final Verification

- Python: 171 passed, 11 subtests passed.
- TypeScript Gateway: 8 passed.
- HTTP challenge: 9 cases x 5 runs passed; L1 p95 65.725ms; L1+WeKnora p95 692.024ms.
- MCP benchmark: 50 runs passed; p95 32.750ms.
- WeKnora-disabled challenge: 6 cases x 5 runs passed; L1 p95 25.897ms.
- Runtime: five aliases, five current schools, 169/169 current sources and success jobs aligned, all Compose services healthy.
- Acceptance report: `qa/reports/md-first-discovery-context-acceptance-2026-07-16.md`.

## Gate A Result

- Added shared deterministic entity-context builder and JSON schema.
- Generated `data/challenge/md-first-discovery/mit/entity_contexts.jsonl`: 1 university + 157 program contexts.
- 14-1 Economics includes readable labels and deterministic links to 6-14 and 14-2.
- Current MIT MD does not contain qualitative 14-1 curriculum/strength content; the projection must not invent it.
- Verification: 146 passed, 7 skipped, 8 subtests passed.
