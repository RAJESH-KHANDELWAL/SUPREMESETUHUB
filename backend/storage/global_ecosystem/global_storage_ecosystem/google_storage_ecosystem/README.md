# GOOGLE_STORAGE_ECOSYSTEM

The provider-level catalog and taxonomy root for Google-related storage domains. This root organizes 184 category namespaces; it is **not** itself a Google Cloud Storage adapter and does not claim that every category is an official Google product.

## Structure
- `taxonomy/google_storage_taxonomy.json` — canonical category groups and classification rules
- `category_index.json` — category IDs, unique package folder names, and paths
- `ecosystem_config.py` — root catalog configuration
- `ecosystem_models.py` — typed category metadata
- `ecosystem_registry.py` — local metadata registry
- `ecosystem_service.py` and `service.py` — catalog status and taxonomy access
- `api/routes.py` — framework-neutral catalog endpoints
- `schemas/` — catalog manifest schema
- `tests/` — offline root-catalog tests

Each category package has its own README, manifest, Python service boundary, API/model namespace, PHP metadata contract, schema and tests.

## Operational boundary
All categories are taxonomy/foundation scaffolds unless separately verified. `NOT_CONFIGURED` means no external connection is established. Do not enable upload, download, delete or synchronization until the exact official provider product/API, authorized credentials, live health checks and end-to-end tests are verified. The root catalog never performs provider I/O.

## Governance
Apply least privilege, encryption, audit logging, data minimization, retention controls, consent and jurisdictional compliance. Adult-related entries are classification namespaces only; age/access controls apply, and unlawful or exploitative content is prohibited.
