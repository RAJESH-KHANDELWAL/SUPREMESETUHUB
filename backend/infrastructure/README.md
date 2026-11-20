# SUPREMESETUHUB Backend Infrastructure

## Canonical ownership
The canonical Infrastructure control-plane implementation is owned by the Global Infrastructure Ecosystem:

`backend/infrastructure/global_ecosystem/global_infrastructure_ecosystem/modules/`

Canonical modules:
- `controller.py` — resource controller
- `repository.py` — database-backed infrastructure resource repository
- `service.py` — validation and resource service layer
- `hostinger_catalog.py` — Hostinger service catalog/readiness metadata

The former implementation files at this package root have been replaced with thin compatibility shims only. They preserve existing import paths but do not own duplicate implementation code.

## Other ecosystem modules
- `global_ecosystem/hostinger_api.py`: read-only Hostinger inventory API client.
- `global_ecosystem/nsfwinfra.py`: NSFWInfra API helper; connection is not verified.
- `global_ecosystem/global_infrastructure_ecosystem/`: 21 domain packages, their ecosystem support modules, integrations, catalog, managers and structure metadata.

## Managers
The Python and PHP root managers verify canonical module presence, package compatibility entry point, Hostinger API and NSFWinfra helper files, and the Global Infrastructure Ecosystem manager. Structural health is not proof of runtime tests or provider connectivity.

## Cross-layer ownership
- CORE and identity/policy: `backend.core`
- Global Ecosystem root: `backend.global_ecosystem`
- Database persistence: `backend.database`
- Storage runtime: `backend.storage`
- Server ecosystem: `backend.server.global_ecosystem.global_server_ecosystem`
- HTTP orchestration: `backend.api`
- Executable provider operations: `backend.engine`

Catalog entries do not prove provider connectivity. Live provider operations require supported APIs, configured credentials, scoped authorization, audit logging, tests and verified connectivity. Never commit credentials, tokens, private keys or customer data.
