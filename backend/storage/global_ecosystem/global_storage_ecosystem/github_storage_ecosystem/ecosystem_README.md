# GITHUB Storage Ecosystem Foundation

Parent catalog for 30 GitHub storage-related category packages. This follows the shared provider-storage foundation pattern: canonical taxonomy, category index, category packages, read-only catalog API, metadata foundation and offline tests.

## Modules
- `ecosystem_config.py` — runtime configuration; no embedded secrets
- `ecosystem_models.py` — typed storage metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_service.py` — foundation status and health contract
- `ecosystem_taxonomy.py` — taxonomy loader and lookup helpers
- `catalog_api.py` — read-only category catalog
- `taxonomy/github_storage_taxonomy.json` — canonical grouped taxonomy
- `category_index.json` — category-to-folder mapping
- `tests/` — offline tests

## Responsibility boundary
This STORAGE namespace owns storage-side identity, taxonomy, metadata, lifecycle definitions and health contracts. GitHub API clients, OAuth/PAT authentication, scopes, endpoints and external operations remain in API/integration layers. Production persistence belongs in the central database.

## Readiness boundary
`FOUNDATION_READY` means local catalog code is available only. It does not establish GitHub API support, account entitlement, authorized connectivity, or successful read/write/delete operations. Keep external connections `NOT_CONFIGURED` until authorized live health checks and end-to-end tests pass. Never commit access tokens, webhook secrets or private repository content.
