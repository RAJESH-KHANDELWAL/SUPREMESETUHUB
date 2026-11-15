# Adobe Creative Cloud Storage

Provider: Adobe  
Storage namespace: `creative_cloud`  
Related API family: Creative Cloud and Assets APIs

## Responsibility
Cloud documents, supported application project references and Creative Cloud Libraries; distinguish cloud documents from local project files.

## API boundary
Desktop applications are not automatically exposed as general-purpose APIs. Cloud document and Libraries support must be verified separately.

OAuth, tokens, scopes, clients, endpoints and external requests belong to `backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`. This package owns normalized storage metadata, object identity, version/lifecycle metadata, registry and readiness contract.

## Files
- `models.py`: validated storage object metadata
- `registry.py`: thread-safe in-memory metadata registry (not production persistence)
- `service.py`: metadata registration and readiness service
- `manifest.json`: machine-readable scope and status
- `tests/test_foundation.py`: offline tests

## Status
Foundation only; external connection `NOT_CONFIGURED`. A healthy local package does not prove entitlement, API availability, OAuth success or working file operations. Production persistence belongs in the central database. Never commit credentials or personal data.
