# GLOBAL WORDPRESS HOSTING HOSTING STORAGE ECOSYSTEM

- **Folder:** `global_wordpress_hosting_storage_ecosystem/`
- **Category:** WORDPRESS_HOSTING
- **Group:** HOSTING_PLATFORMS
- **Provider:** GLOBAL HOSTING
- **State:** Category foundation scaffold; external connection is not configured.

## Scope
WordPress sites, environments, deployment and platform metadata.

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
- `php/global_wordpress_hosting_storage_ecosystem.php` — PHP metadata reader

## Safety and integration boundary
This is a storage taxonomy namespace, not proof that a hosting provider offers this service or that an account is connected. Do not mark connected until authorized credentials, provider-specific live health checks and end-to-end tests pass. No provisioning, deployment, upload, download, delete or billing operation is enabled by this scaffold. Never commit credentials or personal data.
