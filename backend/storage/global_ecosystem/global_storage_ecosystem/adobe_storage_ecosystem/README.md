# ADOBE STORAGE ECOSYSTEM

Provider-owned storage taxonomy and metadata foundation for Adobe-related storage domains.

## Structure
- `taxonomy/adobe_storage_taxonomy.json`: canonical taxonomy grouped by storage domain.
- `category_index.json`: canonical index of all 9 Adobe storage category packages.
- `adobe_storage_capability_matrix.json`: product/API boundary and capability notes.
- `adobe_storage_ecosystem.py`: provider-level child ecosystem catalog.
- Each category package retains its product-specific README, manifest, adapter contract, config, models, registry, service and tests; it also includes API-handler contracts, record models, JSON schema, PHP metadata reader and ecosystem health/configuration contracts.

## Readiness boundary
All packages are catalog/foundation scaffolds. They do not prove Adobe product entitlement, API availability, or live storage connectivity. No upload, download, delete, sync, replication or persistence operation is enabled by these scaffolds. Implement only documented product-specific APIs with authorized credentials, live health checks and end-to-end tests. Never commit secrets or personal data.
