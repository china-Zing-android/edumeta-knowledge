-- =============================================================================
-- L1 + WeKnora Retrieval — PostgreSQL Control Plane
-- Plan §3 Data Control Plane. This file REPLACES the old duplicated control-plane
-- schema (qa_cases, qa_reviews, url_manifest, JSON-array relational links).
--
-- Migration policy (Plan §12 Assumptions): this is an unreleased project with no
-- production migration compatibility requirement. The local dev PostgreSQL volume
-- is reset once; this single schema file is the source of truth.
--
-- Eleven authoritative tables:
--   universities        stable identity and range-search metadata
--   school_versions     staging/current dataset version per university + publication state
--   ingestion_runs      one row per uploaded MD (input hash + stage failures)
--   ingestion_records   validated staging JSON records for the run
--   catalog_entries     authoritative normalized catalog records
--   catalog_entry_disciplines controlled taxonomy relationships for upward/range retrieval
--   source_registry     one canonical URL per university/source with WeKnora IDs + lifecycle
--   source_entry_links  many-to-many association between sources and catalog entries
--   fact_store          authoritative raw/normalized facts + review/conflict state
--   entity_contexts     versioned MD-first discovery projection
--   weknora_import_jobs asynchronous import/poll/retry state (one MD -> one KB)
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Enums: status/state domains used as CHECK constraints on TEXT columns so the
-- schema stays portable across engines while still enforcing the value domain.
-- -----------------------------------------------------------------------------

-- -----------------------------------------------------------------------------
-- universities: stable identity is created before parsing a new school's MD.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS universities (
  university_id       TEXT PRIMARY KEY,
  university_name     TEXT NOT NULL,
  aliases             JSONB NOT NULL DEFAULT '[]'::jsonb,
  country_code        TEXT,
  region              TEXT,
  school_tier         TEXT NOT NULL,
  weknora_knowledge_base_id TEXT,
  weknora_knowledge_base_name TEXT,
  status              TEXT NOT NULL DEFAULT 'pending',
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT chk_university_tier CHECK (school_tier IN ('core', 'non_core')),
  CONSTRAINT chk_university_status CHECK (status IN ('pending', 'active', 'failed'))
);

CREATE INDEX IF NOT EXISTS idx_universities_range
  ON universities (country_code, region, school_tier, status);

-- -----------------------------------------------------------------------------
-- school_versions: staging/current dataset version per university + publication state.
-- Exactly one row per (university_id) is "current" at any time, enforced by a
-- partial unique index. Old versions are retained for rollback.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS school_versions (
  version_id          TEXT NOT NULL,
  university_id       TEXT NOT NULL,
  dataset_version     TEXT NOT NULL,          -- e.g. mit_20260704_v2
  publication_state   TEXT NOT NULL,          -- staging | current | superseded | failed
  input_hash          TEXT NOT NULL,          -- sha256 of the uploaded MD
  record_counts       JSONB NOT NULL DEFAULT '{}'::jsonb,  -- {catalog_entries, fact_store, source_registry, ...}
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  published_at        TIMESTAMPTZ,
  superseded_at       TIMESTAMPTZ,
  PRIMARY KEY (university_id, version_id),
  CONSTRAINT fk_school_university
    FOREIGN KEY (university_id) REFERENCES universities(university_id),
  CONSTRAINT chk_school_pub_state
    CHECK (publication_state IN ('staging', 'current', 'superseded', 'failed'))
);

-- At most one current version per university — the core current-version integrity.
CREATE UNIQUE INDEX IF NOT EXISTS uq_school_versions_current
  ON school_versions (university_id)
  WHERE publication_state = 'current';

CREATE INDEX IF NOT EXISTS idx_school_versions_university
  ON school_versions (university_id, publication_state);

