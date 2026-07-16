CREATE TABLE IF NOT EXISTS entity_contexts (
  context_id TEXT NOT NULL,
  university_id TEXT NOT NULL,
  version_id TEXT NOT NULL,
  entity_type TEXT NOT NULL,
  entity_id TEXT NOT NULL,
  entry_id TEXT,
  title TEXT NOT NULL,
  display_label TEXT NOT NULL,
  attributes JSONB NOT NULL DEFAULT '{}'::jsonb,
  highlights JSONB NOT NULL DEFAULT '[]'::jsonb,
  sample_children JSONB NOT NULL DEFAULT '[]'::jsonb,
  related_entities JSONB NOT NULL DEFAULT '[]'::jsonb,
  available_topics JSONB NOT NULL DEFAULT '[]'::jsonb,
  source_ids JSONB NOT NULL DEFAULT '[]'::jsonb,
  md_section_paths JSONB NOT NULL DEFAULT '[]'::jsonb,
  dataset_version TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'active',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
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
