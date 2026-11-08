# SERVER — MAIN BASE FOUNDATION

SERVER is an independent backend domain, structured at the same architectural
level as API, CORE, ENGINE, DATABASE and STORAGE.

## Domain layout

- `config.py`: runtime configuration
- `models.py`: server inventory models and request objects
- `contracts.py`: repository, provider and lifecycle contracts
- `exceptions.py`: typed domain errors
- `registry.py`: default in-process inventory registry
- `lifecycle.py`: server lifecycle state transitions
- `health.py`: health aggregation
- `service.py`: SERVER application service
- `manager.py`: lifecycle and management facade
- `controller.py`: framework-neutral controller
- `global_ecosystem/global_server_ecosystem/`: provider catalog, adapters,
  layer contracts, orchestration and cloud-provider ecosystem

## Public entry point

```python
from backend.server import ServerManager

server = ServerManager()
record = server.register(name="Primary Web", server_type="WEB")
print(server.get(record["server_id"]))
print(server.health())
```

## Layer boundaries

- API owns HTTP routes and transport.
- CORE owns foundation rules and policies.
- ENGINE owns execution engines.
- DATABASE owns durable structured data.
- STORAGE owns file and object persistence.
- SERVER owns server inventory, provider integration boundaries, server
  lifecycle orchestration, deployment and runtime control-plane concerns.

SERVER does not copy API, CORE, ENGINE, DATABASE or STORAGE implementations.
They remain independent and can be connected through explicit adapter contracts
at the application composition root.

## Current operational limitations

The default inventory registry is in-memory and is not durable across restarts.
Lifecycle methods only update control-plane status; they do not provision,
start or stop remote machines. Provider entries in the catalog are not proof
of live provider connectivity. Durable inventory and live provisioning require
explicit DATABASE and provider adapters.
