# GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM

- **Folder:** `global_individual_storage_ecosystem/`
- **Category:** INDIVIDUAL
- **Group:** PERSONAL_AND_INDIVIDUAL_STORAGE
- **Provider / Owner:** GLOBAL INDIVIDUAL
- **State:** Category foundation scaffold; external connection is not configured.

## Package contents
- `__init__.py` — package export
- `ecosystem_config.py` — runtime configuration
- `ecosystem_models.py` — individual storage metadata model
- `ecosystem_service.py` — health and description contract
- `service.py` — category-specific adapter boundary
- `api/routes.py` — framework-neutral API handlers
- `models/record.py` — model export
- `schemas/manifest.schema.json` — manifest schema
- `schemas/individual_storage_record.schema.json` — individual metadata schema
- `tests/test_foundation.py` — offline tests
- `php/global_individual_storage_ecosystem.php` — PHP metadata reader

## Scope
This category organizes individual-owned storage metadata, identity references, personal files and media metadata, backup references, synchronization associations, sharing permissions, retention, portability and recovery metadata. The foundation must not store personal file content, credentials, authentication secrets or cryptographic keys.

## Safety and integration boundary
Identity proofing and authentication belong to the identity/authentication services; consent decisions belong to the consent service; cryptographic keys belong to key management; external storage operations belong to approved provider adapters. Do not mark connected until authorized credentials, provider-specific live health checks and end-to-end read/write tests pass. No upload, download or delete operation is enabled by this scaffold. Never commit credentials or personal data.
