# ADOBE CORE ECOSYSTEM

Provider-level Core inventory and policy foundation for Adobe product families.

## Current scope

- 32 Adobe product/service domains represented in `catalog.py`.
- Shared contracts, policy metadata, read-only module service and orchestrator.
- One product-family package scaffold: `adobe_creative_cloud_core_ecosystem`.
- Remaining product families are catalog entries pending their own package scaffolds.
- No live Adobe API connections or credentials are configured.

## Layer boundaries

Core owns product identity, capability metadata, lifecycle, policy and readiness. OAuth, SDK clients and HTTP transport belong to the Adobe API layer; persistence belongs to Storage/Database; jobs belong to Runtime/Engine; user workflows belong to Application/UI.

See `PRODUCT_ECOSYSTEM_STANDARD.md` and `ADOBE_CORE_IMPLEMENTATION_STATUS.md` for the implementation standard and verified scope.
