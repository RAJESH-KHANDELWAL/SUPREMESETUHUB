# Atlassian Storage Ecosystem

Canonical storage-side catalog for Atlassian products in SUPREMESETUHUB.

## Product ecosystems

- `atlassian_jira_storage_ecosystem` — Jira
- `atlassian_confluence_storage_ecosystem` — Confluence
- `atlassian_bitbucket_storage_ecosystem` — Bitbucket
- `atlassian_trello_storage_ecosystem` — Trello
- `atlassian_jira_service_management_storage_ecosystem` — Jira Service Management
- `atlassian_jira_product_discovery_storage_ecosystem` — Jira Product Discovery
- `atlassian_compass_storage_ecosystem` — Compass
- `atlassian_bamboo_storage_ecosystem` — Bamboo

## Package responsibilities

This package owns the Atlassian product catalog, storage metadata, lifecycle classification and readiness contracts. It does not implement OAuth, credentials, API clients, webhooks or product operations; those belong in the separate Atlassian API/integration layer.

## Foundation files

- `atlassian_storage_ecosystem.py` — provider catalog and manifest validation
- `ecosystem_manifest.json` — product catalog, geographic scope, maturity vocabulary and connection state
- `ecosystem_config.py` — runtime configuration; secrets must come from environment variables or a secret manager
- `ecosystem_models.py` — typed storage metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_service.py` — provider-neutral identity and health contract
- `tests/` — offline tests for catalog and foundation behavior

## Operational boundaries

All eight product entries are catalog-only. No live provider connection, account entitlement, generic file-storage API, export right or provider-side storage guarantee is implied.

A product may be marked connected only after authorized authentication, least-privilege permission checks, live health checks and end-to-end tests pass. Production records belong in central database/object-storage services, not the in-memory registry.

Apply encryption, audit logging, retention controls, jurisdictional compliance and data minimization. Never commit credentials or private customer content.
