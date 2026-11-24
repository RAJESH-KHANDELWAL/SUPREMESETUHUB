# Global Developer Core Ecosystem

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/`

## Mission
Provider-neutral developer control plane for discovery, classification, capability metadata, lifecycle status, policy boundaries and dependency mapping across developer platforms, APIs, SDKs, cloud, AI/ML, data, security, testing, automation and India-focused services.

## Canonical Google Core-aligned architecture
- `catalog.py`: canonical module and provider/domain catalog.
- `product_catalog.py`: curated provider/platform inventory facade.
- `domain_catalog.py`: domain taxonomy.
- `contracts.py`: tenant, secret-reference, readiness and result contracts.
- `policy.py`: tenant validation, capability classification and authorization boundaries.
- `domain_runtime.py`: shared read-only domain manager.
- `module_service.py`: provider/module metadata and policy service.
- `orchestrator.py`: discovery, health and dependency orchestration.
- `service.py`: control-plane service facade.
- `manager.py`: canonical manager and singleton `get_manager()`.
- `manager.php`: PHP interoperability facade; Python remains canonical.

## Inventory
- 29 existing domain/provider directories represented in the catalog.
- 19 normalized developer domains.
- Directories `integrations`, `services`, and `tools` remain support namespaces, not falsely counted as provider implementations.
- No live provider adapters are claimed.

## Master catalog
Registered through the separate `ecosystem_module_index` in `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`. The module index is architecture metadata and does not increment the 2468 target or duplicate numbered entries.

## Layer boundaries
Core performs metadata and policy only. OAuth, provider APIs/SDK transport, deployments, payment execution, database writes, queue processing and UI belong to their dedicated layers. Secrets remain in an external secret manager.
