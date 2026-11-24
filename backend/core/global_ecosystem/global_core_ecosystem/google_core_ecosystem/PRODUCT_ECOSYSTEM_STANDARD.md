# Google Product Core Ecosystem Standard

The Google Core root owns provider-level identity, product registration, domain classification, capability metadata, policy boundaries, lifecycle and readiness.

Each product Core package is responsibility-driven: include only the manifest, contracts, service or other files that the product actually needs. Empty placeholder folders and repeated copies of shared managers are not required.

Shared Python orchestration is centralized in `manager.py`, `orchestrator.py` and the existing catalog modules. PHP consumers use the thin root `manager.php` facade and `google_php_core_ecosystem/GoogleCoreContract.php` contract. Neither PHP nor Core performs OAuth token exchange or Google API transport.

Google API clients, OAuth flows, durable storage, database operations, background execution and user interfaces remain in their respective layers. Catalog entries do not prove API eligibility, entitlement, authorization or live connectivity. Live status requires deployment-level authentication and provider smoke tests.
