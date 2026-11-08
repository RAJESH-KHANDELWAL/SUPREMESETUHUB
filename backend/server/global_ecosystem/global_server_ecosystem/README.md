# GLOBAL SERVER ECOSYSTEM

Independent SERVER orchestration layer:
`backend/server/global_ecosystem/global_server_ecosystem/`

## Ownership and boundaries

- **API** owns HTTP routes, request/response schemas and transport.
- **CORE** owns provider-neutral domain models, validation, lifecycle rules and policy.
- **ENGINE** owns execution engines and concrete provider execution adapters.
- **DATABASE** owns durable structured records and database access.
- **STORAGE** owns file, object and artifact persistence.
- **SERVER** owns cross-layer composition, adapter registration, orchestration,
  lifecycle coordination, provider integration entry points and capability routing.

SERVER does not copy the implementation of another layer. All five layer adapters
are explicitly injected. CORE validation and ENGINE dispatch remain separate.
DATABASE record reads and STORAGE artifact resolution are routed only through
their respective registered adapters.

## Provider alignment

The canonical provider IDs match the GLOBAL SERVER CORE and ENGINE provider set:
Abelohost, AWS, Cloudflare, DigitalOcean, Google, Microsoft and ViceTemple.

Azure and Hostinger are retained as additional SERVER-specific catalog entries
for backward compatibility; they are not represented as members of the peer
layers' canonical seven-provider set.

Provider packages expose a common SERVER adapter contract. A provider is
`NOT_CONFIGURED` until a callable handler is explicitly injected. This package
does not create credentials, contact cloud APIs or simulate infrastructure
operations.

## SERVER-owned modules

- `catalog.py`: five layer ownership descriptors, canonical/additional providers,
  and server service-type catalog.
- `contracts.py`: protocols for API, CORE, ENGINE, DATABASE, STORAGE and providers.
- `models.py`: orchestration request/result value objects.
- `registry.py`: thread-safe five-layer adapter registry.
- `provider_base.py`: common fail-closed provider adapter contract.
- `provider_registry.py`: validated provider registration and connection status.
- `operation_catalog.py` / `operations.py`: provisioning, deployment, networking,
  monitoring, security, backup and scaling capability routing.
- `service.py` / `manager.py`: composition, dispatch, health and adapter access.
- `runtime.py`: read-only process diagnostics.
- `*_server/`: provider integration entry points.
- `layers/`, `providers/`, `integrations/`: extension namespaces.

## Operational truth

Catalog presence is not proof of provider support or a live connection.
A registered adapter is not proof that its credentials or remote service work;
that must be verified by the adapter implementation. Unconfigured operations fail
closed. Importing SERVER does not access secrets, provision infrastructure, write
DATABASE records, or upload STORAGE artifacts. Runtime diagnostics describe only
the current application process.

## Offline tests

```bash
python -m unittest backend.server.global_ecosystem.global_server_ecosystem.test_server backend.server.global_ecosystem.global_server_ecosystem.test_registry backend.server.global_ecosystem.global_server_ecosystem.test_runtime backend.server.global_ecosystem.global_server_ecosystem.test_operations
```
