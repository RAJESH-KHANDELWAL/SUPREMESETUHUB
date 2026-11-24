# GLOBAL_CLOUD_BOOT_VOLUME_STORAGE_ECOSYSTEM

- **Folder:** `global_cloud_boot_volume_storage_ecosystem/`
- **Parent ecosystem:** `GLOBAL_CLOUD_STORAGE_ECOSYSTEM`
- **Category:** `BLOCK_VOLUME_STORAGE`
- **Category group:** `BLOCK_AND_VOLUME_STORAGE`
- **Subcategory:** Boot Volume Storage
- **Provider scope:** Provider-neutral global cloud storage taxonomy
- **State:** Independent category foundation scaffold; external provider connection is not configured.

## Package contents
- `__init__.py` — package export
- `ecosystem_config.py` — environment-based runtime configuration
- `ecosystem_manifest.json` — category identity and safety state
- `ecosystem_models.py` — category metadata record
- `ecosystem_service.py` — health and description contract
- `service.py` — category-specific adapter boundary
- `api/routes.py` — framework-neutral API handlers
- `models/record.py` — model export
- `schemas/manifest.schema.json` — manifest schema
- `tests/test_foundation.py` — offline foundation tests
- `php/global_cloud_boot_volume_storage_ecosystem.php` — read-only PHP metadata contract

## Integration and safety boundary
This package is an independent taxonomy and metadata namespace. Its existence does not assert that every cloud provider offers this capability. Do not mark a provider connected until its product is verified, authorized credentials are configured through an external secret manager, provider-specific live health checks pass, and end-to-end tests are completed. Storage operations remain disabled. Never commit credentials, personal data, or customer file contents.
