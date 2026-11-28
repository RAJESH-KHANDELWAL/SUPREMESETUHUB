# APPLE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem/`

## Mission
Apple Core is a read-only provider control plane for Apple provider identity, product-family registration, domain classification, capability metadata, policy boundaries, dependency metadata and readiness.

## Canonical entry points
- `manager.py`: public manager; status, health, product/domain/offering discovery, dependency map and domain-manager access.
- `manager.php`: PHP interoperability contract facade; sanitizes sensitive fields and validates response shape.
- `catalog.py`: provider identity and 8 registered product families.
- `product_catalog.py`: offering inventory and routing metadata.
- `domain_catalog.py`: six responsibility domains and product routing.
- `contracts.py`: tenant context, secret references, readiness and result contracts.
- `policy.py`: metadata-only capability guardrails.
- `module_service.py`: reusable product-family Core service.
- `orchestrator.py`: discovery, health and dependency metadata.
- `service.py`: public ecosystem status and registry integration.
- `domain_runtime.py`: shared read-only manager for responsibility domains.
- `tests/test_apple_core_manager.py`: structural and behavior validation for catalog, domain and product-family manager contracts.
- `apple_*_core_ecosystem/` product-family packages: eight packages with canonical `manager.py` entry points and package documentation.
- Six responsibility-domain packages: each contains `manager.py`, `__init__.py` and `README.md`, backed by the shared runtime.
- Naming-standard shared packages: `apple_core_registry_core_ecosystem/`, `apple_shared_compatibility_core_ecosystem/`, `apple_shared_configuration_core_ecosystem/`, `apple_shared_contracts_core_ecosystem/`, `apple_shared_documentation_core_ecosystem/`, `apple_shared_events_core_ecosystem/`, `apple_shared_exceptions_core_ecosystem/`, `apple_shared_orchestration_core_ecosystem/`, `apple_shared_security_core_ecosystem/`, `apple_shared_testing_core_ecosystem/`, `apple_shared_utilities_core_ecosystem/`, `apple_shared_validation_core_ecosystem/`. These are shared responsibility/support packages; inspect contents before adding implementation or duplicating utilities.

## Domains
1. App Store and Distribution
2. App Store Commerce
3. Device Management
4. Cloud Data and Sync
5. Payments and In-App Commerce
6. Identity and Notifications

## Layer boundaries
| Layer | Responsibility |
|---|---|
| Apple Core | provider/product identity, capability metadata, domains, lifecycle policy, readiness |
| Apple API | authentication/signing, adapters, transport and response normalization |
| Storage/Database | durable data, schemas, migrations and transactions |
| Runtime/Engine | queues, jobs, retries, scheduling and execution |
| Application/UI | sessions, consent and product workflows |

Core does not store credentials, private keys, payment secrets, tokens or signing material. Catalog registration does not prove entitlement, authorization, API availability or live connectivity. Apple API calls and live connections are not performed by this Core package.
