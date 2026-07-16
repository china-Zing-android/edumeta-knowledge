Status: done

# Cross-University Retrieval Handoff

## Goal

Extend the completed L1 + WeKnora MIT slice with one production ingestion API and three retrieval directions over already-ingested universities: downward, range, and upward discipline-to-university search.

## Locked Boundaries

- Results include only universities already ingested into this system.
- No institutional ranking or external university discovery.
- Broad/range/upward search uses OpenSearch L1 only; WeKnora is used after university/source scope is selected.
- One MCP tool and one retrieval contract remain.
- University IDs are caller-supplied stable identifiers; the service auto-detects create versus update.
- Same-university updates upload a complete MD snapshot, not a patch fragment.

## Implementation

- Add authoritative `universities` and `catalog_entry_disciplines` control-plane tables.
- Add deterministic controlled discipline taxonomy and enrich every catalog entry.
- Add `POST /v1/university-ingestions` while retaining `/v1/ingestions` as a compatibility alias.
- Extend `/v1/retrieve` with `direction=auto|downward|range|upward` and structured filters.
- Add current-document markers to global OpenSearch indexes for cross-university queries.
- Return grouped university matches with the programs and sources that caused each match.

## Verification Target

- Existing MIT 30-case acceptance remains green.
- New API distinguishes new/update/unchanged university ingestion.
- “医学专业的院校有哪些？” returns only ingested universities with matching medicine/biomedical programs and source URLs.
- Country/tier/degree filters do not leak out-of-range universities.
- Broad search p95 remains below one second without WeKnora calls.

## Delivered State

- Preferred ingestion API: `POST /v1/university-ingestions` and `GET /v1/university-ingestions/{run_id}`; legacy `/v1/ingestions` remains an alias.
- Ingestion identity includes parser contract, full MD content, and caller-supplied university metadata.
- Caller metadata and parsed MD metadata are merged deterministically and published to PostgreSQL and OpenSearch.
- Nonterminal WeKnora imports survive school-version switches: successful sources are inherited; pending/running/failed sources receive a current-version continuation job carrying the existing knowledge ID.
- Release gate selects the latest MIT, cross-university, MCP, incremental, and runtime reports.

## Runtime Verification

Stanford was ingested through the production API as a genuine new university and then rebuilt through the corrected metadata/import-continuation contract.

```text
create run: ing_bfca8b4857d940e6b8463871a1100030
final update run: ing_f80d2055a72b4461824bdda452c68e1c
Stanford catalog entries: 12
Stanford discipline links: 15
Stanford sources: 15
Stanford current WeKnora success: 15/15
MIT current WeKnora success: 112/112
current universities: MIT, Stanford
```

Observed retrieval:

```text
“计算机专业的院校有哪些？” -> MIT + Stanford
“医学专业的院校有哪些？” -> MIT only
California range filter -> Stanford only
MCP upward smoke -> MIT + Stanford, total_ms=22.453, weknora_ms=0
```

Final verification on 2026-07-16:

```text
Python suite: 129 passed, 7 skipped
PostgreSQL integration: 11 passed
TypeScript Gateway: 8 passed
MIT acceptance: 30 cases x 5 runs, L1 p95 56.237ms, L1+L2 p95 592.516ms
Cross-university acceptance: 9 cases x 5 runs, upward p95 26.019ms, range p95 25.479ms
MCP benchmark: 50 runs, p95 24.417ms
Runtime Compose gate: passed, 2 current versions, 127/127 current sources imported
Release gate: passed, 5/5 gates
```

Reports:

- `qa/reports/retrieval-acceptance-2026-07-16.json`
- `qa/reports/cross-university-acceptance-2026-07-16.json`
- `qa/reports/mcp-benchmark-2026-07-16.json`
- `qa/reports/runtime-compose-2026-07-16.json`
- `qa/reports/release-gate-2026-07-16.json`

## Remaining Boundary

Harvard, Princeton, and Berkeley files remain synthetic pipeline seeds, not authoritative production datasets. Adding them uses the same full-snapshot API and requires objective source/content review; no architecture change or new MCP tool is required.
