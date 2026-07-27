ALTER TABLE ingestion_runs
  DROP CONSTRAINT IF EXISTS chk_run_status;

ALTER TABLE ingestion_runs
  ADD CONSTRAINT chk_run_status
  CHECK (status IN (
    'accepted',
    'parsing',
    'weknora_preparing',
    'unchanged',
    'validating',
    'publishing',
    'published',
    'failed'
  ));
