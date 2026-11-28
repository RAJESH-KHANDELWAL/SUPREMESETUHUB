# GLOBAL APP CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Layer:** CORE  
**Ecosystem ID:** `GLOBAL-APP-CORE-ECOSYSTEM`

## Mission
Read-only control plane for application-provider identity, provider discovery, app form factors, capability groups, domain classification and dependency metadata. Public manager conventions align with Google Core.

## Canonical sources
- Providers: `backend/global_ecosystem/global_app_ecosystem/providers.py`
- App types and capability groups: `backend/global_ecosystem/global_app_ecosystem/capabilities.py`
- Scope taxonomy: `backend/global_ecosystem/global_app_ecosystem/scope.py`
- Master planning catalog: `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`, owned by `GLOBAL_ENGINE_ECOSYSTEM`

## Existing package files
- `manager.py`: canonical manager and `get_manager()`
- `manager.php`: PHP read-only interoperability facade
- `service.py`: provider resolution and app-type validation
- `__init__.py`: public exports
- `test_global_app_core.py`: manager, registry and catalog contract tests

No parallel provider registry or duplicate master JSON is created.

## Layer boundaries
| Layer | Responsibility |
|---|---|
| APP Core | Provider metadata, app types, capability taxonomy, domain discovery |
| APP | Application composition, components, lifecycle and runtime |
| API | Provider authentication, SDK clients, transport and response normalization |
| AUTH / IDENTITY | Actor identity, authentication and authorization |
| DATABASE / STORAGE | Durable records, tenant isolation, retention and backups |
| ENGINE | Jobs, scheduling, retries and execution |
| Application UI | User sessions, consent and user workflows |

Catalog presence does not prove API availability, entitlement, partnership, authentication or live integration. Core performs no app execution, provider API calls or persistence.

## Master catalog
The manager exposes `master_catalog_reference()`, `master_catalog_inventory()` and `get_master_catalog_entry(entry_id)`. Access is read-only and on demand. Cross-reference rows retain canonical IDs and are counted separately from unique entries.

The target is **2,468 unique entries**, not 2,468 app providers. Current counts are read from the master JSON and validated at runtime/CI. No dummy entries, duplicate catalog, artificial folders or placeholder files are created to reach the target.
