# GLOBAL CLOUD CORE ARCHITECTURE

## Metadata flow
`GlobalCloudCoreManager` -> canonical cloud provider catalog -> capability taxonomy -> cloud domain classification -> workload and regional-scope discovery.

## Master catalog flow
`GlobalCloudCoreManager` -> read-only on-demand inventory -> `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`.

The master file remains owned by Global Engine. Cloud Core never copies, writes, expands or manufactures its entries. Counts for unique entries, source rows, cross-references, target and remaining entries are reconciled at read time.

## Public manager contract
- `get_manager()`, `status()`, `health()`
- `list_products()`, `get_product()`
- `list_domains()`, `list_domain_inventory()`, `get_domain_manager()`
- `list_offerings()`, `get_offering()`
- `list_scopes()`, `list_capabilities()`, `dependency_map()`
- `master_catalog_reference()`, `master_catalog_inventory()`, `get_master_catalog_entry()`

PHP exposes the master-catalog reference, inventory and exact-entry lookup.

## Boundaries
Core performs classification and discovery only. Cloud API owns credentials and transport; Cloud Engine owns provisioning and execution; Database and Storage own persistence. No live cloud connection or provisioning is inferred from catalog registration.
