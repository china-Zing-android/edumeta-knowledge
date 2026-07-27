Status: done

# Batch University Markdown Ingestion Handoff

## Goal

Add the 2026-07 university Markdown batch to the repository and provide a gated, resumable one-command path for incremental L1 ingestion while WeKnora URL imports are paused.

## Dataset

- Source directory: `data/raw-md/universities/`.
- 448 Markdown documents, approximately 22 MB.
- Country counts: US 242, UK 98, CA 48, AU 39, IE 8, SG 7, NZ 5, CH 1.
- Manifest resolves 9 duplicate documents and enables 439 university identities.
- Cross-country acronym collisions are scoped, including `us_smu` and `sg_smu`.

## Quality Gate

- Ruleset `2026-07-27.1`: 276 `passed`, 75 `needs_review`, 88 `failed` across 439 enabled universities.
- Five generic issue classes are gated: invalid entities, URL integrity, degree consistency, completeness/source specificity, and retrieval regression.
- Import requires the current Markdown SHA-256 to match the committed passed preflight result.
- Pre/post audit results persist in `ingestion_runs.quality_audits`; post-index failure leaves the previous current version active.

## Delivered

- `scripts/university_md_batch.py`: manifest, preflight, sequential ingest, polling, filters, dry-run, and resumable state.
- `scripts/import_universities.sh`: one-command Docker entry point.
- Read-only raw-data bind mount and persistent `batch_import_state` Docker volume.
- Parser support for unnumbered catalog tables, relative URLs, table school/department columns, localized dates, and duplicate structured entries.
- Dataset README and operations runbook.
- Per-university pre/post Parser compatibility results and a Chinese ingestion-readiness report separating technical ingestion from MIT-level release acceptance.
- Versioned quality rules, structured audit schema, pre-publish static gate, staged OpenSearch post-index probes, and ingestion audit persistence.
- Generic fixes for false table headers, full/bare/relative URL ordering, BA/BS/Minor identity, hard degree filters, catalog/context ownership, and discipline over-expansion.
- Resumable batch state now invalidates on Markdown hash or quality-ruleset changes, so previously published schools are re-imported after parser/audit upgrades.
- Resumable state and ingestion identity include parser contract version, so unchanged Markdown is reprocessed after parser semantics change.
- Explicit dry-run/apply quarantine command removes previously published but now unverified schools from the current retrieval set without deleting history.
- PostgreSQL staging uses `COPY`, promotion uses pipeline mode, and successful runs delete their staging copies in the same transaction.
- Migration `010_prune_published_ingestion_records.sql` removes historical staging copies for already published runs; failed-run staging remains available for diagnosis.
- PostgreSQL receives 256 MB Compose shared memory so vacuuming ingestion tables does not exceed Docker's default 64 MB `/dev/shm`.

## Verification

- Full Python suite: 231 passed, 7 skipped, 15 subtests passed before the final Compose shared-memory assertion; the Compose test file then passed 7/7.
- TypeScript Tool Gateway: 9 tests passed after typecheck and build.
- Full preflight: 276 passed, 75 needs_review, 88 failed.
- Dry-run selection with country/limit returns the expected passed IDs.
- Fake HTTP lifecycle verifies create -> published -> repeated upload unchanged.
- No source file exceeds GitHub's per-file size limit; no credential pattern was found.
- Final local Compose images build and start successfully with persistent volumes preserved.
- Pre-upgrade comparison: 210 direct technical passes, 135 newly passing after generic Parser upgrades, 16 conditional reviews, and 78 blocked.
- Live post-ingestion student QA against `http://100.74.163.113:8000`: 30 cases x 5 runs, 22/30 strict pass, no nondeterminism, L1 HTTP p95 153.490 ms. Accuracy and source-URL quality do not pass release criteria; detailed report at `qa/reports/live-batch-student-qa-2026-07-24.md`.
- Post-audit QA uses the same 30 question texts in `qa/live-batch-student-qa-post-audit-2026-07-27.jsonl`. Princeton, Melbourne, and Toronto now expect `not_found` because their Markdown fails the completeness gate and must be quarantined. The original suite remains unchanged as the 22/30 baseline.
- `qa/` is mounted read-only into Fast Router so the server can run the 30-question benchmark inside Docker without installing host Python packages.
- Batch ingestion now reports upload acceptance, run ID, status transitions, a 10-second heartbeat, completion, and elapsed time.
- Compose bootstrap is migration-only. It no longer republishes `data/normalized` fixtures, so restarts cannot bypass ingestion quality gates or restore quarantined schools.
- Local final ingestion: 276/276 quality-passed universities active, 0 non-terminal runs, and no successful-run staging growth.
- Local final QA: 30 cases x 5 runs passed, no failures or nondeterminism; L1 p95 108.460 ms, upward p95 134.003 ms, range p95 409.415 ms.
- Post-PostgreSQL-recreate smoke: 30/30 passed; L1 p95 72.242 ms, upward p95 44.131 ms, range p95 66.040 ms.

## Current Risks

- `needs_review` schools are structurally parseable but are not automatically publishable, mainly because their catalog uses one generic homepage source.
- 88 blocked schools require better Markdown/source structure; they must not receive school-specific parser exceptions.
- Batch `passed` remains an L1 structural/retrieval status, not MIT-level factual acceptance.
- Very large catalogs remain ingestion long-tail cases, but they expose progress and complete within the 1200-second operational ceiling; retrieval latency is unaffected.

## Runtime Command

```bash
./scripts/import_universities.sh --dry-run --country US --limit 5
./scripts/import_universities.sh --country US --limit 5
```

Set `WEKNORA_IMPORT_ENABLED=false` before L1 batch ingestion. The default command does not import failed, needs-review, duplicate, or hash-mismatched documents.

After deployment, run quarantine in dry-run/apply mode, re-import all passed schools with a 1200-second per-school ceiling, then execute the post-audit 30-question suite. Do not delete Docker volumes.
