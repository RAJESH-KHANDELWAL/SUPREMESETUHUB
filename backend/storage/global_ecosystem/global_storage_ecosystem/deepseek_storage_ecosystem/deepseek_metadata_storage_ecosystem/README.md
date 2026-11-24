# DEEPSEEK_METADATA_STORAGE_ECOSYSTEM

- **Folder:** `deepseek_metadata_storage_ecosystem/`
- **Category:** METADATA
- **Group:** DATA_AND_STORAGE
- **Provider:** DeepSeek
- **State:** Category foundation scaffold; external connection is not configured.

## Package contents
- `__init__.py` — package export
- `ecosystem_config.py` — runtime configuration
- `ecosystem_models.py` — category metadata model
- `ecosystem_service.py` — health and description contract
- `service.py` — category-specific adapter boundary
- `api/routes.py` — framework-neutral API handlers
- `models/record.py` — model export
- `schemas/manifest.schema.json` — manifest schema
- `tests/test_foundation.py` — offline tests
- `php/deepseek_metadata_storage_ecosystem.php` — PHP metadata reader

## Safety and integration boundary
This folder is a category namespace, not proof that DeepSeek offers a matching product or stores this category's data. Do not mark connected until authorized credentials, provider-specific live health checks and end-to-end read/write tests pass. No upload, download or delete operation is enabled by this scaffold. Never commit credentials or personal data.
