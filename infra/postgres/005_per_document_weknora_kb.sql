ALTER TABLE universities
  ADD COLUMN IF NOT EXISTS weknora_knowledge_base_id TEXT,
  ADD COLUMN IF NOT EXISTS weknora_knowledge_base_name TEXT;

ALTER TABLE ingestion_runs
  ADD COLUMN IF NOT EXISTS weknora_knowledge_base_id TEXT,
  ADD COLUMN IF NOT EXISTS weknora_kb_operation TEXT NOT NULL DEFAULT 'reuse';

DO $$ BEGIN
  ALTER TABLE ingestion_runs ADD CONSTRAINT chk_run_weknora_kb_operation
    CHECK (weknora_kb_operation IN ('create', 'reuse', 'explicit'));
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;

UPDATE universities AS universities
   SET weknora_knowledge_base_id=current_sources.weknora_knowledge_base_id,
       weknora_knowledge_base_name=COALESCE(universities.weknora_knowledge_base_name, 'legacy-shared')
  FROM (
    SELECT DISTINCT ON (sources.university_id)
           sources.university_id, sources.weknora_knowledge_base_id
      FROM source_registry AS sources
      JOIN school_versions AS versions USING (university_id, version_id)
     WHERE versions.publication_state='current'
       AND sources.weknora_knowledge_base_id IS NOT NULL
     ORDER BY sources.university_id, sources.updated_at DESC
  ) AS current_sources
 WHERE universities.university_id=current_sources.university_id
   AND universities.weknora_knowledge_base_id IS NULL;
