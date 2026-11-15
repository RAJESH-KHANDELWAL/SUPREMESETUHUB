# GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM

- **Folder:** `global_individual_storage_ecosystem/`
- **Ecosystem ID:** `GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM`
- **Provider / Owner:** `GLOBAL_INDIVIDUAL`
- **Category:** `INDIVIDUAL`
- **Group:** `PERSONAL_AND_INDIVIDUAL_STORAGE`
- **State:** Category foundation scaffold; external connection is not configured.

## Standard package structure
- `__init__.py` — package export
- `ecosystem_config.py` — runtime configuration; no embedded secrets
- `ecosystem_manifest.json` — canonical ecosystem identity and readiness state
- `ecosystem_models.py` — individual-owned storage metadata model
- `ecosystem_registry.py` — thread-safe in-memory metadata registry for development/tests
- `ecosystem_service.py` — catalog validation, health and description contract
- `service.py` — category-specific adapter boundary
- `api/routes.py` — framework-neutral status and health handlers
- `models/record.py` — public model export
- `schemas/manifest.schema.json` — manifest contract
- `schemas/individual_storage_record.schema.json` — individual metadata contract
- `taxonomy/global_individual_storage_taxonomy.json` — grouped category taxonomy
- `category_index.json` — flat category index and count
- `tests/test_foundation.py` — offline foundation tests
- `php/global_individual_storage_ecosystem.php` — read-only PHP metadata contract

## Scope
Organizes individual-owned storage metadata, opaque identity and ownership references, account associations, personal file/media metadata, backup references, synchronization associations, sharing permissions, retention, portability and recovery metadata. It does not store personal file content.

## Security and integration boundary
Identity proofing/authentication, consent decisions, cryptographic keys and external provider operations remain owned by their respective services. Store only minimized metadata and opaque references. Never store credentials, authentication secrets, cryptographic keys or personal file content in this package.

The package is a foundation scaffold, not a live personal cloud drive. Do not mark it connected until authorized integration, provider-specific live health checks and end-to-end read/write tests pass. Upload, download, delete and synchronization operations remain disabled.
