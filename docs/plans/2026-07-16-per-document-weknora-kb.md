# Per-Document WeKnora KB Implementation

1. Persist the university-to-current-KB mapping and the ingestion run's KB operation.
2. Add upload parameters for explicit KB selection and force-new behavior.
3. Add a WeKnora KB control client that validates existing KBs and creates new KBs from a template.
4. Stamp the resolved KB ID onto every source before staging and publication.
5. Route import jobs and polling through each job's KB ID.
6. Group deep-search scopes by source KB ID and query each KB independently.
7. Move MIT to the supplied KB, then ingest smaller test documents into newly created KBs.
8. Verify same-school update reuse and explicit single-document KB update.
