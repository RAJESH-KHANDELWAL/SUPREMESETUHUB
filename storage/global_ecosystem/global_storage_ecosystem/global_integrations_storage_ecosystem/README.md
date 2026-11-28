# GLOBAL INTEGRATIONS STORAGE ECOSYSTEM

- **Folder:** `global_integrations_storage_ecosystem/`
- **Ecosystem ID:** `GLOBAL_INTEGRATIONS_STORAGE_ECOSYSTEM`
- **Provider / Owner:** `GLOBAL INTEGRATIONS`
- **Owning layer:** `STORAGE`
- **Source taxonomy:** `GLOBAL_INTEGRATIONS_API_ECOSYSTEM`
- **Category namespaces:** 30 API-aligned storage scaffolds
- **State:** Taxonomy and catalog foundation; external connections are not configured.

## Architecture
The existing API-layer taxonomy is the naming and classification reference. Each existing `*_integrations_api_ecosystem` namespace has a corresponding `*_integrations_storage_ecosystem` child namespace. Existing source names are preserved; only the owning layer suffix changes from API to STORAGE.

## Root package
- `ecosystem_config.py` — runtime configuration; no embedded secrets
- `ecosystem_manifest.json` — canonical identity, source mapping and readiness state
- `ecosystem_models.py` — typed storage metadata record
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_service.py` — catalog validation and health contract
- `ecosystem_taxonomy.py` / `taxonomy/` — API-aligned category taxonomy
- `category_index.json` — source API namespace to storage folder map
- `catalog_api.py` — read-only catalog facade
- `api/routes.py` — framework-neutral read-only handlers
- `models/` and `schemas/` — public model and manifest contract
- `php/` — read-only PHP metadata contract
- `tests/` — offline foundation tests

## Layer boundary and readiness
This package owns storage-side identity, metadata, taxonomy, object lifecycle definitions and storage health metadata. API routes/contracts remain in the API layer; provider API clients, authentication and external operations remain in their respective API/integration layers. A matching API namespace is not proof of a provider storage product, official endpoint, account entitlement or working integration. Do not mark a provider connected until authorized live health checks and end-to-end read/write tests pass. Upload, download, delete and synchronization remain disabled. Never commit credentials or personal data.
