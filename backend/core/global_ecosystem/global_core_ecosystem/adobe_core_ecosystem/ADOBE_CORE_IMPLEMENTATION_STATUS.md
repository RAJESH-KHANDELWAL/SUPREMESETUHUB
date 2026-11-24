# Adobe Core Implementation Status

Last catalog review: 2026-11-16.

- Official catalog pages reviewed: Adobe global product catalog and Adobe for Business product catalog.
- Global catalog source-page result count: 100.
- Adobe for Business source-page result count: 43.
- Named deduplicated entries: 119 (see `adobe_product_inventory.json`).
- Canonical Core domains: 32.
- Canonical Core package scaffolds: 32/32.
- Standard directories per package: 10/10.
- Machine-readable manifests per package: present.
- Shared provider catalog/contracts/policy/services/orchestrator: existing foundation retained.
- Live Adobe connections verified: 0.
- Credentials configured: 0.
- Adobe API family adapters: 8/8 scaffolded separately in the API layer.
- Core-to-API family references: explicit mappings added only where a family-level relationship is justified; unmapped domains are not assigned invented endpoints.
- Product-specific API entitlements/scopes: not verified.
- Product-specific integration tests: not executed in this change.

## Remaining production work

1. Verify lifecycle and regional availability for every named catalog item.
2. Map official developer APIs and product entitlements to the correct API-layer modules.
3. Implement product-specific Core capability contracts and lifecycle transitions.
4. Configure secrets only through approved secret management; never commit credentials.
5. Implement and run unit, contract and integration tests in CI.
6. Reconcile the catalog periodically because Adobe updates products and catalog listings.

A scaffold or catalog entry is not a completed live integration.
