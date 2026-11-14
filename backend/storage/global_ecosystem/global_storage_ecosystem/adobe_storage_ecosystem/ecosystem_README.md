# Adobe Storage Ecosystem Foundation

This is the Adobe-specific provider package inside the Global Storage Ecosystem.

## Package modules

- `ecosystem_config.py` — runtime configuration; secrets must come from a secret manager or environment.
- `ecosystem_models.py` — typed metadata records.
- `ecosystem_registry.py` — local metadata registry.
- `ecosystem_service.py` — package identity and readiness contract.
- `ecosystem_manifest.json` — Adobe storage scope, products, capabilities, and connection state.
- `products/`, `services/`, `platforms/`, `storage_capabilities/` — Adobe-specific catalog namespaces.
- `geography/` and `maturity_levels/` — coverage descriptors, not universal subject taxonomies.
- `tests/` — offline foundation tests.

## Readiness policy

`FOUNDATION_INITIALIZED` means the local package scaffold exists. It does not mean Adobe is connected. Use `NOT_CONFIGURED` until an authorized Adobe organization, product entitlement, credentials, OAuth scopes, permissions, and live health checks are verified.

## Architecture boundary

Universal subject categories belong to sibling Global Category Storage Ecosystems. This Adobe package must contain only Adobe provider products, services, platforms, storage constructs, and their integrations.