-- -----------------------------------------------------------------------------
-- ingestion_runs: one row per uploaded MD, including input hash and stage failures.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ingestion_runs (
  run_id              TEXT PRIMARY KEY,       -- ing_xxx
  university_id       TEXT NOT NULL,
  school_tier         TEXT NOT NULL,          -- core | non_core
  operation           TEXT NOT NULL DEFAULT 'update', -- create | update | unchanged
  version_id          TEXT NOT NULL,          -- the school_version this run targets
  input_hash          TEXT NOT NULL,          -- sha256 of the MD, used to detect unchanged input
  weknora_knowledge_base_id TEXT,
  weknora_kb_operation TEXT NOT NULL DEFAULT 'reuse', -- create | reuse | explicit
  status              TEXT NOT NULL,          -- accepted|unchanged|validating|publishing|published|failed
  stage_failures      JSONB NOT NULL DEFAULT '[]'::jsonb,
  error_message       TEXT,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT chk_run_status
    CHECK (status IN ('accepted', 'unchanged', 'validating', 'publishing', 'published', 'failed')),
  CONSTRAINT chk_run_tier
    CHECK (school_tier IN ('core', 'non_core')),
  CONSTRAINT chk_run_operation
    CHECK (operation IN ('create', 'update', 'unchanged')),
  CONSTRAINT chk_run_weknora_kb_operation
    CHECK (weknora_kb_operation IN ('create', 'reuse', 'explicit')),
  CONSTRAINT fk_run_version
    FOREIGN KEY (university_id, version_id) REFERENCES school_versions(university_id, version_id)
);

CREATE INDEX IF NOT EXISTS idx_ingestion_runs_university
  ON ingestion_runs (university_id, status);

-- -----------------------------------------------------------------------------
-- ingestion_records: validated staging JSON records for the run.
-- A run's records are stored as authoritative JSON before publication so the
-- validation/diff/publish flow can operate on staging data.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ingestion_records (
  run_id              TEXT NOT NULL REFERENCES ingestion_runs(run_id) ON DELETE CASCADE,
  entity_name         TEXT NOT NULL,          -- catalog_entries | fact_store | source_registry | source_entry_links
  record_id           TEXT NOT NULL,          -- entry_id / fact_id / source_id / link_id
  university_id       TEXT NOT NULL,
  record_hash         TEXT NOT NULL,          -- normalized content hash for diffing
  record              JSONB NOT NULL,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (run_id, entity_name, record_id)
);

CREATE INDEX IF NOT EXISTS idx_ingestion_records_entity
  ON ingestion_records (university_id, entity_name);

CREATE INDEX IF NOT EXISTS idx_ingestion_records_hash
  ON ingestion_records (record_hash);

-- -----------------------------------------------------------------------------
-- source_registry: one canonical URL per university/source with WeKnora IDs and
-- lifecycle state. The URL lifecycle master table. entry_ids are NO LONGER a
-- JSON array here — the many-to-many lives in source_entry_links.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS source_registry (
  source_id           TEXT NOT NULL,          -- stable across versions: university_id + canonical_url
  university_id       TEXT NOT NULL,
  version_id          TEXT NOT NULL,          -- which school_version introduced/last published it
  program_id          TEXT,
  source_url          TEXT,
  canonical_url       TEXT NOT NULL,
  url_type            TEXT NOT NULL,
  topics              JSONB NOT NULL DEFAULT '[]'::jsonb,
  official_source     BOOLEAN NOT NULL DEFAULT false,
  priority            INTEGER NOT NULL DEFAULT 1,
  content_hash        TEXT,
  weknora_content_hash TEXT,
  crawl_status        TEXT NOT NULL DEFAULT 'pending',
  parser_status       TEXT NOT NULL DEFAULT 'pending',
  weknora_import_status TEXT NOT NULL DEFAULT 'pending',
  weknora_knowledge_base_id TEXT,             -- KB this URL lives in (one MD -> one KB)
  weknora_knowledge_id TEXT,
  weknora_document_id TEXT,
  weknora_chunk_ids JSONB NOT NULL DEFAULT '[]'::jsonb,
  weknora_tag_ids JSONB NOT NULL DEFAULT '[]'::jsonb,
  weknora_import_job_id TEXT,
  status              TEXT NOT NULL DEFAULT 'active',   -- active | inactive | superseded
  capture_date        DATE NOT NULL,
  last_verified       DATE NOT NULL,
  dataset_version     TEXT NOT NULL,
  source_version      TEXT,
  error_message       TEXT,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (university_id, version_id, source_id),
  CONSTRAINT chk_source_status
    CHECK (status IN ('active', 'inactive', 'superseded')),
  CONSTRAINT fk_source_version
    FOREIGN KEY (university_id, version_id) REFERENCES school_versions(university_id, version_id)
);

