# ADOBE STORAGE ECOSYSTEM

Canonical Adobe storage-domain catalog and category package collection, aligned to the Google Storage Ecosystem package layout.

## Root package
- `service.py`: provider-level Adobe Storage Ecosystem entry point.
- `catalog_api.py`: read-only category catalog API.
- `ecosystem_config.py`: environment-only runtime configuration.
- `ecosystem_models.py`: typed ecosystem metadata record.
- `ecosystem_registry.py`: thread-safe in-memory metadata registry (not production persistence).
- `ecosystem_service.py`: readiness and health contract.
- `ecosystem_manifest.json`: machine-readable ecosystem identity and readiness.
- `category_index.json`: canonical index of all 9 category packages.
- `taxonomy/adobe_storage_taxonomy.json`: canonical grouped taxonomy.
- `adobe_storage_capability_matrix.json`: product/API boundaries and capability notes.
- `php/AdobeStorageCatalog.php`: PHP metadata interface.
- `tests/`: offline foundation and taxonomy tests.

## Category package layout
Each category follows the Google category-package baseline: `README.md`, `__init__.py`, `api/`, `ecosystem_config.py`, `ecosystem_manifest.json`, `ecosystem_models.py`, `ecosystem_service.py`, `models/`, `php/`, `schemas/`, `service.py`, and `tests/`.

Adobe-specific adapter contracts, metadata registries and legacy compatibility modules are retained where useful.

## Readiness boundary
These packages are catalog and metadata foundations. They do not prove Adobe product entitlement, API availability or live storage connectivity. No upload, download, delete, sync or replication operation is enabled. Implement only documented product-specific APIs with authorized credentials, live health checks and end-to-end tests. Never commit secrets or personal data.
