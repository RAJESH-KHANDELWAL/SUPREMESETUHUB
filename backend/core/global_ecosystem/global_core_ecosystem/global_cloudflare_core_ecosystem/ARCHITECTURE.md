# Cloudflare Core Architecture

- `product_catalog.py`: canonical product inventory and explicit classification of pre-existing directories.
- `domain_catalog.py`: domain taxonomy derived from product ownership; counts reconcile from the same inventory.
- `policy.py`: tenant-context and sensitive-capability guardrails.
- `orchestrator.py`: read-only product/domain discovery and dependency mapping.
- `service.py`: control-plane service interface.
- `manager.py`: stable Python entry point and read-only bridge to `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`.
- `manager.php`: PHP interoperability facade; no duplicated product registry.
- `test_cloudflare_core.py`: reconciliation, routing, policy and master-catalog tests.

The master catalog remains the only source for the 2468 expansion target. The Cloudflare product inventory is not a count toward that target. Existing external/unknown folders are not treated as Cloudflare products.
