# Indexer

This package will publish validated L1 data to OpenSearch staging indexes and switch current aliases after gates pass.

MVP uses per-school current aliases so a single-school update cannot replace
another school's published documents:

```text
l1_catalog_entries_<university_id>_current
l1_url_manifest_<university_id>_current
l1_quick_facts_<university_id>_current
```

Global aggregation aliases such as `l1_catalog_entries_current` are a later
operational layer and must only be switched from a complete multi-school
staging build.