-- Canonical URL uniqueness WITHIN a university (Plan §3 constraint).
CREATE UNIQUE INDEX IF NOT EXISTS uq_source_registry_canonical
  ON source_registry (university_id, version_id, canonical_url);

CREATE INDEX IF NOT EXISTS idx_source_registry_university
  ON source_registry (university_id, status);

CREATE INDEX IF NOT EXISTS idx_source_registry_weknora_kb
  ON source_registry (weknora_knowledge_base_id)
  WHERE weknora_knowledge_base_id IS NOT NULL;

-- -----------------------------------------------------------------------------
-- catalog_entries: authoritative normalized catalog records.
-- references source_registry; many-to-many links live in source_entry_links.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS catalog_entries (
  entry_id            TEXT NOT NULL,
  university_id       TEXT NOT NULL,
  version_id          TEXT NOT NULL,
  program_id          TEXT,
  school              TEXT NOT NULL,
  department          TEXT NOT NULL,
  level               TEXT NOT NULL,          -- undergraduate | graduate
  degree_level        TEXT NOT NULL,          -- SB | MEng | SM | PhD ...
  degree_full_name    TEXT,
  course_code         TEXT,
  program_name        TEXT NOT NULL,
  canonical_program_name TEXT,
  aliases             JSONB NOT NULL DEFAULT '[]'::jsonb,        -- text list, not a relational link
  source_id           TEXT NOT NULL,
  source_url          TEXT NOT NULL,
  topics              JSONB NOT NULL DEFAULT '[]'::jsonb,
  search_text         TEXT NOT NULL,
  cross_school        BOOLEAN NOT NULL DEFAULT false,
  cross_school_names  JSONB NOT NULL DEFAULT '[]'::jsonb,        -- text list
  raw_section_path    TEXT,
  capture_date        DATE NOT NULL,
  dataset_version     TEXT NOT NULL,
  source_version      TEXT,
  status              TEXT NOT NULL DEFAULT 'active',
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (university_id, version_id, entry_id),
  CONSTRAINT chk_catalog_status
    CHECK (status IN ('active', 'inactive', 'superseded')),
  CONSTRAINT fk_catalog_version
    FOREIGN KEY (university_id, version_id) REFERENCES school_versions(university_id, version_id),
  CONSTRAINT fk_catalog_source
    FOREIGN KEY (university_id, version_id, source_id)
    REFERENCES source_registry(university_id, version_id, source_id)
);

CREATE INDEX IF NOT EXISTS idx_catalog_university_level
  ON catalog_entries (university_id, level, degree_level);

CREATE INDEX IF NOT EXISTS idx_catalog_source
  ON catalog_entries (source_id);

-- -----------------------------------------------------------------------------
-- catalog_entry_disciplines: controlled taxonomy relationships. One catalog
-- entry may belong to several disciplines without duplicating the entry.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS catalog_entry_disciplines (
  link_id             TEXT NOT NULL,
  university_id       TEXT NOT NULL,
  version_id          TEXT NOT NULL,
  entry_id            TEXT NOT NULL,
  discipline_id       TEXT NOT NULL,
  discipline_label    TEXT NOT NULL,
  match_method        TEXT NOT NULL DEFAULT 'rule',
  confidence          DOUBLE PRECISION NOT NULL DEFAULT 1,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (university_id, version_id, link_id),
  UNIQUE (university_id, version_id, entry_id, discipline_id),
  CONSTRAINT fk_discipline_entry
    FOREIGN KEY (university_id, version_id, entry_id)
    REFERENCES catalog_entries(university_id, version_id, entry_id)
);

