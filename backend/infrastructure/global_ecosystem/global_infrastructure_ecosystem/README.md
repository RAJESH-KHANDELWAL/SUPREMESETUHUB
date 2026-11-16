# GLOBAL INFRASTRUCTURE ECOSYSTEM

Central integration and discovery layer for every domain currently maintained by `backend/infrastructure/`.

## Direct root-level domain structure

The 21 infrastructure domain folders are placed directly inside this ecosystem root, matching the layout of `backend/infrastructure/`. There is deliberately no intermediate `domains/` directory.

- `backup/`, `billing/`, `cdn/`, `containers/`, `database/`, `dns/`, `domains/`
- `email/`, `firewall/`, `ftp/`, `hosting/`, `ipam/`, `load_balancer/`, `model/`
- `monitoring/`, `network/`, `object_storage/`, `security/`, `server/`, `ssl/`, `storage/`

Each folder is a lazy adapter that points to its canonical implementation in `backend/infrastructure/<domain>/`; implementation is not duplicated.

## Supporting ecosystem structure

- `modules/` exposes lazy loaders for six existing infrastructure root modules: controller, Hostinger API, Hostinger catalog, NSFWinfra, repository and service.
- `integrations/core/` loads the existing `backend.core` foundation.
- `integrations/global_core_ecosystem/` loads the existing GLOBAL CORE ECOSYSTEM and its dedicated GLOBAL INFRASTRUCTURE CORE ECOSYSTEM validation package.
- `structure.py` records canonical source paths and direct ecosystem package paths.

## Ownership and preservation

The original `backend/infrastructure/<domain>/` implementations remain in place and canonical. Ecosystem folders provide stable discovery/integration entry points without forking or duplicating runtime code. Root-level infrastructure modules likewise remain canonical under `backend/infrastructure/`.

CORE remains canonical in `backend/core/`. GLOBAL CORE ECOSYSTEM remains canonical in `backend/core/global_ecosystem/global_core_ecosystem/`. Its dedicated infrastructure contract is `global_infrastructure_core_ecosystem/`.

Database persistence remains in `backend/database/`; storage runtime remains in `backend/storage/`; server ecosystem remains in `backend/server/`; executable operations remain in ENGINE; HTTP orchestration remains in API.

## Safety

A registered adapter is not proof of a live provider connection. Provider actions require configured credentials, scoped authorization, audit logging, tests and verified connectivity. No credentials or destructive provider operations are enabled by this catalog.

Status: direct root-level domain adapters and cross-layer integration entry points registered. Runtime/provider connectivity is not asserted.
