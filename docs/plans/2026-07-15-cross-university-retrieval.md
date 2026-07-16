# Cross-University Retrieval Implementation Plan

## Objective

Add automated university upsert ingestion and bidirectional/range retrieval without reintroducing L0, rankings, external discovery, or a second runtime architecture.

## Tasks

1. Define controlled discipline taxonomy and catalog enrichment contract.
2. Add university registry and catalog-discipline relationships to PostgreSQL.
3. Version parser output so parser/schema upgrades rebuild unchanged source MD safely.
4. Add the preferred university ingestion API and complete stage/status reporting.
5. Publish current-aware university/catalog documents to OpenSearch.
6. Add downward/range/upward retrieval modes and filters.
7. Extend the single MCP tool schema without adding new tools.
8. Add objective QA for discipline-to-university and range filtering.
9. Rebuild Compose, migrate current data, and run full regression and latency gates.