CREATE INDEX IF NOT EXISTS idx_catalog_disciplines_lookup
  ON catalog_entry_disciplines (discipline_id, university_id, version_id);

-- -----------------------------------------------------------------------------
-- source_entry_links: many-to-many association between sources and catalog entries
-- (and facts). Replaces the old JSON-array entry_ids/weknora_chunk_ids pattern.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS source_entry_links (
  link_id             TEXT NOT NULL,          -- deterministic: source_id + target
  source_id           TEXT NOT NULL,
  target_entity       TEXT NOT NULL,          -- catalog_entry | fact
  target_id           TEXT NOT NULL,          -- entry_id / fact_id
  university_id       TEXT NOT NULL,
  version_id          TEXT NOT NULL,
  topics              JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (university_id, version_id, link_id),
  CONSTRAINT chk_link_target
    CHECK (target_entity IN ('catalog_entry', 'fact')),
  UNIQUE (university_id, version_id, source_id, target_entity, target_id),
  CONSTRAINT fk_link_source
    FOREIGN KEY (university_id, version_id, source_id)
    REFERENCES source_registry(university_id, version_id, source_id)
);

CREATE INDEX IF NOT EXISTS idx_links_source
  ON source_entry_links (source_id);

CREATE INDEX IF NOT EXISTS idx_links_target
  ON source_entry_links (target_entity, target_id);

-- -----------------------------------------------------------------------------
-- fact_store: authoritative raw/normalized facts and review/conflict state.
-- weknora_chunk_ids relationship is NOT a JSON array link here; evidence linkage
-- is captured via evidence_ids (fact-evidence, a documented fact attribute, not
-- a source↔entity relational link) — kept as JSONB per Plan §3 wording.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS fact_store (
  fact_id             TEXT NOT NULL,
  university_id       TEXT NOT NULL,
  version_id          TEXT NOT NULL,
  program_id          TEXT,
  entry_id            TEXT,
  fact_type           TEXT NOT NULL,          -- deadline | application_fee | test_score | ...
  fact_key            TEXT NOT NULL,
  raw_value           TEXT NOT NULL,
  normalized_value    JSONB,
  unit                TEXT,
  currency            TEXT,
  admission_cycle     TEXT,
  term                TEXT,
  source_id           TEXT NOT NULL,
  source_url          TEXT NOT NULL,
  evidence_ids        JSONB NOT NULL DEFAULT '[]'::jsonb,        -- documented fact attribute
  capture_date        DATE NOT NULL,
  dataset_version     TEXT NOT NULL,
  source_version      TEXT,
  confidence          DOUBLE PRECISION NOT NULL DEFAULT 1,
  review_status       TEXT NOT NULL,          -- approved | review_required | rejected
  conflict_status     TEXT NOT NULL,          -- none | conflicted
  status              TEXT NOT NULL DEFAULT 'active',
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (university_id, version_id, fact_id),
  CONSTRAINT chk_fact_review
    CHECK (review_status IN ('approved', 'review_required', 'rejected')),
  CONSTRAINT chk_fact_conflict
    CHECK (conflict_status IN ('none', 'conflicted')),
  CONSTRAINT chk_fact_status
    CHECK (status IN ('active', 'inactive', 'superseded')),
  CONSTRAINT fk_fact_version
    FOREIGN KEY (university_id, version_id) REFERENCES school_versions(university_id, version_id),
  CONSTRAINT fk_fact_source
    FOREIGN KEY (university_id, version_id, source_id)
    REFERENCES source_registry(university_id, version_id, source_id)
);

CREATE INDEX IF NOT EXISTS idx_fact_store_lookup
  ON fact_store (university_id, fact_type, fact_key);

CREATE INDEX IF NOT EXISTS idx_fact_store_review
  ON fact_store (review_status, conflict_status);

