# DigitalOcean Storage Ecosystem Foundation

This root follows the Google Storage Ecosystem parent-catalog pattern: canonical taxonomy, category index, independently named category packages, read-only catalog API, metadata foundation and offline tests.

## Modules
- `ecosystem_config.py` — runtime configuration; no embedded secrets
- `ecosystem_models.py` — typed storage metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_service.py` — foundation status and health contract
- `ecosystem_taxonomy.py` — taxonomy loader and lookup helpers
- `catalog_api.py` — read-only category catalog
- `taxonomy/digitalocean_storage_taxonomy.json` — grouped taxonomy
- `category_index.json` — category-to-folder mapping
- `tests/` — offline tests

## Responsibility boundary
The storage catalog does not implement DigitalOcean authentication, API clients, network calls or data transfer. Those remain in API/integration layers. The central database owns production persistence.

## Readiness boundary
`FOUNDATION_READY` means local catalog code is available only. It does not establish API support, account entitlement, connectivity, or successful upload/download/delete. Keep external connections `NOT_CONFIGURED` until authorized live health checks and end-to-end tests pass. Never commit credentials or personal data.