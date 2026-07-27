ALTER TABLE ingestion_runs
  ADD COLUMN IF NOT EXISTS quality_audits JSONB NOT NULL DEFAULT '{}'::jsonb;
