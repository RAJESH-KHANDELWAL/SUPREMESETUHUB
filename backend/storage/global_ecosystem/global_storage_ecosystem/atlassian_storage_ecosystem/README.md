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

## Responsibility and boundaries

This package owns storage taxonomy, metadata, lifecycle classification and readiness contracts. OAuth, credentials, API clients, webhooks and product operations belong in the Atlassian API/integration layer. Catalog entries do not imply a live connection, entitlement or generic file-storage API.

Each product has `domains/`, `geography/` and `maturity_levels/` classifications. Use least privilege, encryption, audit logs, retention controls and data minimization. Never commit credentials or personal data.
