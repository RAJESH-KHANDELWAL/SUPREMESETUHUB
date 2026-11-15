# Adobe Document Cloud Storage

Provider: Adobe  
Storage namespace: `document_cloud`  
Related API family: PDF Services API; Acrobat Sign API

## Responsibility
Document Cloud file metadata, ownership, sharing, starred/shared state and document lifecycle references.

## API boundary
PDF Services processing and Acrobat Sign agreements are not automatically generic Document Cloud file storage CRUD.

OAuth, tokens, scopes, clients, endpoints and external requests belong to `backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`. This package owns normalized storage metadata, object identity, version/lifecycle metadata, registry and readiness contract.

## Files
- `models.py`: validated storage object metadata
- `registry.py`: thread-safe in-memory metadata registry (not production persistence)
- `service.py`: metadata registration and readiness service
- `manifest.json`: machine-readable scope and status
- `tests/test_foundation.py`: offline tests

## Status
Foundation only; external connection `NOT_CONFIGURED`. A healthy local package does not prove entitlement, API availability, OAuth success or working file operations. Production persistence belongs in the central database. Never commit credentials or personal data.
