# GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM — Foundation

This package follows the category foundation layout used by the provider storage ecosystems. It defines a provider-neutral individual-storage category contract; it is not a live personal cloud drive.

## Modules
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_models.py` — category metadata model
- `ecosystem_registry.py` — thread-safe in-memory metadata registry for local development/tests
- `ecosystem_service.py` — health and description contract
- `service.py` — category-specific adapter boundary
- `ecosystem_manifest.json` — category identity, scope and readiness state
- `taxonomy/` and `category_index.json` — individual storage taxonomy
- `api/routes.py` — framework-neutral API handlers
- `models/record.py` — public model export
- `schemas/` — manifest and individual metadata schemas
- `tests/test_foundation.py` — offline tests
- `php/` — read-only PHP metadata contract

## Data ownership
Identity proofing/authentication, consent decisions, cryptographic keys and external provider operations remain owned by their respective services. This package stores opaque references and minimized metadata only; it must not store personal file content or secrets.

## Readiness
`CATEGORY_FOUNDATION_SCAFFOLD` means package structure and local contracts exist. It does not mean an external provider is connected. Connection requires authorized integration, live health checks and end-to-end tests. Upload/download/delete remain disabled.
