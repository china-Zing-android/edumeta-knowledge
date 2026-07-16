CREATE TABLE IF NOT EXISTS universities (
  university_id TEXT PRIMARY KEY,
  university_name TEXT NOT NULL,
  aliases JSONB NOT NULL DEFAULT '[]'::jsonb,
  country_code TEXT,
  region TEXT,
  school_tier TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT chk_university_tier CHECK (school_tier IN ('core', 'non_core')),
  CONSTRAINT chk_university_status CHECK (status IN ('pending', 'active', 'failed'))
);

INSERT INTO universities (university_id, university_name, aliases, school_tier, status)
SELECT DISTINCT versions.university_id,
       CASE WHEN versions.university_id='mit' THEN 'Massachusetts Institute of Technology'
            ELSE initcap(replace(versions.university_id, '_', ' ')) END,
       jsonb_build_array(upper(versions.university_id)),
       COALESCE((SELECT runs.school_tier FROM ingestion_runs AS runs
                 WHERE runs.university_id=versions.university_id
                 ORDER BY runs.created_at DESC LIMIT 1), 'core'),
       'active'
  FROM school_versions AS versions
ON CONFLICT (university_id) DO NOTHING;

CREATE INDEX IF NOT EXISTS idx_universities_range
  ON universities (country_code, region, school_tier, status);

DO $$ BEGIN
  ALTER TABLE school_versions ADD CONSTRAINT fk_school_university
    FOREIGN KEY (university_id) REFERENCES universities(university_id);
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;

CREATE TABLE IF NOT EXISTS catalog_entry_disciplines (
  link_id TEXT NOT NULL,
  university_id TEXT NOT NULL,
  version_id TEXT NOT NULL,
  entry_id TEXT NOT NULL,
  discipline_id TEXT NOT NULL,
  discipline_label TEXT NOT NULL,
  match_method TEXT NOT NULL DEFAULT 'rule',
  confidence DOUBLE PRECISION NOT NULL DEFAULT 1,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (university_id, version_id, link_id),
  UNIQUE (university_id, version_id, entry_id, discipline_id),
  CONSTRAINT fk_discipline_entry
    FOREIGN KEY (university_id, version_id, entry_id)
    REFERENCES catalog_entries(university_id, version_id, entry_id)
);

CREATE INDEX IF NOT EXISTS idx_catalog_disciplines_lookup
  ON catalog_entry_disciplines (discipline_id, university_id, version_id);

ALTER TABLE ingestion_runs
  ADD COLUMN IF NOT EXISTS operation TEXT NOT NULL DEFAULT 'update';

DO $$ BEGIN
  ALTER TABLE ingestion_runs ADD CONSTRAINT chk_run_operation
    CHECK (operation IN ('create', 'update', 'unchanged'));
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;
