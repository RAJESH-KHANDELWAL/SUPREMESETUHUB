# GLOBAL SERVER ECOSYSTEM

Canonical implementation of the SERVER domain.

## Ownership
- Provider and service-type catalog metadata.
- Local server inventory registration, lookup, listing and lifecycle flags.
- Input validation, duplicate protection and thread-safe in-memory inventory.
- Ecosystem status and health reporting.
- Provider adapter execution remains an ENGINE concern; API, CORE, DATABASE and STORAGE remain separate owners.

## Provider truthfulness
Catalog entries are metadata, not proof of an account connection or SDK capability. No remote host is provisioned or monitored by this package. The in-memory registry is process-local and is not durable across restarts. Live provisioning and reachability must be implemented only through separately configured, authorized adapters and infrastructure.

## Compatibility
The lowercase package under `backend/server` is a compatibility facade that imports this canonical package.

## Tests
`python -m pytest backend/SERVER/GLOBAL_ECOSYSTEM/GLOBAL_SERVER_ECOSYSTEM backend/server/global_ecosystem/global_server_ecosystem -q`
