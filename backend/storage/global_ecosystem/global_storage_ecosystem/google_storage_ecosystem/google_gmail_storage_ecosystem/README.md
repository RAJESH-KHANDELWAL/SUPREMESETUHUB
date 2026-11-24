# GOOGLE_GMAIL_STORAGE_ECOSYSTEM

- **Folder:** `google_gmail_storage_ecosystem/`
- **Ecosystem ID:** `GOOGLE_GMAIL_STORAGE_ECOSYSTEM`
- **Provider:** `GOOGLE`
- **Category:** `GMAIL`
- **Group:** `COMMUNICATION`
- **State:** Category foundation scaffold; external connection is not configured.

## Standard package structure
- `__init__.py` — public package export
- `ecosystem_config.py` — runtime configuration; no embedded secrets
- `ecosystem_manifest.json` — canonical identity and readiness state
- `ecosystem_models.py` — category metadata record with opaque owner reference
- `ecosystem_registry.py` — thread-safe in-memory metadata registry for development/tests
- `ecosystem_service.py` — manifest validation, description and health contract
- `service.py` — category-specific service entry point
- `api/routes.py` — framework-neutral status and health handlers
- `models/record.py` — public model export
- `schemas/manifest.schema.json` — manifest contract
- `schemas/category_record.schema.json` — metadata record contract
- `tests/test_foundation.py` — offline foundation tests
- `php/google_gmail_storage_ecosystem.php` — read-only PHP metadata contract

## Scope
Organizes gmail category metadata and opaque ownership references. It stores minimized metadata only, not provider credentials, authentication secrets, cryptographic keys or personal file content. This category namespace does not imply that a separate official Google product/API exists for every taxonomy entry.

## Security and integration boundary
Identity proofing, authentication, consent decisions, cryptographic keys and external provider operations remain owned by their respective services. Apply least privilege, encryption, audit logging, retention controls, data minimization and jurisdictional compliance.

This package is a foundation scaffold, not a live connected service. Do not mark it connected until the exact official provider product/API, authorized integration, live health checks and end-to-end tests are verified. Upload, download, delete and synchronization remain disabled.
