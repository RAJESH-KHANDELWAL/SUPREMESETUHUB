# NSF WINFRA CORE ECOSYSTEM

**Parent:** Global Core Ecosystem  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/nsfwinfra_core_ecosystem/`

## Purpose

Metadata-only control plane for infrastructure domains, aligned with the Google Core architecture: stable manager, catalog, contracts, policy, on-demand master-catalog reference, orchestration, service facade, readiness metadata, standards, documentation and tests. It does not implement infrastructure execution or claim live connectivity.

## Registered packages (10)

1. `nsfwinfra_account_limits_core_ecosystem` — Account Limits
2. `nsfwinfra_anime_generation_core_ecosystem` — Anime Generation
3. `nsfwinfra_async_jobs_core_ecosystem` — Async Jobs
4. `nsfwinfra_image_editing_core_ecosystem` — Image Editing
5. `nsfwinfra_image_generation_core_ecosystem` — Image Generation
6. `nsfwinfra_image_to_video_core_ecosystem` — Image to Video
7. `nsfwinfra_image_video_effects_core_ecosystem` — Image & Video Effects
8. `nsfwinfra_signed_uploads_core_ecosystem` — Signed Uploads
9. `nsfwinfra_text_to_video_core_ecosystem` — Text to Video
10. `nsfwinfra_webhooks_core_ecosystem` — Webhooks

## Root modules

- `manager.py`: canonical manager and `get_manager()` entry point.
- `manager.py`: single canonical source for provider identity, product-family catalog, inventory helpers and `get_manager()`.
- `contracts.py`: shared result envelope.
- `policy.py`: security, privacy, authorization and execution boundaries.
- `master_catalog.py`: on-demand, read-only reference to the canonical 2468-target catalog.
- `orchestrator.py`: inventory, health and dependency mapping.
- `service.py`: root status facade.
- `backend/test/test_nsfwinfra_core_ecosystem.py`: canonical root and product-manager regression suite.

Each package has a manager, package README and package initializer. Add files only when a concrete package responsibility requires them.

## Master catalog

The canonical file is `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`. This Core references it on-demand and read-only; it does not duplicate numbered entries or modify catalog numbering/contents. Summary loading reports the source's actual expansion counters when the file is accessible and never invents completion numbers.

## Layer boundaries

Core owns identity, capability metadata, policy boundaries, discovery and readiness. API transport, authentication, secrets, persistence, database operations, queue execution, processing engines, upload transport, webhook delivery and user-facing workflows belong to their designated layers. Trusted tenant/actor context is supplied by the authenticated application/security layer. Catalog registration does not grant authorization or entitlement.

## Status semantics

Registered means metadata exists. Ready means required deployment checks have passed. Connected/live must only be reported after actual external checks; this metadata manager always reports `live_connection_verified: false` and `execution_performed: false`.
