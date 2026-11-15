# Anthropic Storage Ecosystem Foundation

This foundation standardizes storage-side identity, metadata, configuration and health reporting for the Anthropic catalog.

## Existing catalog retained
The eight Anthropic Claude child ecosystems and `anthropic_storage_ecosystem.py` remain intact. This foundation does not replace the provider-specific catalog or duplicate API clients, authentication, endpoints or operations.

## Modules
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_models.py` — typed storage metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_service.py` — foundation status and health contract
- `ecosystem_manifest.json` — existing Anthropic taxonomy and readiness declaration
- `tests/` — offline foundation and catalog tests

## Readiness boundary
FOUNDATION_READY means local foundation code is available. It does not mean Anthropic APIs or any Claude feature is connected, entitled, or capable of generic storage operations. Verify authorized API support and end-to-end behavior before declaring a connection. Production persistence belongs in the central database. Never commit credentials or personal data.
