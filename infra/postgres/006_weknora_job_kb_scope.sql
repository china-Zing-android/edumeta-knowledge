DROP INDEX IF EXISTS uq_weknora_jobs_active_source;

CREATE UNIQUE INDEX uq_weknora_jobs_active_source
  ON weknora_import_jobs (university_id, knowledge_base_id, source_id)
  WHERE status IN ('queued', 'running', 'success');
