# GLOBAL SERVER ECOSYSTEM

Canonical SERVER-domain implementation lives in this package.

## Responsibilities
- Provider catalog and server service-type taxonomy.
- Thread-safe in-memory server inventory.
- Registration, lookup, listing, authorization-state and disable-state transitions.
- Ecosystem description and local inventory-health facade.
- Lowercase `backend.server` remains a compatibility namespace.

## Provider boundary
Catalog entries do not prove SDK support, connected provider accounts, remote provisioning, VPN tunnels, or host monitoring. Live provisioning belongs to separately implemented and securely configured runtime adapters. Local inventory health is not remote host reachability.

## Layer ownership
SERVER owns server inventory and lifecycle metadata. API, CORE, ENGINE and DATABASE remain independent. The duplicate `backend.servers` namespace is being retired after its useful registration and authorization behavior is integrated here.

## Tests
Run: `python -m pytest backend/SERVER/GLOBAL_ECOSYSTEM/GLOBAL_SERVER_ECOSYSTEM backend/server/global_ecosystem/global_server_ecosystem -q`
