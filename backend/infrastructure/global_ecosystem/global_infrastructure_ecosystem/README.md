# GLOBAL INFRASTRUCTURE ECOSYSTEM

Central integration and discovery layer for every domain currently maintained by `backend/infrastructure/`.

## Actual in-ecosystem structure

- `domains/<domain>/` contains a lazy adapter package for each of the 21 canonical infrastructure domains.
- `modules/` exposes lazy loaders for the six infrastructure root modules: controller, Hostinger API, Hostinger catalog, NSFWinfra, repository and service.
- `integrations/core/` loads the existing `backend.core` foundation.
- `integrations/global_core_ecosystem/` loads the existing GLOBAL CORE ECOSYSTEM and its dedicated GLOBAL INFRASTRUCTURE CORE ECOSYSTEM validation package.
- `structure.py` records both canonical source paths and the in-ecosystem adapter paths.

## Domain coverage

Backup, Billing, CDN, Containers, Database, DNS, Domains, Email, Firewall, FTP, Hosting, IPAM, Load Balancer, Model, Monitoring, Network, Object Storage, Security, Server, SSL and Storage.

## Ownership and preservation

The original `backend/infrastructure/<domain>/` implementations remain in place and are canonical. The ecosystem adapters load those packages lazily; they do not fork or duplicate the implementation. Root-level infrastructure modules likewise remain canonical under `backend/infrastructure/`.

CORE remains canonical in `backend/core/`. GLOBAL CORE ECOSYSTEM remains canonical in `backend/core/global_ecosystem/global_core_ecosystem/`. Its dedicated infrastructure contract is `global_infrastructure_core_ecosystem/`. The adapters provide stable integration entry points without moving CORE ownership into Infrastructure.

Database persistence remains in `backend/database/`; storage runtime remains in `backend/storage/`; server ecosystem remains in `backend/server/`; executable operations remain in ENGINE; HTTP orchestration remains in API.

## Safety

A registered adapter is not proof of a live provider connection. Provider actions require configured credentials, scoped authorization, audit logging, tests and verified connectivity. No credentials or destructive provider operations are enabled by this catalog.

Status: domain adapter structure and cross-layer integration entry points registered. Runtime/provider connectivity is not asserted.
