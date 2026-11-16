# GLOBAL DEVELOPER CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Layer:** CORE  
**Ecosystem ID:** `GLOBAL-DEVELOPER-CORE-ECOSYSTEM`  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem/`

## Mission

The Developer Core is the provider and domain control plane for the Bharat-to-global developer ecosystem. It owns canonical provider identity, package registration, domain taxonomy, capability metadata, policy metadata, lifecycle/readiness reporting, dependency discovery and read-only orchestration.

## Canonical inventory and source of truth

The provider package inventory mirrors the 29 provider-specific API ecosystem directories under:

`backend/api/global_ecosystem/global_api_ecosystem/global_developer_api_ecosystem/`

Those API package directories are the current provider inventory source for package parity. The Developer runtime taxonomy remains at `backend/global_ecosystem/global_developer_ecosystem/catalog.py` and supplies geographic scopes, maturity levels, developer domains and prohibited-use-case taxonomy. The API directory and runtime taxonomy have different responsibilities; neither proves that a third-party API is available or connected.

The three existing support directories `integrations/`, `services/` and `tools/` are retained as support namespaces and are not counted as provider packages.

## Google Core product package standard

Every provider package follows the ten-folder convention:

1. `authentication/` — authenticated actor/tenant context contract only; no credentials or token exchange.
2. `capabilities/` — declared capability metadata.
3. `docs/` — provider-specific documentation and implementation notes.
4. `events/` — event contract metadata; no event delivery.
5. `lifecycle/` — registration and readiness metadata.
6. `models/` — provider/product metadata, not model execution.
7. `schemas/` — metadata schemas and validation contracts.
8. `security/` — security boundaries and policy metadata.
9. `services/` — read-only Core facade boundary.
10. `tests/` — package and contract tests.

Each package also contains `README.md`, `ecosystem_manifest.json`, `ecosystem_config.py`, `contracts.py`, `__init__.py` and `authentication/contract.php`.

## Layer ownership

| Layer | Responsibility |
|---|---|
| CORE | Provider identity, catalog, policy metadata, lifecycle, readiness and orchestration |
| API | External API contracts, OAuth, credentials, SDK clients, transport and webhooks |
| ENGINE | Code execution, builds, CI jobs, deployment jobs, queues and orchestration execution |
| DATABASE | Persistent developer records, schemas, queries and migrations |
| STORAGE | Repositories, artifacts, packages, logs and backups |
| SECURITY / IDENTITY | Authentication, authorization, secret management, audit and security enforcement |
| APPLICATION | Developer portals, dashboards, sessions and user workflows |

Core does not import or execute sibling API/ENGINE/DATABASE/STORAGE layers. It does not duplicate SDKs, credentials, transport, code execution, builds, deployments, persistence or UI.

## Safety and governance

- Adult-only technology categories remain disabled by default and require age assurance, consent, privacy, moderation and jurisdiction-specific legal review.
- Prohibited use cases include sexual content involving minors, non-consensual intimate imagery, coercion/exploitation/trafficking, doxxing/private-data exposure and malware/unauthorized access.
- No secrets, API keys, access tokens, private keys or credentials belong in Core manifests or status payloads.
- Registration is not provider verification, account entitlement, API availability or live connectivity.
- All 29 provider records are catalog-only; no live connections or external API calls are claimed.
