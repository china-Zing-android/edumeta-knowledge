-- Markdown admin control plane: durable batches, source metadata, previews, and audit events.

CREATE TABLE IF NOT EXISTS ingestion_batches (
  batch_id            TEXT PRIMARY KEY,
  mode                TEXT NOT NULL,
  source_root_id      TEXT,
  source_relative_path TEXT,
  status              TEXT NOT NULL DEFAULT 'accepted',
  total_count         INTEGER NOT NULL DEFAULT 0,
  accepted_count      INTEGER NOT NULL DEFAULT 0,
  published_count     INTEGER NOT NULL DEFAULT 0,
  failed_count        INTEGER NOT NULL DEFAULT 0,
  unchanged_count     INTEGER NOT NULL DEFAULT 0,
  weknora_disabled_count INTEGER NOT NULL DEFAULT 0,
  rejected_count      INTEGER NOT NULL DEFAULT 0,
  rejected_items      JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT chk_ingestion_batch_mode CHECK (mode IN ('upload', 'directory')),
  CONSTRAINT chk_ingestion_batch_status CHECK (status IN ('accepted', 'processing', 'completed', 'partial', 'failed'))
);

ALTER TABLE ingestion_runs
  ADD COLUMN IF NOT EXISTS batch_id TEXT REFERENCES ingestion_batches(batch_id),
  ADD COLUMN IF NOT EXISTS source_filename TEXT,
  ADD COLUMN IF NOT EXISTS source_size_bytes BIGINT,
  ADD COLUMN IF NOT EXISTS source_relative_path TEXT,
  ADD COLUMN IF NOT EXISTS source_root_id TEXT,
  ADD COLUMN IF NOT EXISTS source_mode TEXT NOT NULL DEFAULT 'direct',
  ADD COLUMN IF NOT EXISTS requested_metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  ADD COLUMN IF NOT EXISTS force_publish_requested BOOLEAN NOT NULL DEFAULT false,
  ADD COLUMN IF NOT EXISTS force_publish_reason TEXT,
  ADD COLUMN IF NOT EXISTS weknora_error TEXT,
  ADD COLUMN IF NOT EXISTS diff_summary JSONB NOT NULL DEFAULT '{}'::jsonb,
  ADD COLUMN IF NOT EXISTS queue_claimed_at TIMESTAMPTZ,
  ADD COLUMN IF NOT EXISTS started_at TIMESTAMPTZ,
  ADD COLUMN IF NOT EXISTS finished_at TIMESTAMPTZ;

CREATE INDEX IF NOT EXISTS idx_ingestion_runs_batch
  ON ingestion_runs (batch_id, created_at);

CREATE INDEX IF NOT EXISTS idx_ingestion_runs_queue
  ON ingestion_runs (status, created_at)
  WHERE status = 'accepted';

CREATE TABLE IF NOT EXISTS admin_previews (
  preview_id          TEXT PRIMARY KEY,
  mode                TEXT NOT NULL,
  source_root_id      TEXT,
  source_relative_path TEXT,
  storage_dir         TEXT,
  items               JSONB NOT NULL DEFAULT '[]'::jsonb,
  status              TEXT NOT NULL DEFAULT 'ready',
  expires_at          TIMESTAMPTZ NOT NULL,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT chk_admin_preview_mode CHECK (mode IN ('upload', 'directory')),
  CONSTRAINT chk_admin_preview_status CHECK (status IN ('ready', 'submitted', 'expired'))
);

CREATE INDEX IF NOT EXISTS idx_admin_previews_expiry
  ON admin_previews (expires_at, status);

CREATE TABLE IF NOT EXISTS admin_audit_events (
  event_id            TEXT PRIMARY KEY,
  action              TEXT NOT NULL,
  reason              TEXT NOT NULL,
  batch_id            TEXT,
  run_id              TEXT,
  university_id       TEXT,
  version_id          TEXT,
  metadata            JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_admin_audit_subject
  ON admin_audit_events (university_id, created_at);

CREATE INDEX IF NOT EXISTS idx_admin_audit_action
  ON admin_audit_events (action, created_at);
