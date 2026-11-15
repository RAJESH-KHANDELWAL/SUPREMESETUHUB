# Adobe Express Storage

Provider: Adobe  
Storage namespace: `express`  
Related API family: No dedicated Express storage API asserted in current Adobe API catalog

## Responsibility
Express project metadata, graphics, brand assets, webpages, videos and published-content references where supported.

## API boundary
Verify documented API support and entitlement before implementing any file operation.

OAuth, tokens, scopes, clients, endpoints and external requests belong to `backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`. This package owns normalized storage metadata, object identity, version/lifecycle metadata, registry and readiness contract.

## Files
- `models.py`: validated storage object metadata
- `registry.py`: thread-safe in-memory metadata registry (not production persistence)
- `service.py`: metadata registration and readiness service
- `manifest.json`: machine-readable scope and status
- `tests/test_foundation.py`: offline tests

## Status
Foundation only; external connection `NOT_CONFIGURED`. A healthy local package does not prove entitlement, API availability, OAuth success or working file operations. Production persistence belongs in the central database. Never commit credentials or personal data.
