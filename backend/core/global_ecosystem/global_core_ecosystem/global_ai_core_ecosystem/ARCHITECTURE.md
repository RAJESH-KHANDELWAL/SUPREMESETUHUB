# GLOBAL AI CORE ARCHITECTURE

## Request and ownership flow

`Authenticated Application Context`
-> `GlobalAICoreManager`
-> `Provider catalog / domain manager / Core policy metadata`
-> `Global AI API provider adapter (authentication, secrets and transport)`
-> `Global AI Engine (inference, agents and tools)`
-> `Global AI Database / Storage (when required)`
-> `Application response`

A separate read-only catalog path is available when requested:

`GlobalAICoreManager`
-> `master_catalog_inventory()`
-> `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` (single source of truth)

Core performs provider discovery, canonical ID resolution, capability metadata checks, lifecycle/readiness reporting and dependency discovery. It does not perform token exchange, network transport, inference, tool execution or persistence. The master-catalog bridge reads the existing JSON file on demand and never mutates or duplicates it.

## Google Core-aligned public API

- `get_manager()` returns the canonical `GlobalAICoreManager`.
- `status()` returns ecosystem and global registry status.
- `health()` reports provider/domain counts and explicit zero live connections/API calls.
- `list_products()` / `get_product()` discover canonical providers.
- `list_domains()` / `list_domain_inventory()` expose the 19-domain taxonomy.
- `get_domain_manager(domain_id)` returns a read-only domain-scoped manager.
- `list_offerings()` / `get_offering()` expose the unified offering inventory.
- `dependency_map()` describes Core-to-runtime/API delegation.
- `master_catalog_reference()` exposes the master catalog identity, owner and read-only access mode without loading the file.
- `master_catalog_inventory(include_cross_references=True)` reads and validates every currently defined source row, section and expansion count on demand.
- `get_master_catalog_entry(entry_id)` returns one exact source row, including cross-reference rows.

The PHP facade provides matching `masterCatalogReference()`, `masterCatalogInventory()` and `getMasterCatalogEntry()` methods.

## Canonical registry

The runtime registry at `backend/global_ecosystem/global_ai_ecosystem/providers.py` is authoritative. Each canonical registry entry maps to one `<provider_id>_core_ecosystem` package. The product index is a parity artifact, not an independent provider source of truth.

Legacy API aliases resolve to canonical IDs. Adjacent hosting, payment, advertising and content-platform entries remain compatibility-only and are excluded from canonical AI provider totals. Frameworks, model families, inference routers and hosted API vendors retain their runtime classifications.

## Master catalog coverage and ownership

`backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` remains the only master catalog and is owned by `GLOBAL_ENGINE_ECOSYSTEM`. Global AI Core does not create a second copy or claim ownership.

The verified snapshot currently contains 248 numbered source rows: 246 unique entries and 2 cross-reference rows. The catalog declares a target of 2,468 unique entries and 2,222 remaining. The bridge returns all 248 current rows by default and preserves the canonical IDs on cross-reference rows. Its validation checks the source row count, unique count, cross-reference count, target and remaining count before returning data.

The target is a planning target, not a request to manufacture 2,222 entries. No folder, file, module, provider or placeholder record may be created merely to increase the count. Only meaningful, individually defined, non-duplicate additions may be made by the master catalog's owning layer. These broad planning topics are exposed as master-catalog context; they are not misrepresented as AI providers.

## Product package standard

Every canonical provider package contains the ten Google Core folders:
`authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/`, `tests/`.

Provider packages are thin read-only facades. Provider-specific credentials, SDKs, API calls and inference implementations belong to API and ENGINE layers respectively. Do not add folders or file mirrors without a concrete runtime, integration, contract or test requirement.

## Readiness semantics

- `CORE_CATALOG_ONLY`: provider is registered; no adapter readiness is implied.
- `ADAPTER_SCAFFOLD_NOT_LIVE_VERIFIED`: an adapter scaffold is declared.
- `READY_FOR_CONFIGURATION`: integration work is in progress and configuration/verification remains.
- `PROVIDER_MARKED_LIVE_REQUIRES_CONNECTION_VERIFICATION`: registry metadata says live, but Core has not verified a connection.
- `READY`: reserved for a deployment-level verified state supplied by the owning integration layer.

Core health must not infer a live connection from a registry label. Default health reports zero verified connections and zero provider API calls.

## Security boundaries

Tenant and actor identity originate in the authenticated application layer. Core policy checks metadata and tenant context only. API authorization, provider consent, entitlement, secret resolution and audit enforcement remain with their owning layers. Secret material is rejected from task contracts and filtered recursively from public provider summaries.
