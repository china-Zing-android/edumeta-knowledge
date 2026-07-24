Status: review

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

- 345 `passed`: allowed for default batch ingestion.
- 16 `needs_review`: schema-valid but fewer than five parsed catalog entries.
- 78 `failed`: no publishable catalog/date structure.
- Import requires the current Markdown SHA-256 to match the committed passed preflight result.

## Delivered

- `scripts/university_md_batch.py`: manifest, preflight, sequential ingest, polling, filters, dry-run, and resumable state.
- `scripts/import_universities.sh`: one-command Docker entry point.
- Read-only raw-data bind mount and persistent `batch_import_state` Docker volume.
- Parser support for unnumbered catalog tables, relative URLs, table school/department columns, localized dates, and duplicate structured entries.
- Dataset README and operations runbook.
- Per-university pre/post Parser compatibility results and a Chinese ingestion-readiness report separating technical ingestion from MIT-level release acceptance.

## Verification

- Full Python suite: 188 passed, 7 skipped, 11 subtests passed.
- Full preflight: 345 passed, 16 needs_review, 78 failed.
- Dry-run selection with country/limit returns the expected passed IDs.
- Fake HTTP lifecycle verifies create -> published -> repeated upload unchanged.
- No source file exceeds GitHub's per-file size limit; no credential pattern was found.
- Pre-upgrade comparison: 210 direct technical passes, 135 newly passing after generic Parser upgrades, 16 conditional reviews, and 78 blocked.
- Live post-ingestion student QA against `http://100.74.163.113:8000`: 30 cases x 5 runs, 22/30 strict pass, no nondeterminism, L1 HTTP p95 153.490 ms. Accuracy and source-URL quality do not pass release criteria; detailed report at `qa/reports/live-batch-student-qa-2026-07-24.md`.

## Current Risks

- Generic Markdown Parser accepts summary/category/policy rows as catalog entries in some schools.
- URL canonicalization can concatenate a base domain with an already host-like URL, yielding unusable double-domain source URLs.
- Retrieval ranking can return a minor, joint degree, or unrelated entry for a requested degree level.
- Batch `passed` remains a technical ingestion status, not MIT-level content acceptance.

## Runtime Command

```bash
./scripts/import_universities.sh --dry-run --country US --limit 5
./scripts/import_universities.sh --country US --limit 5
```

Set `WEKNORA_IMPORT_ENABLED=false` before L1 batch ingestion. The default command does not import failed, needs-review, duplicate, or hash-mismatched documents.
