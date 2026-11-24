# Global Communication Product Core Ecosystem Standard

The Global Communication Core root owns provider-neutral identity, product/service reference registration, domain classification, capability metadata, lifecycle/readiness metadata, dependency discovery and policy boundaries.

## Package ownership
- `catalog.py`: canonical root and provider/platform reference catalog.
- `product_catalog.py`: curated provider/platform and existing-directory inventory.
- `domain_catalog.py`: communication domain taxonomy.
- `contracts.py`: tenant context, secret references, readiness and result contracts.
- `policy.py`: authorization, restricted-domain and safe-summary guardrails.
- `module_service.py`: shared read-only provider metadata facade.
- `domain_runtime.py`: shared domain-scoped discovery facade.
- `manager.py`, `orchestrator.py`, `service.py`: canonical orchestration and public entry points.
- `manager.php`: thin PHP interoperability facade; Python remains canonical.

Provider-specific directories remain responsibility-driven. Do not create empty placeholder files/folders or copy shared managers into every provider package. Add a provider package only when it has distinct Core responsibilities and an individually reviewed manifest/contract.

## Layer boundaries
Communication Core owns metadata and policy. API adapters, OAuth/consent exchanges, message delivery, telephony, video transport, durable storage, queues, billing and user interfaces belong to their respective API, storage, runtime and application layers.

Catalog presence is not proof of public API availability, account entitlement, user authorization, implementation or live connectivity. Never store credentials in this package. Live status requires deployment authentication and provider smoke tests.
