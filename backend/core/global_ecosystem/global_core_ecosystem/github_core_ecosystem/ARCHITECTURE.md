# GitHub CORE Architecture

GitHub CORE is the provider control plane above 12 family packages. It follows the same separation of concerns as Google Core: a canonical provider catalog, stable contracts, policy guardrails, a read-only orchestrator, a service facade and one public manager entry point.

## Request and discovery flow

1. The application authenticates the caller and supplies tenant/actor context.
2. `GitHubCoreManager` delegates status and discovery to the Core service/orchestrator.
3. Core resolves a registered family and validates metadata/request shape only.
4. API/Integration authenticates to GitHub and performs a specific REST/GraphQL operation.
5. ENGINE owns retries, rate-limit backoff, asynchronous jobs and webhook delivery.
6. DATABASE/STORAGE own persistence and artifacts.
7. The application presents the result.

## Core public API

- `get_manager()` returns the canonical `GitHubCoreManager`.
- `status()` returns provider registry and readiness metadata.
- `health()` reports family counts, declared route coverage and explicit zero Core API calls.
- `list_families()` / `get_family()` discover registered API families.
- `list_offerings()` / `get_offering()` expose the unified family inventory.
- `dependency_map()` describes Core-to-API delegation edges.

## Ownership boundaries

| Component | Owns |
|---|---|
| `manager.py` | stable public entry point |
| `catalog.py` | canonical provider and family registry |
| `contracts.py` / `request_contracts.py` | tenant, result, secret-reference and request-shape contracts |
| `policy.py` | Core metadata guardrails; not provider authorization |
| `orchestrator.py` | read-only discovery, health and dependency metadata |
| `service.py` | provider status and service facade |
| API / Integration | GitHub credentials, authentication, REST/GraphQL calls and endpoint adapters |
| ENGINE | jobs, retries, rate-limit scheduling and webhook execution |

## Existing API boundary

Shared authenticated REST transport exists at `backend/integration/provider/github.py`. Routes in `backend/api/connectors.py` currently expose authenticated connection status, account identity, repository listing and repository metadata. Family-specific endpoint coverage must be verified independently.

## Security invariants

- Core never reads environment secrets, constructs Authorization headers or resolves secret references.
- Core never calls GitHub, writes repository data or executes jobs.
- Tenant and actor context must be supplied by the authenticated application.
- Sensitive operations require explicit provider authorization and audit in the API/application layers.
- Catalog registration and route declarations are not proof of live authentication or complete API coverage.
