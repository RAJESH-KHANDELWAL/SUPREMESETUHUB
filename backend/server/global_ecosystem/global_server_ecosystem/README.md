# GLOBAL SERVER ECOSYSTEM

Independent SERVER domain and runtime setup:
`backend/server/global_ecosystem/global_server_ecosystem/`

## Independent ownership

SERVER is a peer backend domain with its own setup. It does not contain, copy,
wrap, instantiate, or orchestrate API, CORE, ENGINE, DATABASE, or STORAGE
implementations. Those remain independent systems in their own directories.

SERVER owns its runtime identity, server-node registry, provider integrations,
capability catalog, operation routing, runtime diagnostics, contracts, models,
services, manager, tools, and tests.

## SERVER structure

- `catalog.py`: SERVER provider catalog and server-service taxonomy.
- `contracts.py`: SERVER provider, runtime and operation contracts only.
- `models.py`: SERVER-owned node and health value objects.
- `registry.py`: in-process registry for SERVER runtime nodes.
- `provider_base.py`: fail-closed provider adapter base.
- `provider_registry.py`: provider validation, registration and status.
- `operation_catalog.py` / `operations.py`: SERVER capability definitions and
  explicitly configured operation routing.
- `service.py` / `manager.py`: SERVER runtime service and manager.
- `services/`: SERVER runtime diagnostics service.
- `integrations/`: SERVER provider integration gateway and provider adapters.
- `tools/`: read-only SERVER diagnostics and catalog tools.
- `*_server/`: provider-specific SERVER integration packages.
- `providers/`: provider catalog namespace.

## Provider and operation safety

Catalog entries are not live integrations. Provider handlers must be explicitly
injected. Unconfigured operations fail closed; no cloud action is simulated.
Runtime registry entries are process-local and are not durable persistence.
No credentials or external connections are attempted by importing this package.

## Offline tests

```bash
python -m unittest backend.server.global_ecosystem.global_server_ecosystem.test_server backend.server.global_ecosystem.global_server_ecosystem.test_registry backend.server.global_ecosystem.global_server_ecosystem.test_runtime backend.server.global_ecosystem.global_server_ecosystem.test_operations
```
