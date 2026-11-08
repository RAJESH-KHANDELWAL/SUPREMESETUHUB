# GLOBAL SERVER ECOSYSTEM

Independent SERVER layer at `backend/server/global_ecosystem/global_server_ecosystem/`.

## Ownership boundaries
- API owns HTTP routes, schemas and transport.
- CORE owns domain contracts, models, rules and policies.
- ENGINE owns execution and provider adapters.
- DATABASE owns durable structured records and database access.
- STORAGE owns files, objects and artifact persistence.
- SERVER owns cross-layer orchestration, adapter registration, lifecycle and composition.

SERVER does not copy another layer's implementation, models, records, provider
execution engines, or storage implementation.

## Package structure
- `catalog.py`: five-layer ownership and server-provider metadata.
- `contracts.py`: SERVER-owned adapter protocols.
- `models.py`: SERVER orchestration request/result types.
- `registry.py`: explicitly injected layer adapter registry.
- `provider_registry.py`: server-provider integration registry.
- `manager.py`: lifecycle facade.
- `service.py`: readiness and orchestration service.
- `layers/`, `providers/`, `integrations/`: extension namespaces.
- `aws_server/`, `azure_server/`, `digitalocean_server/`, `google_server/`,
  `hostinger_server/`: existing provider integration packages.

Provider folders are retained. Their existing integrations remain NOT_CONFIGURED
until credentials and adapters are explicitly supplied. Importing this package
does not contact providers, provision infrastructure, access secrets, connect to
databases, or write to storage.

## Tests
Run `python -m unittest backend.server.global_ecosystem.global_server_ecosystem.test_server backend.server.global_ecosystem.global_server_ecosystem.test_registry`.
