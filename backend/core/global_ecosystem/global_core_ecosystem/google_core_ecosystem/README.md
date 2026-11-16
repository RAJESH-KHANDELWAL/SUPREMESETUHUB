# GOOGLE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/`

## Mission

Google Core is the provider-level control plane for Google product families. It owns:
- product-family identity and canonical registration;
- capability catalog and lifecycle/readiness metadata;
- tenant-context and capability policy checks;
- product discovery, dependency mapping and health reporting;
- boundaries between Core, API, storage, runtime and application layers.

It does **not** duplicate Google SDK clients, OAuth exchanges, API transport, database persistence or secret storage.

## Product coverage

The current catalog contains 23 product families: Admin SDK, Ads, Analytics, Business Profile, Calendar, Chat, Cloud, Contacts, Docs, Drive, Firebase, Forms, Gemini, Gmail, Identity & OAuth, Maps Platform, Meet, People, Search Console, Sheets, Slides, Vertex AI and YouTube.

## Layer ownership

| Layer | Owns |
|---|---|
| Google Core | Identity, capability policy, lifecycle, orchestration, readiness |
| Google API Ecosystem | OAuth/API clients, provider requests, response normalization |
| Google Storage Ecosystem | Durable records, tenant isolation, retention and backups |
| Google Runtime/Engine | Jobs, retries, queues, scheduling and execution |
| Application/UI | User sessions, consent screens, product workflows |

## Security rules

1. Tenant and actor identity must come from the authenticated application layer.
2. Capability registration is not user authorization and is not proof of Google OAuth consent.
3. Secrets and OAuth tokens must never be committed to Git or returned in status payloads.
4. Use least-privilege OAuth scopes and explicit consent for each account.
5. Destructive, administrative, publishing, billing and write capabilities require explicit authorization and audit.
6. Do not claim a live connection until the API adapter completes a real deployment-level smoke test.
7. A product without an implemented API adapter remains catalog-only even when its Core service is available.

## Shared Core modules

- `contracts.py`: tenant context, opaque secret references, readiness and result contracts.
- `policy.py`: capability checks and safe metadata filtering.
- `module_service.py`: reusable read-only product Core service.
- `orchestrator.py`: product discovery, health and dependency map.
- `catalog.py`: canonical 23-product inventory.
- `service.py`: public ecosystem status and registry integration.

Each product package exposes its own `service.py` class using the shared contract. API implementation remains in the corresponding API ecosystem folder.

## PHP policy

The current backend is Python/FastAPI. PHP is not added to this Core tree unless a concrete PHP application/runtime integration is introduced; duplicate language files without a runtime owner create unmaintainable dead code.
