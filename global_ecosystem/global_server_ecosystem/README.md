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

## Provider-wise ecosystem hierarchy

The canonical SERVER-layer provider package convention mirrors the sibling
API, CORE, ENGINE and DATABASE server ecosystems:
`<provider>_server_server_ecosystem/`.

Each provider package contains:
- `__init__.py`: public namespace exports
- `provider.py`: binding to the existing SERVER provider adapter

Canonical provider packages:
- `abelohost_server_server_ecosystem/`
- `aws_server_server_ecosystem/`
- `azure_server_server_ecosystem/` (additional)
- `cloudflare_server_server_ecosystem/`
- `digitalocean_server_server_ecosystem/`
- `google_server_server_ecosystem/`
- `hostinger_server_server_ecosystem/` (additional)
- `microsoft_server_server_ecosystem/`
- `vicetemple_server_server_ecosystem/`

The common baseline of seven providers matches API, CORE, ENGINE and DATABASE.
Azure and Hostinger remain additional SERVER catalog entries. The older
`<provider>_server_ecosystem/` service-family taxonomy packages and
`<provider>_server/` adapters are retained for compatibility; they are not
the canonical layer-shaped provider namespaces. Provider namespace creation
does not imply that every provider supports every server service or that a
live connection/provisioning adapter exists.

## Complete folder map checked against sibling layers

The sibling layer roots were inspected recursively, including provider folders
and the shared directories. Their actual provider baseline is seven names:
`abelohost`, `aws`, `cloudflare`, `digitalocean`, `google`,
`microsoft`, and `vicetemple`.

Their provider-folder contents differ by owning layer:
- API: one provider-specific `<provider>_server_api_ecosystem.py` file.
- CORE: `__init__.py` and `.gitkeep`.
- ENGINE: `__init__.py` and `engine.py`.
- DATABASE: `__init__.py` and `.gitkeep`.
- STORAGE: the inspected SERVER STORAGE root currently contains only
  `README.md`; it has no provider folders to copy.

SERVER has its own provider-layer package entrypoints. Each
`<provider>_server_server_ecosystem/` contains:
- `__init__.py`: public SERVER provider namespace
- `provider.py`: binding to the existing SERVER adapter
- `server.py`: SERVER-layer entrypoint and provider metadata

The seven-provider baseline is present. Azure and Hostinger are retained as
additional SERVER catalog providers because they already existed in this
SERVER domain; they are not part of the seven-provider sibling baseline.

SERVER shared folders were also inspected:
- `integrations/`: `__init__.py`, `provider_gateway.py`
- `services/`: `__init__.py`, `runtime_service.py`
- `tools/`: `__init__.py`, `diagnostics.py`
- `providers/`: SERVER provider catalog namespace

These SERVER-owned implementations are retained rather than replaced with
other layers' files. Their folder names follow the sibling layout, while
their contents remain specific to SERVER responsibilities.

## SERVER service-type packages

The service taxonomy has dedicated SERVER-owned packages: `vpn_server/`, `vps_server/`, `cloud_server/`, `web_server/`, `cloud_web_server/`, `dedicated_server/`, `edge_server/`, `application_server/`, and `database_server/`. Each package declares its service-type identity and ownership boundary. These are taxonomy/contract namespaces, not claims of live provisioning or hosting.

## Runtime and provider status

The SERVER domain reports `NOT_CONFIGURED` when no provider adapters have been
explicitly registered, and `CONFIGURED` when at least one adapter is registered.
Neither state claims that a remote provider is reachable or healthy.

Provider catalog entries are not live integrations. Provider handlers must be
explicitly injected. Unconfigured providers and operations fail closed; no
cloud action is simulated. A registered handler is not proof of a successful
external connection: `external_connections` remains `NOT_ATTEMPTED` until a
real, separately implemented health probe is deliberately invoked.

Runtime registry entries are process-local and are not durable persistence.
No credentials or external connections are attempted by importing this package.
Runtime diagnostics describe the local application process only; they do not
probe the health of a remote server node.

## Operational capability boundary

The capability catalog defines SERVER-owned responsibility areas such as
provisioning, deployment, networking, monitoring, security, backup and scaling.
These are routing contracts, not claims that each provider supports every
operation. Concrete provider handlers must validate operation names, payloads,
authorization, and provider-specific capabilities before performing changes.

Read-only diagnostics and catalog tools must not invoke mutating operations.
Credential storage, durable node persistence, remote health probes, provider
authentication, provisioning and deployment require explicit production
integrations and configuration.

## Offline tests

Run from the repository root:

```bash
python -m unittest backend.server.global_ecosystem.global_server_ecosystem.test_server backend.server.global_ecosystem.global_server_ecosystem.test_registry backend.server.global_ecosystem.global_server_ecosystem.test_runtime backend.server.global_ecosystem.global_server_ecosystem.test_operations backend.server.global_ecosystem.global_server_ecosystem.test_provider_ecosystems
```


## Public SERVER service integration

The package is the provider/runtime coordination layer consumed by
`backend.server.ServerService`. Its provider registry, gateway and operation
service are surfaced through the SERVER manager/controller. Provider health
is `NOT_PROBED` until a provider-specific real health probe is implemented;
registration alone never proves external connectivity. All remote operations
remain fail-closed until an explicit adapter is registered.
