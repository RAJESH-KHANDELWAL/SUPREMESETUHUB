# Adobe Product Core Ecosystem Standard

Adobe Core follows the provider Core pattern used by Google Core while retaining Adobe-specific product-family inventory.

- Root `manager.py` is the canonical Python entry point; `manager.php` is a thin PHP contract facade.
- `catalog.py` is the source of truth for product-family registration.
- `domain_catalog.py` derives provider governance and product-family domain inventory from the canonical catalog.
- `domain_runtime.py` provides shared read-only domain discovery; domain-specific logic belongs in product Core packages.
- `contracts.py`, `policy.py`, `module_service.py`, `orchestrator.py` and `service.py` are shared Core responsibilities.
- Product packages contain only files required for that product's responsibilities; do not create empty fixed templates or duplicate shared managers.

Core owns provider/product identity, capability metadata, lifecycle and policy metadata, readiness and stable contracts. API owns OAuth, SDK clients, HTTP transport, endpoints and webhooks. Storage owns file/object persistence. Database owns durable structured records. Runtime/Engine owns jobs, queues, schedulers and execution. Application/UI owns user workflows and presentation.

Catalog entries and API-family mappings do not prove entitlement, authorization, live connection or production readiness. Production integrations require verified capabilities, official API references, entitlement/scope checks, secure configuration, contract tests, error handling, observability and successful integration tests.
