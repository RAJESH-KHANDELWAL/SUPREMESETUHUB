# ADOBE CREATIVE CLOUD STORAGE

- **Folder:** `adobe_creative_cloud_storage_ecosystem/`
- **Provider:** Adobe
- **Category:** CREATIVE_CLOUD
- **Group:** CREATIVE_CLOUD
- **State:** Category foundation scaffold; external connection is not configured.

## Package contents
- `__init__.py` — package exports and compatibility interfaces
- `api/routes.py` — framework-neutral status and health handlers
- `ecosystem_config.py` — environment-only runtime configuration
- `ecosystem_manifest.json` — canonical machine-readable package manifest
- `ecosystem_models.py` — typed category metadata record
- `ecosystem_service.py` — category readiness and health contract
- `models/record.py` — canonical model export
- `php/adobe_creative_cloud_storage_ecosystem.php` — PHP metadata reader
- `schemas/manifest.schema.json` — manifest validation schema
- `service.py` — Adobe-specific metadata/readiness service
- `tests/test_foundation.py` — offline package tests

Adobe-specific adapter contract, metadata registry and legacy compatibility modules are retained where present.

## Integration and safety boundary
This is a category namespace and metadata scaffold, not proof of a matching Adobe product entitlement or live API access. No upload, download, delete, sync or replication operation is enabled. Implement only documented product-specific APIs with authorized credentials, provider-specific live health checks and end-to-end tests. Never commit credentials or personal data.
