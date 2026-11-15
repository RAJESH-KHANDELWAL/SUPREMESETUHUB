# Adobe Workfront Storage

Provider: Adobe  
Storage namespace: `workfront`  
Related API family: Requires separate Workfront API validation; current Adobe API catalog does not list a dedicated Workfront API child

## Responsibility
Workfront project asset references, documents, proofs, approvals, attachments and connected-storage relationships.

## API boundary
Distinguish Workfront workflow records from the service that stores binary assets. Verify Workfront API and connected storage permissions separately.

OAuth, tokens, scopes, clients, endpoints and external requests belong to `backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`. This package owns normalized storage metadata, object identity, version/lifecycle metadata, registry and readiness contract.

## Files
- `models.py`: validated storage object metadata
- `registry.py`: thread-safe in-memory metadata registry (not production persistence)
- `service.py`: metadata registration and readiness service
- `config.py`: safe environment-only runtime configuration\n- `adapter_contract.py`: abstract storage operations contract; concrete clients stay in the API/integration layer\n- `manifest.json`: machine-readable scope and status
- `tests/test_foundation.py`: offline tests

## Status
Foundation only; external connection `NOT_CONFIGURED`. A healthy local package does not prove entitlement, API availability, OAuth success or working file operations. Production persistence belongs in the central database. Never commit credentials or personal data.
