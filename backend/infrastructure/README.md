# SUPREMESETUHUB Infrastructure

This package is the infrastructure control-plane layer. It inventories resources and
provides safe adapters for checking infrastructure connectivity. It is not a replacement
for the existing backend database, storage, hosting, or deployment implementations.

## Existing modules retained

- `database/` at `backend/database/`: current application database implementations and configuration.
- `ftp/healthcheck.py`: existing read-only explicit-FTPS connectivity check.
- `hosting/`, `server/`, `network/`, `domains/`, `dns/`: infrastructure inventory and lifecycle records.
- `storage/`, `object_storage/`, `backup/`: storage and backup inventory/services.
- `security/`, `firewall/`, `ssl/`: security-related inventory/services.
- `monitoring/`: monitoring configuration/records.
- `hostinger_api.py`: existing Hostinger API integration.

These modules are retained in place. Their presence does not by itself prove that a real
provider operation is connected or enabled; inventory records and live provider actions
are separate capabilities.

## Server domain integration

`backend/infrastructure/server/` keeps its existing SQL-backed infrastructure inventory
and now exposes the independent `backend/server/` domain through
`ServerDomainIntegration` and `ServerController.domain`.

The integration is a facade, not a second copy of the SERVER domain. The canonical
implementation and its `global_ecosystem/global_server_ecosystem/` provider hierarchy
remain under `backend/server/`. Both packages remain present and retain separate
responsibilities:

- Infrastructure inventory: existing database-backed physical/virtual/dedicated server records.
- SERVER domain: domain registry, lifecycle state, provider gateway, capability adapters,
  and global provider ecosystem.

Use the controller's explicit `*_domain_*` methods for the canonical domain so that its
records are not confused with the legacy infrastructure SQL inventory. Domain lifecycle
and delete calls update control-plane metadata only; remote infrastructure changes still
require explicitly configured provider/operation adapters. The public HTTP collection
route `/infrastructure/servers` remains unchanged.

## Added safe adapters

- `database/`: explicit health adapter for the existing SQLite runtime service (when
  injected) and the existing central MySQL connection implementation.
- `ftp/profiles.py` and `ftp/service.py`: named profiles for the FTP environment
  variables already used by the Hostinger deployment workflows. Secrets remain in
  environment variables and are never returned by the adapter.
- `monitoring/probes.py`: read-only HTTP(S) HEAD probes.
- `server/healthcheck.py`: TCP port reachability checks without login or commands.
- `dns/healthcheck.py`: operating-system resolver checks (not authoritative-zone verification).
- `ssl/healthcheck.py`: CA- and hostname-verified TLS certificate expiry checks.

## Boundaries

1. Keep database connection/schema ownership in `backend/database/`; do not create a
   second database engine in this package.
2. Keep the existing FTP healthcheck as the protocol implementation. The new FTP service
   only resolves known environment profiles and delegates to that check.
3. Health checks are read-only. They do not upload, delete, rename, provision, migrate,
   or modify remote resources.
4. Never commit credentials, tokens, private keys, or customer data.
5. Add real provider actions only behind explicit authorization, scoped identities,
   audit logging, and tests.
6. SQLite remains the current `DatabaseService` runtime implementation. The MySQL
   adapter reports connectivity only; it does not switch application queries to MySQL.
