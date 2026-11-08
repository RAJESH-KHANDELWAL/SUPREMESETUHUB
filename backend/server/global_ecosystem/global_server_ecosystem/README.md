# GLOBAL SERVER ECOSYSTEM

Independent SERVER orchestration layer at
`backend/server/global_ecosystem/global_server_ecosystem/`.

## Ownership boundaries

- API owns HTTP routes, schemas and transport.
- CORE owns domain contracts, models, rules and policies.
- ENGINE owns execution and concrete provider adapters.
- DATABASE owns durable structured records and database access.
- STORAGE owns files, objects and artifact persistence.
- SERVER owns cross-layer composition, adapter registration, orchestration,
  lifecycle coordination and capability routing.

SERVER connects to these layers through explicit injected contracts. It does not
copy their implementations, data models, database access, storage code, or
provider execution engines. CORE validation and ENGINE dispatch remain separate.

## Package modules

- `catalog.py`: layer ownership and provider metadata.
- `contracts.py`: SERVER-owned adapter protocols.
- `models.py`: orchestration request/result value objects.
- `registry.py`: explicitly injected API/CORE/ENGINE/DATABASE/STORAGE adapters.
- `provider_registry.py`: cloud/server provider adapter registration.
- `operation_catalog.py`: provisioning, deployment, networking, monitoring,
  security, backup and scaling capability definitions.
- `operations.py`: fail-closed execution through explicitly registered
  capability adapters.
- `manager.py` and `service.py`: composition, health and orchestration.
- `runtime.py`: read-only process diagnostics.
- `layers/`, `providers/`, `integrations/`: extension namespaces.
- `aws_server/`, `azure_server/`, `digitalocean_server/`, `google_server/`,
  `hostinger_server/`: provider integration packages.

## Safety and current implementation status

Catalog entries are capability definitions, not proof of live infrastructure.
Unregistered layer, provider and operation adapters remain disconnected.
Operational calls fail closed when their adapter is missing. Registered adapters
must implement the documented interface and own the actual remote action.
Importing this package does not contact providers, access secrets, provision
resources, connect to DATABASE, or write to STORAGE. Runtime diagnostics only
describe the current application process; they do not control remote servers.

DATABASE and STORAGE remain separate domains and must be injected through their
own adapters. No persistent SERVER inventory adapter is configured by default.

## Tests

Run:
`python -m unittest backend.server.global_ecosystem.global_server_ecosystem.test_server backend.server.global_ecosystem.global_server_ecosystem.test_registry backend.server.global_ecosystem.global_server_ecosystem.test_runtime backend.server.global_ecosystem.global_server_ecosystem.test_operations`
