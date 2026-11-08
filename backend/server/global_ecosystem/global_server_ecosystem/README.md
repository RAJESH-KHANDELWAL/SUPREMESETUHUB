# GLOBAL SERVER ECOSYSTEM

Independent SERVER-owned coordination boundary for five existing backend layers.

## Ownership
- API: HTTP routes, schemas and transport.
- CORE: domain contracts, models, rules and policies.
- ENGINE: execution and provider adapters.
- DATABASE: durable structured records.
- STORAGE: files, objects and artifacts.
- SERVER: coordinates explicitly injected adapters and reports readiness.

SERVER does not copy layer code or data, own provider catalogs, persist server
inventory, or store artifacts. Its in-memory adapter registry is process-local.

## Safety
Importing this package does not connect to a provider, provision a machine,
access secrets, connect to a database, or write storage. Adapters must be
explicitly configured and authorized. Missing adapters are NOT_CONNECTED.

## Tests
Run `python -m pytest backend/server/global_ecosystem/global_server_ecosystem/test_server.py -q`.
