# GLOBAL INFRASTRUCTURE ECOSYSTEM

Canonical home for the 21 infrastructure domain implementations and their domain-specific ecosystem packages.

## Direct root-level domain structure

All 21 domain folders live directly inside this ecosystem root. There is no intermediate `domains/` wrapper:

- `backup/`, `billing/`, `cdn/`, `containers/`, `database/`, `dns/`, `domains/`
- `email/`, `firewall/`, `ftp/`, `hosting/`, `ipam/`, `load_balancer/`, `model/`
- `monitoring/`, `network/`, `object_storage/`, `security/`, `server/`, `ssl/`, `storage/`

Each folder contains its actual implementation files and its own `global_ecosystem/` substructure where present.

## Supporting ecosystem structure

- `modules/` exposes adapters for six infrastructure root modules: controller, Hostinger API, Hostinger catalog, NSFWinfra, repository and service.
- `integrations/` contains explicit CORE and GLOBAL CORE integration entry points.
- `structure.py` records canonical package paths and ownership.

## Ownership and compatibility

The 21 domain implementations are physically owned here. The parent `backend.infrastructure` package exposes this directory as a compatibility import path, so existing imports such as `backend.infrastructure.server` continue to resolve without retaining duplicate domain folders at the parent level.

Root-level infrastructure modules remain under `backend/infrastructure/`. CORE remains canonical in `backend/core/`; database persistence remains in `backend/database/`; storage runtime remains in `backend/storage/`; server ecosystem remains in `backend/server/`; executable operations remain in ENGINE; HTTP orchestration remains in API.

## Safety

A registered adapter is not proof of a live provider connection. Provider actions require configured credentials, scoped authorization, audit logging, tests and verified connectivity. No credentials or destructive provider operations are enabled by this catalog.

Status: 21 domain implementation packages consolidated under the ecosystem root. Runtime/provider connectivity is not asserted.
