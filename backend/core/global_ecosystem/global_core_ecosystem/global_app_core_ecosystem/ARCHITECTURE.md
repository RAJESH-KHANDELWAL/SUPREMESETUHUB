# GLOBAL APP CORE ARCHITECTURE

## Control-plane flow
`GlobalAppCoreManager` -> canonical APP provider registry -> app type/capability taxonomy -> domain inventory and dependency metadata.

## Master catalog flow
`GlobalAppCoreManager` -> read-only on-demand inventory -> `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`.

The master file remains the single source of truth owned by Global Engine. APP Core does not copy, write, expand or manufacture entries. It validates unique-entry, numbered-row, cross-reference, target and remaining counts.

## Public contract
- `get_manager()`, `status()`, `health()`
- `list_products()`, `get_product()`, `list_offerings()`, `get_offering()`
- `list_domains()`, `list_domain_inventory()`
- `list_app_types()`, `list_capability_groups()`, `validate_app_type()`
- `dependency_map()`
- `master_catalog_reference()`, `master_catalog_inventory()`, `get_master_catalog_entry()`

PHP exposes matching master-catalog reference, inventory and lookup methods.

## Boundaries
Core does not execute apps, make provider API calls, authenticate users, store secrets, persist business data or run jobs. Provider registry entries are discovery metadata only. The 2,468 target is not an app-provider count or a request to create 2,222 placeholders.
