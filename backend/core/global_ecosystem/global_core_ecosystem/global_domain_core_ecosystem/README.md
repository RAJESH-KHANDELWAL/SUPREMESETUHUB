# GLOBAL DOMAIN CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Path:** `backend/core/global_ecosystem/global_core_ecosystem/global_domain_core_ecosystem/`

## Mission
Canonical inventory and governance metadata for domain registration, DNS, registrar, registry, lifecycle, DNSSEC, TLS, provider discovery, tenancy and readiness.

## Core modules
- `catalog.py`: root and provider directory inventory
- `product_catalog.py`: provider references (catalog only)
- `domain_catalog.py`: responsibility taxonomy
- `contracts.py`: result contract
- `policy.py`: governance and security boundary
- `domain_runtime.py`: read-only inventory runtime
- `module_service.py`: per-domain service
- `orchestrator.py`: discovery facade
- `service.py`: public status service
- `manager.py`: canonical entry point
- `manager.php`: PHP interoperability
- `test_global_domain_core.py`: package tests

Provider directories are inventory references, not implemented or connected adapters. Core does not perform API transport, credential handling, DNS mutations, domain purchases or live provider calls.
