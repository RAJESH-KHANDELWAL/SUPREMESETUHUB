# ADOBE CORE ECOSYSTEM

Provider-level Core inventory, product-family package scaffolds, contracts and policy metadata for Adobe.

## Coverage snapshot (2026-11-16)

- 32 canonical Core domains represented in the shared catalog.
- 32/32 canonical Core domain package scaffolds present.
- Every package contains the ten-directory standard and machine-readable manifest.
- Named product inventory is maintained in `adobe_product_inventory.json`, sourced from Adobe's global and business product catalogs.
- Catalog source pages report 100 global catalog results and 43 Adobe for Business results; these counts include overlapping bundles, products, editions and services and must not be summed as unique products.

## Important status distinction

This update completes the **Core inventory and package scaffold baseline**, not production integrations for every Adobe product. Product-specific capability implementations, official API mapping, account entitlements, credentials, provider connections and integration tests remain unverified. No live Adobe connection is claimed.

## Layer boundaries

OAuth/SDK/HTTP transport belongs to Adobe API; persistence belongs to Storage/Database; jobs belong to Runtime/Engine; user workflows belong to Application/UI.

See `ADOBE_CATALOG_AUDIT.md`, `ADOBE_CORE_IMPLEMENTATION_STATUS.md` and `PRODUCT_ECOSYSTEM_STANDARD.md`.
