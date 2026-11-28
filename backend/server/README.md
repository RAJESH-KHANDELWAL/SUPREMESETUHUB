# SERVER — MAIN BASE FOUNDATION

SERVER is an independent backend domain at the same architectural level as API,
CORE, ENGINE, DATABASE and STORAGE.

## SERVER domain modules

- `config.py`, `models.py`, `exceptions.py`: configuration and domain types
- `contracts.py`: explicit repository, provider and lifecycle interfaces
- `registry.py`: default in-process inventory (non-durable)
- `lifecycle.py`: control-plane lifecycle state transitions
- `health.py`: runtime, inventory and provider health aggregation
- `service.py`, `manager.py`, `controller.py`: complete inventory CRUD, control-plane lifecycle, provider gateway and capability dispatch interfaces
- `operation_catalog.py`: SERVER capability catalog
- `operations.py`: fail-closed adapter registry and operational dispatcher
- `global_ecosystem/global_server_ecosystem/`: global provider ecosystem,
  provider registry, layer adapters and orchestration contracts

## Operational capability domains

SERVER now has explicit boundaries for:
- Provisioning and deprovisioning
- Application deployment and rollback
- Networking, DNS, addressing and firewall integrations
- Monitoring, metrics and operational events
- Security and access-policy integrations
- Backup and recovery
- Capacity and scaling

These are capability boundaries, not claims that remote operations are already
connected. Each operation requires an explicitly registered adapter owned by
the relevant provider or infrastructure integration. An unconfigured capability
fails closed instead of pretending that a server was provisioned or deployed.

## Layer ownership

- API owns HTTP routes, schemas and transport.
- CORE owns foundation rules and policies.
- ENGINE owns execution engines.
- DATABASE owns durable structured records and database access.
- STORAGE owns file/object and artifact persistence.
- SERVER owns server inventory, lifecycle orchestration, provider coordination,
  deployment/networking/monitoring/security control-plane boundaries.

SERVER does not copy the implementation of API, CORE, ENGINE, DATABASE or
STORAGE. Cross-layer connections use explicit contracts and injected adapters.

## Current operational limitations

The default inventory registry is in-memory and is not durable across restarts.
Lifecycle methods update control-plane status only; they do not power on/off
remote machines. Provider catalog entries do not prove live connectivity.
Durable inventory requires a DATABASE adapter; artifact persistence requires a
STORAGE adapter; actual infrastructure actions require configured provider
adapters and credentials. No secrets or external services are accessed at import.


## Completed SERVER application surface

The public `ServerService`, `ServerManager` and `ServerController` expose:
- Inventory create, read, list, update and local-record delete.
- Start, stop and restart request-state transitions.
- Provider registration, provider description, health status and explicit operation dispatch.
- Capability adapter registration and operation dispatch.
- Read-only health and runtime diagnostics.

Provider handlers and capability adapters must be explicitly injected. A
configured handler is reported as `NOT_PROBED`, not as a reachable provider.
Inventory deletion and lifecycle state changes affect SERVER metadata only;
they do not delete, start, stop or restart remote infrastructure.
