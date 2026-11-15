# Adobe Creative Cloud Assets Storage

Provider: Adobe  
Storage namespace: `creative_cloud_assets`  
Related API family: Creative Cloud and Assets APIs

## Responsibility
Reusable creative assets, metadata, ownership, sharing, versions and supported library relationships.

## API boundary
Only documented asset endpoints, types and authorized scopes are in scope.

OAuth, tokens, scopes, clients, endpoints and external requests belong to `backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`. This package owns storage metadata, object identity, version/lifecycle metadata, registry and readiness contract.

## Files
- `models.py`: validated storage object metadata
- `registry.py`: thread-safe in-memory metadata registry (not production persistence)
- `service.py`: metadata registration and readiness service
- `manifest.json`: machine-readable scope and status
- `tests/test_foundation.py`: offline tests

## Status
Foundation only; external connection `NOT_CONFIGURED`. A healthy local package does not prove entitlement, API availability, OAuth success or working file operations. Production persistence belongs in the central database. Never commit credentials or personal data.
