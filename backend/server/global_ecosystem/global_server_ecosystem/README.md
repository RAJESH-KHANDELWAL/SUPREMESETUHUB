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

Each registered provider has a canonical `<provider>_server_ecosystem/` package.
Inside it, provider-scoped service-family namespaces follow the
`<provider>_<service>_server_ecosystem/` convention.

Provider roots:
- `abelohost_server_ecosystem/`
- `aws_server_ecosystem/`
- `azure_server_ecosystem/` (additional integration; distinct from Microsoft canonical entry)
- `cloudflare_server_ecosystem/`
- `digitalocean_server_ecosystem/`
- `google_server_ecosystem/`
- `hostinger_server_ecosystem/`
- `microsoft_server_ecosystem/`
- `vicetemple_server_ecosystem/`

Each provider root contains the SERVER service-family namespaces:
`vpn`, `vps`, `cloud`, `web`, `cloud_web`, `dedicated`, `edge`,
`application`, and `database`. For example:
`aws_server_ecosystem/aws_vps_server_ecosystem/`.

These packages establish ownership and naming boundaries only. A namespace
does not assert that a provider offers that service, nor that provisioning,
authentication, monitoring, or remote execution is implemented. Provider
support must be verified against the provider's actual product/API and wired
through an explicit, fail-closed adapter. Existing `*_server/` packages remain
as compatibility adapter packages; they are not deleted or silently moved.

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
python -m unittest backend.server.global_ecosystem.global_server_ecosystem.test_server backend.server.global_ecosystem.global_server_ecosystem.test_registry backend.server.global_ecosystem.global_server_ecosystem.test_runtime backend.server.global_ecosystem.global_server_ecosystem.test_operations
```
