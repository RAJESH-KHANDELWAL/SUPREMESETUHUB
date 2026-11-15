# GOOGLE_STORAGE_ECOSYSTEM — Root Catalog

This is the provider-level catalog for Google-related storage categories. It is distinct from every individual category package and does not implement Google Cloud Storage operations.

## Root modules
- `ecosystem_config.py` — root catalog configuration
- `ecosystem_models.py` — category metadata record
- `ecosystem_registry.py` — thread-safe in-memory registry for local development
- `ecosystem_service.py` — taxonomy/index loading, consistency and health checks
- `service.py` — public root catalog service
- `taxonomy/google_storage_taxonomy.json` — grouped taxonomy
- `category_index.json` — category-to-folder mapping
- `api/routes.py` — framework-neutral status endpoints
- `models/record.py` — model export
- `schemas/manifest.schema.json` — root manifest contract
- `tests/test_foundation.py` — offline checks

## Readiness
The root reports catalog consistency only. It never reports a provider connection as verified and never performs external storage operations. Each category adapter requires its own authorized integration, health checks and end-to-end tests.
