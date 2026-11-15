# GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM

- **Folder:** `global_individual_storage_ecosystem/`
- **Ecosystem ID:** `GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM`
- **Provider / Owner:** `GLOBAL_INDIVIDUAL`
- **Category:** `INDIVIDUAL`
- **Group:** `PERSONAL_AND_INDIVIDUAL_STORAGE`
- **State:** `CATEGORY_FOUNDATION_SCAFFOLD`
- **Connection:** `NOT_CONFIGURED`

## Standard category package structure

- `__init__.py` — package export
- `ecosystem_config.py` — safe-by-default runtime configuration; no embedded secrets
- `ecosystem_manifest.json` — canonical ecosystem identity and readiness state
- `ecosystem_models.py` — individual-owned metadata record and opaque owner reference
- `ecosystem_registry.py` — thread-safe in-memory registry for development/tests
- `ecosystem_service.py` — manifest, taxonomy, index, safety and health validation
- `service.py` — category-specific adapter boundary
- `api/routes.py` — framework-neutral status and health handlers
- `models/record.py` — public model export
- `schemas/manifest.schema.json` — strict manifest contract
- `schemas/individual_storage_record.schema.json` — individual metadata record contract
- `taxonomy/global_individual_storage_taxonomy.json` — grouped taxonomy source
- `category_index.json` — flat category index and declared count
- `tests/test_foundation.py` — offline foundation contract tests
- `php/global_individual_storage_ecosystem.php` — read-only PHP metadata contract

## Scope

Organizes individual-owned storage metadata, opaque identity and ownership references, account associations, personal file/media metadata, backup references, synchronization associations, sharing permissions, retention, portability and recovery metadata. It does not store personal file content.

## Validation contract

The foundation health check verifies canonical manifest identity, package/provider/category/group alignment, taxonomy-to-index equality, declared category count, duplicate-category protection, foundation state and safe integration flags. The expected taxonomy and index each contain 17 categories.

## Security and integration boundary

Identity proofing/authentication, consent decisions, cryptographic keys and external provider operations remain owned by their respective services. Store minimized metadata and opaque references only. Never store credentials, authentication secrets, cryptographic keys or personal file content.

Runtime enablement defaults to **false**. External connection remains `NOT_CONFIGURED`; provider verification remains false; upload, download, delete and synchronization remain disabled. Do not enable operations until authorized integration, live provider health checks and end-to-end read/write tests have passed.
