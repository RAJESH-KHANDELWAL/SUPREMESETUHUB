# GOOGLE_STORAGE_ECOSYSTEM — Root Catalog Foundation

This package follows the standardized foundation layout while retaining its distinct role as the provider-level taxonomy/catalog root. It organizes Google-related storage category namespaces; it is not a live Google Drive, Google Photos or Google Cloud Storage adapter and does not claim every taxonomy category is an official Google product.

## Canonical identity
- Ecosystem ID: `GOOGLE_STORAGE_ECOSYSTEM`
- Package: `google_storage_ecosystem`
- Provider: `GOOGLE`
- Package type: `STORAGE_TAXONOMY_AND_METADATA_FOUNDATION`
- Taxonomy: 18 groups / 184 categories
- Connection state: `NOT_CONFIGURED`

## Foundation modules
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_manifest.json` — canonical identity, safety flags and readiness state
- `ecosystem_models.py` — typed category metadata record
- `ecosystem_registry.py` — thread-safe in-memory registry for local development/tests only
- `ecosystem_service.py` — taxonomy/index/schema consistency validation and health contract
- `service.py` and `__init__.py` — public root catalog entry points
- `api/routes.py` — framework-neutral catalog status and health handlers
- `models/record.py` — public model export
- `schemas/manifest.schema.json` — root manifest JSON contract
- `taxonomy/google_storage_taxonomy.json` and `category_index.json` — taxonomy source and flat category index
- `tests/test_foundation.py` — offline root-catalog tests
- `php/google_storage_ecosystem.php` — read-only PHP metadata reader

## Category package boundary
Every category is isolated in its own `google_<category>_storage_ecosystem/` package. Category-specific configuration, metadata models, registry, service adapter boundary, API, schemas, tests and PHP contract belong to that child package. The root catalog validates classification and package paths; it does not perform provider I/O.

## Data ownership and security
Store category metadata and opaque references only where appropriate. Do not store credentials, authentication secrets, cryptographic keys or personal file content in this root catalog. Apply least privilege, encryption, audit logging, data minimization, retention controls, consent and jurisdictional compliance. Age/access controls apply where required.

## Readiness contract
`TAXONOMY_AND_CATALOG_FOUNDATION` means the root taxonomy and local catalog contracts exist. It does not mean an external provider is connected or that all 184 categories are verified Google products. Authorized integration, exact product/API verification, live health checks and end-to-end tests are required before any category enables storage operations. Upload, download, delete and synchronization remain disabled at this root.
