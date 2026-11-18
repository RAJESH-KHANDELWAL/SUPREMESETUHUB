# GLOBAL APP CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Layer:** CORE  
**Ecosystem ID:** `GLOBAL-APP-CORE-ECOSYSTEM`  
**Runtime domain:** `GLOBAL_APP_ECOSYSTEM`  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_app_core_ecosystem/`

## Mission

Global App Core is the provider-neutral control plane for application-platform identity, catalog discovery, app-type classification, domain taxonomy, capability metadata, lifecycle/readiness reporting and safe orchestration boundaries across Bharat and global application ecosystems.

The runtime application-provider registry is the single source of truth:

`backend/global_ecosystem/global_app_ecosystem/providers.py`

Core consumes that registry. It must not create a competing provider inventory or silently rewrite provider IDs.

## Scope and evidence

The runtime catalog currently contains provider discovery metadata. Each entry is marked `catalog_only` and `live_connection_verified=False` in the inspected registry. Registration means discoverable metadata only; it does not prove an API, partnership, entitlement, account, authorization, app availability or live integration.

The taxonomy is maintained by:
- `backend/global_ecosystem/global_app_ecosystem/scope.py` — application domains and maturity levels.
- `backend/global_ecosystem/global_app_ecosystem/capabilities.py` — app types, delivery platforms and capability groups.
- `backend/global_ecosystem/global_app_ecosystem/providers.py` — canonical provider catalog and registry validation.

## Canonical provider Core package standard

Every provider-specific package under this root follows the same ten-folder convention used by the Google Core reference:

1. `authentication/` — authentication-context contracts only; no credentials or token exchange.
2. `capabilities/` — declared app capabilities and policy metadata.
3. `docs/` — provider-specific architecture, scope and implementation notes.
4. `events/` — lifecycle and domain event contracts.
5. `lifecycle/` — registration, readiness and lifecycle metadata.
6. `models/` — app/product/service metadata, not app execution.
7. `schemas/` — provider metadata schemas and validation contracts.
8. `security/` — safe-handling rules and security metadata.
9. `services/` — provider Core facade and read-only service contracts.
10. `tests/` — provider package and contract tests.

`google_app_core_ecosystem/` is the reference package for this convention. Other provider folders must adopt the same layout without changing canonical provider IDs.

## Layer ownership

| Layer | Owns |
|---|---|
| Global App Core | Provider identity, catalog mapping, app-type/domain taxonomy, capability metadata, Core policy, lifecycle/readiness and orchestration metadata |
| Global App API | OAuth and provider authentication, secret resolution, SDK/HTTP clients, transport, retries and response normalization |
| Global App Engine | App adapters, workflow execution, automation, tool invocation and runtime operations |
| Global App Database | Structured records, schemas, queries, migrations and transactions |
| Global App Storage | Files, media, backups, retention and tenant-isolated durable artifacts |
| Application/UI | User sessions, consent, user workflows and presentation |

Core must not duplicate API transport, token exchange, secret storage, app execution, adapter invocation, persistence or user-interface workflows.

## Public service contract

`GlobalAppCoreService` is read-only and metadata-oriented:
- `resolve_provider(provider_id)` resolves one canonical provider or raises `KeyError`.
- `validate_app_type(app_type_id)` validates an app form factor or raises `KeyError`.
- `provider_snapshot(provider_id)` returns an allow-listed, secret-filtered metadata view.
- `catalog_snapshot()` reports provider counts, taxonomy, maturity levels and verification counts.
- `health_snapshot()` reports catalog integrity and explicitly states that no execution or persistence occurred.

No method in this Core package performs a provider API call or claims a live connection.

## Security and lifecycle rules

- Tenant and actor identity must originate from the authenticated application layer.
- Core metadata checks are not application authorization or provider authorization.
- Never store credentials, access/refresh tokens, API keys, private keys or secret values in Core.
- Store opaque secret references only when a contract requires a reference; resolve secret material at the API/security boundary.
- Payment, publishing, messaging, account changes, destructive actions and access to sensitive data require explicit authorization, consent where applicable and audit in the owning runtime layer.
- Adult or age-restricted application categories require lawful age assurance, verified consent/rights, privacy, safety and no-minors safeguards; catalog membership is not approval to access or distribute content.
- A provider status of `configured` or `live_verified` must be backed by evidence from the owning integration layer. Core must not infer it from catalog presence.
- Current catalog entries are not live-verified unless the registry explicitly says so and supporting runtime evidence is available.

## Verification requirements

CI should verify:
1. Runtime provider IDs are unique and every Core provider package maps to one canonical ID.
2. Every provider Core package contains all ten required folders.
3. Provider inventory and Core package inventory reconcile.
4. App types, capability groups, domain IDs and maturity levels are unique and structurally valid.
5. Catalog-only providers are never reported as configured or live.
6. Python imports, contract tests and repository-level compatibility tests pass.
7. No secret material appears in tracked files or status payloads.

A successful catalog check does not establish a live provider connection.
