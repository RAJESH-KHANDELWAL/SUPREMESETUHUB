# NSFWinfra Core Ecosystem

Provider Core metadata/control plane for the existing ten NSFWinfra product families. Follows Google Core's provider catalog, contracts, domain taxonomy, policy, orchestration, service and canonical `manager.py/get_manager()` pattern.

## Product packages (existing directories retained)
1. Account Limits
2. Anime Generation
3. Async Jobs
4. Image Editing
5. Image Generation
6. Image to Video
7. Image/Video Effects
8. Signed Uploads
9. Text to Video
10. Webhooks

## Root responsibilities
- `catalog.py`: provider and product-family inventory with existing package/API references.
- `product_catalog.py`: canonical product lookup.
- `domain_catalog.py`: 21 cross-product domains and coverage mapping.
- `contracts.py`: tenant context, opaque secret reference and result contract.
- `master_catalog.py`: read-only mapping/counts to master 2468 catalog.
- `policy.py`: tenant/capability policy classification and adult-content default-deny boundary.
- `module_service.py`: shared product metadata service.
- `domain_runtime.py`: read-only domain manager.
- `orchestrator.py`: products, domains, health, offerings and dependencies.
- `service.py`: provider status service.
- `manager.py`: canonical manager/get_manager().
- `manager.php`: thin metadata interoperability facade; Python is canonical.
- `product_ecosystem_index.json`: machine-readable inventory.
- `backend/test/test_nsfwinfra_core.py`: test suite.

No boilerplate product subfolders or duplicate clients are added. Existing ten folders remain as product boundaries until meaningful product-specific Core implementation is required.

## Existing dependencies verified in repository
- API catalog: `backend/api/global_ecosystem/global_api_ecosystem/nsfwinfra_api_ecosystem/`
- AI API package: `backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/nsfwinfra_ai_api_ecosystem/`
- AI Core facade: `backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/nsfwinfra_ai_core_ecosystem/`
- AI provider package: `backend/ai/global_ecosystem/global_ai_ecosystem/global_ai_providers/nsfwinfra_ai_ecosystem/`
- No duplicate API clients, AI facade, database or storage are created.

## Master ecosystem catalog (2468)
Read-only source `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` reports 246 target? Current expansion metadata: **246 current unique entries**, **2,222 remaining**, target **2,468**. NSFWinfra Core maps existing entries `S09_cloud_computing`, `S10_global_infrastructure`, `S10_global_ai_core`, `S12_ai_research`. This PR adds zero entries and does not modify the source.

## Domain coverage (21)
Provider governance; Account limits and quotas; Anime/style generation; Image generation/editing; Video generation/transformation; Media effects; Async jobs/lifecycle; Signed upload/asset handoff; Events/webhooks; Media asset metadata; Model catalog/capabilities; Content safety and age gating; Security/privacy/access; Storage/retention boundaries; Readiness/dependencies; Capability discovery; Error/retry metadata; Interoperability/integration; Usage/billing metadata; Tenant policy/authorization; Operations/observability.

## Safety, privacy and readiness
Adult-category access is default-deny; require 18+ verification, lawful policy, consent and rights as applicable. This is metadata only, not age verification/moderation implementation. Actual enforcement belongs to application/API execution layers. Tenant/actor identity must come from authenticated app context. Secrets are represented by opaque references, not stored. Generation/edit/upload/webhook execution, provider network calls, OAuth, DB writes, migrations, jobs and billing are not performed. No live provider readiness is claimed.
