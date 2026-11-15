# GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM

- **Folder:** `global_individual_storage_ecosystem/`
- **Ecosystem ID:** `GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM`
- **Provider / Owner:** `GLOBAL_INDIVIDUAL`
- **Category:** `INDIVIDUAL`
- **Group:** `PERSONAL_AND_INDIVIDUAL_STORAGE`
- **State:** `CATEGORY_FOUNDATION_SCAFFOLD`
- **Connection:** `NOT_CONFIGURED`

## Standard package structure

- `__init__.py` — public package export
- `ecosystem_config.py` — safe-by-default runtime configuration; no embedded secrets
- `ecosystem_manifest.json` — canonical identity and readiness state
- `ecosystem_models.py` — individual metadata record with opaque owner reference
- `ecosystem_registry.py` — thread-safe in-memory metadata registry for development/tests
- `ecosystem_service.py` — manifest, taxonomy, index, safety and health validation
- `service.py` — category-specific service entry point
- `api/__init__.py` and `api/routes.py` — API namespace and framework-neutral status/health handlers
- `models/__init__.py` and `models/record.py` — public model namespace and export
- `schemas/manifest.schema.json` — manifest contract
- `schemas/category_record.schema.json` — standard category metadata record contract
- `schemas/individual_storage_record.schema.json` — individual-domain metadata contract
- `taxonomy/global_individual_storage_taxonomy.json` — grouped taxonomy source
- `category_index.json` — flat category index and declared count
- `tests/__init__.py` and `tests/test_foundation.py` — offline foundation tests
- `php/global_individual_storage_ecosystem.php` — read-only PHP metadata contract

## Scope

Organizes individual-owned storage metadata, opaque identity and ownership references, account associations, personal file/media metadata, backup references, synchronization associations, sharing permissions, retention, portability and recovery metadata. It does not store personal file content.

## Validation contract

The foundation health check verifies canonical manifest identity, package/provider/category/group alignment, taxonomy-to-index equality, declared category count, duplicate-category protection, foundation state and safe integration flags. The expected taxonomy and index each contain 17 categories. The standard category schema and the individual-domain schema both preserve the mandatory opaque owner reference.

## Security and integration boundary

Identity proofing/authentication, consent decisions, cryptographic keys and external provider operations remain owned by their respective services. Store minimized metadata and opaque references only. Never store credentials, authentication secrets, cryptographic keys or personal file content.

Runtime enablement defaults to **false**. External connection remains `NOT_CONFIGURED`; provider verification remains false; upload, download, delete and synchronization remain disabled. Do not enable operations until authorized integration, live provider health checks and end-to-end read/write tests have passed.
