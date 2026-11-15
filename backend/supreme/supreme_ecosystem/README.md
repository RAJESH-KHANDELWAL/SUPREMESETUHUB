# SUPREME ECOSYSTEM

The SUPREME ECOSYSTEM is a domain/system namespace under the parent SUPREME layer.

## Architecture map
- `supreme_api_ecosystem/` — canonical SUPREME API ECOSYSTEM: HTTP routes, request/response contracts, middleware, and API documentation.
- `core/` — SUPREME ecosystem core namespace; remains independent of API.
- `engines/` — SUPREME ecosystem execution engines; remain independent of API and CORE.
- `database/` — SUPREME ecosystem persistence namespace; remains independent of API and ENGINE.
- `auth/`, `authentication/`, `authorization/`, `security/`, `permissions/`, `roles/`, `sessions/` — security and identity namespaces. Authentication and authorization are separate concerns.
- `connectors/`, `integrations/`, `providers/` — external integration boundaries.
- `schemas/`, `responses/`, `middleware/`, `routers/` — ecosystem-level namespaces; API-specific contracts are owned by `supreme_api_ecosystem/`.

## Boundary rules
1. API does not contain CORE business logic.
2. API does not contain ENGINE execution logic.
3. API does not own DATABASE schemas, repositories, migrations, or connection internals.
4. CORE, ENGINE, DATABASE, AUTHENTICATION, and AUTHORIZATION remain independent layers.
5. Cross-layer communication uses explicit interfaces and dependency wiring.
6. Existing domain modules and integrations remain in their current locations unless a reviewed migration updates every import and test.

See `supreme_api_ecosystem/README.md` for the SUPREME API ECOSYSTEM ownership, package map, and development rules.
