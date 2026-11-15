# GLOBAL INDIVIDUAL Storage Ecosystem — Foundation

This package defines a provider-neutral storage metadata foundation for individual-person data. It is not a live personal cloud drive and does not create, authenticate or connect external accounts.

## Modules

- `ecosystem_config.py` — runtime configuration; no embedded secrets
- `ecosystem_models.py` — typed individual-storage metadata records
- `ecosystem_registry.py` — thread-safe in-memory registry for local development/tests
- `ecosystem_service.py` — capability, readiness and health contract
- `ecosystem_manifest.json` — scope, privacy rules and readiness declaration
- `taxonomy/` — controlled taxonomy for individual storage domains
- `api/routes.py` — framework-neutral API route contract
- `models/record.py` — import-compatible model surface
- `schemas/` — JSON schema for individual storage metadata
- `tests/` — offline foundation tests

## Data ownership

The identity service owns identity proofing and account authentication. Consent/authorization services own consent decisions. Key-management services own cryptographic keys. Provider adapters own external storage operations. This package stores opaque references and storage metadata only.

## Readiness

`FOUNDATION_READY` means local foundation code is available. It does not mean a provider is connected or that files can be uploaded, downloaded, shared or deleted. Production persistence must use the central database with least-privilege access, encryption, audit logs, retention controls, backups and jurisdictional compliance.
