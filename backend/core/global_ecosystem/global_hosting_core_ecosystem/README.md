# GLOBAL HOSTING CORE ECOSYSTEM

Parent: GLOBAL CORE ECOSYSTEM. Canonical path: `backend/core/global_ecosystem/global_core_ecosystem/global_hosting_core_ecosystem/`.

## Mission
Read-only hosting control plane for provider identity, domain taxonomy, capability metadata, discovery, policy, readiness and dependency mapping. Architecture follows the separation used by `google_core_ecosystem/` while retaining hosting-specific records.

## Components
- `catalog.py`: canonical provider inventory and ecosystem root.
- `provider_catalog.py`: filtered provider inventory and lookup facade.
- `hosting_categories.py` + `domain_catalog.py`: taxonomy, domain inventory and coverage summary.
- `contracts.py`: tenant context, opaque secret reference, readiness and result contracts.
- `module_service.py`: reusable provider Core service and capability metadata.
- `orchestrator.py`: discovery, health and dependency metadata.
- `policy.py`: tenant checks, capability classification and metadata redaction.
- `service.py`: public service and read-only 2468 master catalog reference.
- `manager.py`: canonical Python entry point; `manager.php` is an interoperability facade.
- `models.py`, `registry.py`, `tests/`: typed contract, lookup and verification.
- Domain packages expose category managers; provider packages expose provider identity metadata.

## Domains
Shared/WordPress; managed WordPress; cloud/VPS/dedicated compute; managed hosting; application platforms; CDN/edge; object storage; media; managed databases; email; domains/DNS; colocation/data centres; control panels; static/developer hosting; specialist platforms; unclassified.

## 2468 master catalog
The canonical file is `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`. Hosting Core references it on demand and read-only. Its `ecosystem_module_index` entry is architecture metadata and does not change the numbered 2468 target. Provider/domain inventory is not copied into numbered sections. Existing expansion counters and entries remain unchanged.

## Boundaries
CORE owns identity, taxonomy, metadata, policy and readiness. OAuth/API transport belongs to API; persistence/migrations to database/storage; provisioning, DNS mutation, deployment, billing and execution to infrastructure/runtime; workflows to application. Secrets remain in an external secret manager. Catalog registration is not proof of availability, entitlement, authorization or live connectivity. No API calls, provisioning, DNS changes, deployments, billing or persistence writes occur in Core. Inventory is extensible and not claimed exhaustive.