-- -----------------------------------------------------------------------------
-- entity_contexts: versioned MD-first discovery projection. This is a compact
-- materialized view of catalog/fact/source relationships, not a graph database
-- and not generated prose.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS entity_contexts (
  context_id          TEXT NOT NULL,
  university_id       TEXT NOT NULL,
  version_id          TEXT NOT NULL,
  entity_type         TEXT NOT NULL,
  entity_id           TEXT NOT NULL,
  entry_id            TEXT,
  title               TEXT NOT NULL,
  display_label       TEXT NOT NULL,
  attributes          JSONB NOT NULL DEFAULT '{}'::jsonb,
  highlights          JSONB NOT NULL DEFAULT '[]'::jsonb,
  sample_children     JSONB NOT NULL DEFAULT '[]'::jsonb,
  related_entities    JSONB NOT NULL DEFAULT '[]'::jsonb,
  available_topics    JSONB NOT NULL DEFAULT '[]'::jsonb,
  source_ids          JSONB NOT NULL DEFAULT '[]'::jsonb,
  md_section_paths    JSONB NOT NULL DEFAULT '[]'::jsonb,
  dataset_version     TEXT NOT NULL,
  status              TEXT NOT NULL DEFAULT 'active',
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (university_id, version_id, context_id),
  CONSTRAINT chk_entity_context_type CHECK (entity_type IN ('university', 'program')),
  CONSTRAINT chk_entity_context_status CHECK (status IN ('active', 'inactive', 'superseded')),
  CONSTRAINT fk_entity_context_version
    FOREIGN KEY (university_id, version_id) REFERENCES school_versions(university_id, version_id),
  CONSTRAINT fk_entity_context_entry
    FOREIGN KEY (university_id, version_id, entry_id)
    REFERENCES catalog_entries(university_id, version_id, entry_id)
);

CREATE INDEX IF NOT EXISTS idx_entity_context_lookup
  ON entity_contexts (university_id, entity_type, entity_id, status);

-- -----------------------------------------------------------------------------
-- weknora_import_jobs: asynchronous import/poll/retry state.
-- Each uploaded MD creates one knowledge base in WeKnora; this table is the job
-- queue (claimed via FOR UPDATE SKIP LOCKED, Plan §6) AND the persistent
-- knowledge/document/chunk/tag/status/retry/failure state.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS weknora_import_jobs (
  job_id              TEXT PRIMARY KEY,
  source_id           TEXT NOT NULL,
  run_id              TEXT REFERENCES ingestion_runs(run_id),
  university_id       TEXT NOT NULL,
  version_id          TEXT NOT NULL,
  knowledge_base_id   TEXT,                   -- the KB this import created/updates (one MD -> one KB)
  knowledge_id        TEXT,
  document_id         TEXT,
  chunk_ids           JSONB NOT NULL DEFAULT '[]'::jsonb,   -- chunk references (lifecycle state, not a relational link)
  tags                JSONB NOT NULL DEFAULT '[]'::jsonb,
  status              TEXT NOT NULL,          -- queued | running | success | failed | superseded
  retry_count         INTEGER NOT NULL DEFAULT 0,
  next_attempt_at     TIMESTAMPTZ,
  started_at          TIMESTAMPTZ,
  finished_at         TIMESTAMPTZ,
  failure_reason      TEXT,
  source_url          TEXT NOT NULL,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT chk_job_status
    CHECK (status IN ('queued', 'running', 'success', 'failed', 'superseded')),
  CONSTRAINT fk_job_source
    FOREIGN KEY (university_id, version_id, source_id)
    REFERENCES source_registry(university_id, version_id, source_id)
);

-- Job-queue claim index: skip-locked claim over queued/running rows.
CREATE INDEX IF NOT EXISTS idx_weknora_jobs_claim
  ON weknora_import_jobs (status, next_attempt_at)
  WHERE status IN ('queued', 'running');

CREATE INDEX IF NOT EXISTS idx_weknora_jobs_source
  ON weknora_import_jobs (source_id);

CREATE UNIQUE INDEX IF NOT EXISTS uq_weknora_jobs_active_source
  ON weknora_import_jobs (university_id, knowledge_base_id, source_id)
  WHERE status IN ('queued', 'running', 'success');

CREATE INDEX IF NOT EXISTS idx_weknora_jobs_university
  ON weknora_import_jobs (university_id, status);
