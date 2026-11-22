# SUPREMESETUHUB — Five Backend Systems Architecture

**Status:** Architecture baseline and non-destructive audit  
**Branch:** `docs/five-layer-architecture-audit`  
**Audited against:** `main`  
**Date:** 2026-11-08

This document records the observed backend layout and establishes ownership boundaries for API, CORE, ENGINE, DATABASE, and STORAGE. It is not a claim that every provider is connected or every subsystem is production-ready.

## 1. Canonical layer roots

| Layer | Canonical root | Primary ownership |
|---|---|---|
| API | `backend/api/` | HTTP routes, request/response schemas, external API adapters, authentication at API boundaries |
| CORE | `backend/core/` | Domain contracts, independent business rules, canonical domain models and policies |
| ENGINE | `backend/engine/` | Execution, orchestration, scheduling and runtime coordination |
| DATABASE | `backend/database/` | Durable relational data access, schemas, migrations, repositories and transactions |
| STORAGE | `backend/storage/` | File/object persistence, storage adapters, metadata and artifact lifecycle |

Global ecosystem catalogs are layer-owned and must remain under their respective roots:

- `backend/api/global_ecosystem/global_api_ecosystem/`
- `backend/core/global_ecosystem/global_core_ecosystem/`
- `backend/engine/global_ecosystem/global_engine_ecosystem/`
- `backend/database/global_ecosystem/global_database_ecosystem/`
- `backend/storage/global_ecosystem/global_storage_ecosystem/`

Each layer owns its implementation. A similarly named provider/category directory in another layer is a separate layer-specific catalog or contract, not permission to copy implementation code across layers.

## 2. Dependency and ownership rules

1. API owns transport concerns. It may call application/domain interfaces, but CORE must never import API routers, HTTP request objects or API adapters.
2. CORE owns domain rules and contracts. It must not import API, ENGINE runtime implementations, DATABASE drivers or STORAGE providers.
3. ENGINE owns execution and orchestration. It may coordinate through stable contracts, but must not absorb or duplicate API, CORE, DATABASE or STORAGE implementations.
4. DATABASE owns durable structured data and transaction semantics. Other layers use its public repositories/services; they do not create competing canonical databases.
5. STORAGE owns file/object bytes and storage lifecycle. DATABASE may store metadata and references, but must not become a second file-storage implementation.
6. Provider catalog presence is not proof of configured credentials, successful connectivity, live capability or production readiness. Status must distinguish catalogued, implemented, configured, connected and verified.
7. Keep secrets out of source control. Do not claim a live integration without an authorized end-to-end check.

## 3. Observed repository facts on main

### API and CORE

- Both have independent Global Ecosystem roots and provider/category directories.
- CORE has its own catalog, manager, models and registry.
- API has provider-specific directories and ecosystem entrypoints.
- The existence of matching folder names does not establish catalog parity or dependency isolation. Those require automated checks.

### ENGINE

- The canonical execution root is `backend/engine/`.
- Its Global Engine catalog is under `backend/engine/global_ecosystem/global_engine_ecosystem/`.
- `backend/engine/database/manager.py` and `backend/engine/storage/manager.py` are orchestration/runtime modules; they must not become alternate owners of database or storage persistence.
- A second path, `backend/engines/global_ecosystem/google_engine/`, also exists. Its import references and intended compatibility role must be mapped before moving or deleting it.

### DATABASE

- The active lowercase service root is `backend/database/`, with connection, manager, schema, model, service and transaction modules.
- Its Global Database catalog is under `backend/database/global_ecosystem/global_database_ecosystem/`.
- `backend/engine/database/manager.py` currently imports `backend.database.service.DatabaseService`. This is an ENGINE-to-DATABASE dependency and should remain an orchestration call, not a duplicate persistence implementation.
- The inspected central DatabaseEngine currently supports SQLite and explicitly rejects other URL schemes until their drivers and lifecycle semantics are implemented. Do not advertise PostgreSQL/MySQL support solely because catalog entries exist.

### STORAGE

- The active lowercase service root is `backend/storage/`, with filesystem, provider registry, S3 and service modules.
- Its Global Storage catalog is under `backend/storage/global_ecosystem/global_storage_ecosystem/`.
- `backend/engine/storage/manager.py` imports the database service and local file-storage implementation. Its role should be orchestration; storage adapters and byte persistence remain STORAGE-owned.
- The inspected provider catalog marks local and AWS S3 as implemented, while Google Drive, OneDrive, MEGA and Hostinger are not implemented in that adapter catalog. Configuration and live connectivity must be checked separately.

### Uppercase legacy/domain paths — do not delete blindly

- `backend/DATABASE/GLOBAL_ECOSYSTEM/GLOBAL_DATABASE_ECOSYSTEM/` contains server-inventory repository/model/service files.
- `backend/STORAGE/GLOBAL_ECOSYSTEM/GLOBAL_STORAGE_ECOSYSTEM/` contains server-artifact repository/model/service files.
- These paths overlap conceptually with the lowercase DATABASE/STORAGE layer names, but their server inventory/artifact responsibilities are not proven to be exact duplicates of the lowercase provider ecosystems.
- `backend/DATABASE/` and `backend/STORAGE/` must not be removed until imports, route mounts, tests, data ownership and migration/compatibility requirements are traced.
- The broader uppercase `backend/SERVER/` migration is handled separately by PR #221. Review its resulting imports and tests before merging or applying overlapping changes.

## 4. Required validation before structural migration

- [ ] Inventory every Python import referencing `backend/engines`, `backend/DATABASE`, `backend/STORAGE` and their subpackages.
- [ ] Identify public routes and callers for each legacy service.
- [ ] Compare provider/category IDs and parent-child relationships across all five catalogs.
- [ ] Check duplicate IDs, missing parents, orphan nodes and unstable names.
- [ ] Verify package exports and compatibility facades.
- [ ] Add import-boundary tests: CORE cannot depend on API/ENGINE/DATABASE/STORAGE; ENGINE cannot own or duplicate their implementations.
- [ ] Add repository/contract tests for DATABASE and STORAGE.
- [ ] Run focused tests, then the full backend test suite and CI.
- [ ] Preserve existing data and APIs; use compatibility facades and staged migrations where required.

## 5. Safe implementation order

1. Freeze and document the five canonical roots and ownership rules.
2. Map imports and consumers of the uppercase and plural legacy paths.
3. Establish contract tests and catalog consistency tests before moving code.
4. Move one bounded responsibility at a time, retaining compatibility imports.
5. Verify data migrations and rollback paths before removing legacy implementations.
6. Report implementation, configuration and live-connectivity status separately.

## 6. Non-goals of this audit commit

This document does not move or delete code, change runtime behavior, migrate databases, connect providers, or assert that CI/tests passed. Those changes require the dependency inventory and focused validation above.
