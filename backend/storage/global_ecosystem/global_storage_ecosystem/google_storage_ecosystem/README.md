# GOOGLE_STORAGE_ECOSYSTEM

- **Folder:** `google_storage_ecosystem/`
- **Ecosystem ID:** `GOOGLE_STORAGE_ECOSYSTEM`
- **Provider:** `GOOGLE`
- **Package type:** `STORAGE_TAXONOMY_AND_METADATA_FOUNDATION`
- **State:** Root catalog foundation; external connection is not configured.
- **Coverage:** 18 taxonomy groups and 184 category namespaces.

## Standard root package structure
- `__init__.py` — public package export
- `ecosystem_config.py` — runtime configuration; no embedded secrets
- `ecosystem_manifest.json` — canonical root identity and readiness state
- `ecosystem_models.py` — typed category metadata model
- `ecosystem_registry.py` — thread-safe in-memory metadata registry for development/tests
- `ecosystem_service.py` — taxonomy/index/schema validation, catalog description and health contract
- `service.py` — public Google Storage catalog service
- `api/routes.py` — framework-neutral catalog status and health handlers
- `models/record.py` — public model export
- `schemas/manifest.schema.json` — root manifest contract
- `taxonomy/google_storage_taxonomy.json` — grouped taxonomy source
- `category_index.json` — flat category-to-folder index and count
- `tests/test_foundation.py` — offline root-catalog tests
- `php/google_storage_ecosystem.php` — read-only PHP metadata contract

## Architecture and scope
This directory is the provider-level Google storage taxonomy/catalog root. It organizes category namespaces; it is not itself a Google Drive, Google Photos or Google Cloud Storage adapter. The taxonomy is a classification framework and does not imply that Google offers an official product/API for every listed category.

Each category has a separate `google_<category>_storage_ecosystem/` child package. Each child package owns its category-specific manifest, configuration, models, registry/service boundary, API, schemas, tests and PHP metadata contract. Provider-specific integrations must remain inside the relevant verified child package.

## Security and integration boundary
Keep credentials, access tokens, cryptographic keys and personal file content out of this catalog. Use least privilege, data minimization, encryption, audit logging, retention controls, consent where required, age/access controls where required and jurisdictional compliance.

The root is a foundation scaffold, not a live Google storage connector. Do not mark it connected until the exact official provider product/API, authorized credentials, live health checks and end-to-end tests are verified. Upload, download, delete and synchronization operations remain disabled.
