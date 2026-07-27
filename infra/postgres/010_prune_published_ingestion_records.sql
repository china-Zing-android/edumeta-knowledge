DELETE FROM ingestion_records AS records
USING ingestion_runs AS runs
WHERE records.run_id = runs.run_id
  AND runs.status IN ('published', 'unchanged');
