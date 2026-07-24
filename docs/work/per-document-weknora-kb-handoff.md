Status: done

# Per-Document WeKnora KB Handoff

## Goal

Move from one global WeKnora KB to one current KB per university full-snapshot MD. New universities create a KB automatically; same-university updates reuse it; uploads can explicitly select an existing KB or force a new KB.

## Locked Decisions

- Current ingestion remains one complete MD snapshot per `university_id`; patch fragments remain unsupported.
- Default behavior: reuse the university's bound KB, otherwise create one.
- `weknora_knowledge_base_id` explicitly selects/rebinds a target KB.
- `create_new_weknora_kb=true` creates and binds a new KB.
- Each source and import job carries its actual KB ID.
- `WEKNORA_KNOWLEDGE_BASE_ID` is legacy fallback only and is not required for normal multi-KB routing.
- `WEKNORA_KB_TEMPLATE_ID` optionally supplies configuration for newly created university KBs; template documents are not copied or searched.
- `WEKNORA_IMPORT_ENABLED=false` pauses the URL worker while preserving URL extraction, L1 publication, and queued jobs; setting it back to `true` resumes the backlog without another MD upload.
- WeKnora search groups scoped sources by KB ID; no global cross-KB search.
- MIT target KB: `1b91fcff-ce72-4e97-9de0-f23a8ba419d9`.
- Old KB content is retained and not deleted.

## Test Inputs

- `docs/测试文件/院校明细/ASU_知识库_完整深度数据_v2.md`
- `docs/测试文件/院校明细/Harvard_知识库_完整深度数据_v2.md`
- `docs/测试文件/院校明细/Caltech_知识库_完整深度数据_v2.md`
- `docs/测试文件/院校明细/Duke_知识库_完整深度数据_v2.md`

ASU is the scale case (more than 1,100 URLs); do not enqueue it during the first small-scope runtime test unless the smaller documents pass first.

## Constraints

- No credentials in source files.
- Keep one MCP tool and the existing retrieval contract.
- No L0, ranking, Redis, or new gateway business logic.
- KB creation uses the configured template KB settings.

## Next Step

Wait for remote WeKnora finalizing tasks, rerun `scripts/runtime_acceptance.py`, and run the full MIT L1+L2 acceptance suite when all current MIT sources are terminal success.

## Delivered

- Added persistent university-to-KB binding and per-ingestion `create/reuse/explicit` operation.
- Added multipart/CLI options:
  - `weknora_knowledge_base_id` / `--weknora-knowledge-base-id`
  - `create_new_weknora_kb` / `--create-new-weknora-kb`
- Added WeKnora KB validation/creation client. New KBs clone retrieval configuration from `WEKNORA_KB_TEMPLATE_ID`.
- Every source/job carries its actual KB ID. Worker tags, imports, polls, persists, and updates OpenSearch using the job KB.
- Deep search groups scoped sources by KB and calls each KB independently.
- Same-KB version updates inherit/continue knowledge IDs; switching KB reimports and does not inherit old-KB IDs.
- Worker claim order is oldest-update-first so long-running polls do not starve new URL submissions.
- Added `deep_v2` parser and `auto` adapter for the selected source documents.
- Empty optional fact indexes are valid during OpenSearch publication.

## Runtime Runs

```text
MIT explicit new KB:
  run_id=ing_d65e91838d3945c9943649076388cd28
  kb_id=1b91fcff-ce72-4e97-9de0-f23a8ba419d9
  catalog=157, sources=112, jobs=112

Caltech new KB:
  run_id=ing_db479812e7c94ee28157a2287c529e96
  kb_id=b9f8e394-f4c5-452f-834e-74b6d3cff46c
  catalog=78, sources=57, jobs=57

Duke new KB:
  run_id=ing_eebb22e3f03e4fb3aa47defd32ce0ff5
  kb_id=34c8210a-e34e-490e-afb6-611c3b3b52f8
  catalog=301, sources=22, jobs=22

Duke automatic reuse update:
  run_id=ing_c18b3418b3ec435c963a8fcfd2fb267a
  kb_operation=reuse
  carried knowledge IDs=22/22
```

ASU and Harvard were parsed and schema-validated but intentionally not queued during the small-scope test:

```text
ASU: catalog=1107, sources=1174
Harvard: catalog=180, sources=166
```

## Verification

```text
Python: 140 passed, 7 skipped, 8 subtests passed
PostgreSQL integration: 12 passed
TypeScript Gateway: 8 passed
Cross-university HTTP: 9 cases x 5 runs passed
MCP upward smoke: physical-science query returned caltech, duke, mit
MIT new-KB scoped search: 3 evidence chunks returned from Course 6-3 knowledge ID
Compose: postgres/opensearch/fast-router/tool-gateway healthy
Multi-KB configuration, import gate, and health semantics: 23 focused tests passed
```

Current remote state at the last runtime gate:

```text
current sources=206
success=33
running=173
worker alive, no worker error
runtime gate status=failed until remote finalizing completes
report=qa/reports/runtime-compose-multikb-2026-07-16.json
```
