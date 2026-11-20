# GLOBAL AI CORE ARCHITECTURE

## Request and ownership flow

`Authenticated Application Context`
-> `GlobalAICoreManager`
-> `Provider catalog / domain manager / Core policy metadata`
-> `Global AI API provider adapter (authentication, secrets and transport)`
-> `Global AI Engine (inference, agents and tools)`
-> `Global AI Database / Storage (when required)`
-> `Application response`

Core performs provider discovery, canonical ID resolution, capability metadata checks, lifecycle/readiness reporting and dependency discovery. It does not perform token exchange, network transport, inference, tool execution or persistence.

## Google Core-aligned public API

- `get_manager()` returns the canonical `GlobalAICoreManager`.
- `status()` returns ecosystem and global registry status.
- `health()` reports provider/domain counts and explicit zero live connections/API calls.
- `list_products()` / `get_product()` discover canonical providers.
- `list_domains()` / `list_domain_inventory()` expose the 19-domain taxonomy.
- `get_domain_manager(domain_id)` returns a read-only domain-scoped manager.
- `list_offerings()` / `get_offering()` expose the unified offering inventory.
- `dependency_map()` describes Core-to-runtime/API delegation.
- `master_catalog_reference()` exposes the separate 2,468-entry master catalog pointer only.

## Canonical registry

The runtime registry at `backend/global_ecosystem/global_ai_ecosystem/providers.py` is authoritative. Each canonical registry entry maps to one `<provider_id>_core_ecosystem` package. The product index is a parity artifact, not an independent provider source of truth.

Legacy API aliases resolve to canonical IDs. Adjacent hosting, payment, advertising and content-platform entries remain compatibility-only and are excluded from canonical AI provider totals. Frameworks, model families, inference routers and hosted API vendors retain their runtime classifications.

## Master catalog boundary

`backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` is owned by `GLOBAL_ENGINE_ECOSYSTEM` and targets 2,468 unique entries. Its last inspected snapshot contained 246 unique entries and 2,222 remaining. Global AI Core publishes a reference to this catalog; it does not import the ENGINE manager, load the file or treat its entries as AI providers.

## Product package standard

Every canonical provider package contains the ten Google Core folders:
`authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/`, `tests/`.

Provider packages are thin read-only facades. Provider-specific credentials, SDKs, API calls and inference implementations belong to API and ENGINE layers respectively.

## Readiness semantics

- `CORE_CATALOG_ONLY`: provider is registered; no adapter readiness is implied.
- `ADAPTER_SCAFFOLD_NOT_LIVE_VERIFIED`: an adapter scaffold is declared.
- `READY_FOR_CONFIGURATION`: integration work is in progress and configuration/verification remains.
- `PROVIDER_MARKED_LIVE_REQUIRES_CONNECTION_VERIFICATION`: registry metadata says live, but Core has not verified a connection.
- `READY`: reserved for a deployment-level verified state supplied by the owning integration layer.

Core health must not infer a live connection from a registry label. Default health reports zero verified connections and zero provider API calls.

## Security boundaries

Tenant and actor identity originate in the authenticated application layer. Core policy checks metadata and tenant context only. API authorization, provider consent, entitlement, secret resolution and audit enforcement remain with their owning layers. Secret material is rejected from task contracts and filtered recursively from public provider summaries.
