# ANTHROPIC_CLAUDE_CONNECTORS_STORAGE_ECOSYSTEM

- **Package:** `anthropic_claude_connectors_storage_ecosystem/`
- **Provider:** Anthropic
- **Category:** CLAUDE_CONNECTORS
- **Group:** CONNECTOR_METADATA
- **State:** Category foundation scaffold; external connection is not configured.

## Canonical package structure
`__init__.py`, `api/`, `ecosystem_config.py`, `ecosystem_manifest.json`,
`ecosystem_models.py`, `ecosystem_service.py`, `models/`, `php/`,
`schemas/`, `service.py`, and `tests/`.

## Preserved taxonomy
The existing `domains/`, `geography/`, and `maturity_levels/` directories remain part of this child ecosystem.

## Integration boundary
This package is a taxonomy and metadata scaffold. It does not establish that Claude claude connectors exposes a generic storage API. Do not mark connected or enable storage operations until product/API availability, account entitlements, authorization, live health checks, and end-to-end tests are verified. Never commit credentials or personal data.
