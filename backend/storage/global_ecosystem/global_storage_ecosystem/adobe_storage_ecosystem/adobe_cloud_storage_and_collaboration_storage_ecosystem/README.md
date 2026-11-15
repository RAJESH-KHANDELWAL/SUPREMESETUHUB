# Adobe Cloud Storage and Collaboration

Provider: Adobe  
Storage namespace: `cloud_storage_and_collaboration`  
Related API family: Creative Cloud and Assets APIs

## Responsibility
Shared cloud-storage and collaboration metadata, projects, folders, supported cloud documents, ownership and permissions.

## API boundary
No universal Adobe Drive or generic file CRUD API is implied.

OAuth, tokens, scopes, clients, endpoints and external requests belong to `backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`. This package owns storage metadata, object identity, version/lifecycle metadata, registry and readiness contract.

## Files
- `models.py`: validated storage object metadata
- `registry.py`: thread-safe in-memory metadata registry (not production persistence)
- `service.py`: metadata registration and readiness service
- `config.py`: safe environment-only runtime configuration\n- `adapter_contract.py`: abstract storage operations contract; concrete clients stay in the API/integration layer\n- `manifest.json`: machine-readable scope and status
- `tests/test_foundation.py`: offline tests

## Status
Foundation only; external connection `NOT_CONFIGURED`. A healthy local package does not prove entitlement, API availability, OAuth success or working file operations. Production persistence belongs in the central database. Never commit credentials or personal data.
