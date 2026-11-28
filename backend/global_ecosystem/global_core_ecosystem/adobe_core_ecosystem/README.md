# ADOBE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/adobe_core_ecosystem/`

## Purpose
Adobe Core is the provider-level control plane and catalog for Adobe product-family identities, capability metadata, domain classification, lifecycle, policy boundaries, dependency references and readiness.

## Canonical shared entry points
- `manager.py`: stable Python manager for status, product/domain discovery and dependency metadata.
- `manager.php`: PHP interoperability facade using the shared result contract.
- `catalog.py`: canonical Adobe product-family catalog.
- `domain_catalog.py`: domain inventory and coverage summary derived from the catalog, plus provider governance.
- `domain_runtime.py`: reusable read-only manager for each catalog domain.
- `contracts.py`: tenant context, secret references, readiness and result contracts.
- `policy.py`: metadata policy guardrails (not provider authorization).
- `module_service.py`: shared product Core facade.
- `orchestrator.py`: product discovery, domain inventory, health and dependency metadata.
- `service.py`: public ecosystem status.
- `test_adobe_core_domains.py`: structural and behavior tests.

## Domain coverage
Every catalog product family is discoverable through the shared domain runtime. The domain inventory includes the provider-governance domain plus each catalog product family; product packages remain responsibility-specific and are not duplicated into empty template directories.

## Layer boundaries
Core owns identity, metadata, policy, lifecycle and readiness. API owns OAuth, SDK/HTTP transport and provider endpoints. Storage owns files/objects; Database owns structured persistence; Runtime/Engine owns jobs and execution; Application/UI owns user workflows.

Catalog registration, API-family mapping or scaffold presence does not prove entitlement, authorization, live connectivity or production readiness. No live Adobe connection is claimed.
