# SUPREME API ECOSYSTEM

Canonical API package: `backend/supreme/supreme_ecosystem/supreme_api_ecosystem/`

This package is the API boundary of the SUPREME ecosystem. It owns HTTP-facing contracts and transport concerns—not core business logic, execution engines, or persistence.

## API responsibilities
- API application and router composition
- Route definitions and versioning
- Request parsing and validation
- Response schemas and consistent error contracts
- API middleware, request context, and correlation identifiers
- OpenAPI/API documentation
- Health/readiness and API-level status endpoints
- Adapter interfaces for calling separately owned services

## Independent layer ownership

| Layer | Responsibility | API relationship |
|---|---|---|
| API | HTTP transport, routes, validation, serialization | Owns this package |
| AUTHENTICATION | Identity verification and sessions | API delegates through interfaces |
| AUTHORIZATION | Access policies and permission checks | API enforces decisions through interfaces |
| CORE | Domain models and business rules | Must not be duplicated or absorbed by API |
| ENGINE | Execution and orchestration | API invokes through defined contracts |
| DATABASE | Persistence, repositories and migrations | API does not own database implementation |

## Package map
- `contracts.py` — API identity, version and layer boundaries
- `routers/` — route modules grouped by API domain
- `schemas/` — request and response schemas
- `middleware/` — transport-level middleware
- `dependencies/` — dependency wiring and boundary adapters
- `docs/` — API conventions and documentation
- `tests/` — API contract and routing tests

## Runtime status
The repository's existing API entry points are catalogued by the parent ecosystem registry. This package establishes the canonical SUPREME API namespace and contract. It does not claim every route, integration, or runtime adapter is implemented or mounted.

## Rules
1. Do not import database internals directly into route modules.
2. Do not move CORE or ENGINE code into this package.
3. Keep authentication and authorization separate.
4. Validate untrusted request data at the API boundary.
5. Never return secrets, tokens, private credentials, or raw internal exceptions.
6. Version externally consumed contracts and keep error responses predictable.
