# Global Communication Core Ecosystem

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_communication_core_ecosystem/`

## Mission
Provider-neutral control plane for communication provider identity, product/service discovery, domain classification, capability metadata, lifecycle/readiness, dependency mapping and governance. It follows the responsibility-driven Google Core architecture without copying Google-specific product logic.

## Canonical structure
- `manager.py`: canonical Python manager and singleton `get_manager()`.
- `manager.php`: thin PHP interoperability facade; Python remains canonical.
- `catalog.py`: canonical root catalog and provider/domain references.
- `product_catalog.py`: curated provider/platform inventory and existing-directory inventory.
- `domain_catalog.py`: 28-domain taxonomy.
- `contracts.py`: tenant context, opaque secret references, readiness and result contracts.
- `policy.py`: authorization, privacy and restricted-domain guardrails.
- `module_service.py`: shared read-only provider metadata service.
- `domain_runtime.py`: shared read-only domain discovery runtime.
- `orchestrator.py` and `service.py`: health, discovery, dependency and status facades.
- `PRODUCT_ECOSYSTEM_STANDARD.md`: package/layer ownership standard.
- `test_global_communication_core.py` and `test_global_communication_core_domains.py`: catalog, contract and policy tests.

Provider directories remain responsibility-driven. Do not create empty placeholder folders or duplicate shared managers in every provider directory. Add provider-specific code only for a documented, independently reviewed responsibility.

## Inventory
- 95 provider/platform reference records (not 95 verified independent companies or live integrations).
- 28 domain definitions.
- 19 pre-existing directories, tracked separately from the provider reference inventory.
- 40 service-family labels (classification metadata).

## Master catalog integration
`backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` has a separate `ecosystem_module_index` entry pointing to this module. This index is architecture metadata, not part of the numbered 2468 target. The original expansion counters and 246 unique catalogue entries remain unchanged. Communication Core reads the master catalog only; it does not mutate or duplicate its numbered entries.

## Layer boundaries
Core owns metadata and policy. OAuth, provider SDK/API transport, message/email delivery, telephony, video transport, durable storage, database operations, queues, billing and UI belong to their dedicated layers. Credentials remain in an external secret manager.

Catalog membership does not prove API availability, account entitlement, caller authorization, implementation or live connectivity. Live status requires deployment authentication and provider smoke tests. Provider names, aliases, products and geographic availability require source-by-source lifecycle verification.
