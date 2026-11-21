# HUGGING FACE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Provider:** Hugging Face (`huggingface`)  
**Layer:** CORE  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/huggingface_core_ecosystem/`

## Mission
Provider-level, provider-neutral control plane for Hugging Face identity, product-family registration, domain taxonomy, capability metadata, tenant and secret-reference contracts, policy boundaries, readiness and dependency discovery.

## Canonical shared architecture
- `constants.py`: identity, canonical master-catalog references and layer paths.
- `manager.py`: stable Python entry point and `get_manager()`.
- `manager.php`: thin PHP 8+ interoperability/status facade.
- `catalog.py`: assembled provider, product and domain catalog.
- `product_catalog.py`: the 15 existing Hugging Face product/API families.
- `domain_catalog.py`: cross-product capability taxonomy.
- `contracts.py`: tenant, secret-reference, readiness and result contracts.
- `policy.py`: authorization, secret, licence, billing and production guardrails.
- `module_service.py`: shared read-only service used by product packages.
- `domain_runtime.py`: shared read-only manager for domain metadata.
- `orchestrator.py`: discovery, health and dependency mapping.
- `service.py`: public status/service interface.
- `test_huggingface_core.py`: structural, contract and layer-boundary tests.

## Product packages
The 15 existing product directories are retained and implemented as thin metadata adapters: Authentication, Billing, Datasets, Discussions, Downloads, Evaluation, Hub, Inference, Inference Endpoints, Models, Organizations, Spaces, Storage, Tasks and Webhooks. Each package delegates to the shared service. Product-specific HTTP clients and endpoint calls belong in API; execution, queues and deployments belong in ENGINE. No duplicate provider clients are introduced.

## Master 2468 catalog alignment
The source of truth is `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`, accessed read-only. This provider maps to the existing canonical topics `S09_artificial_intelligence` and `S09_machine_learning` under Technology & Digital Ecosystem. This implementation adds zero master-catalog entries and does not inflate the target count.

## Layer ownership
| Layer | Responsibility |
|---|---|
| Hugging Face CORE | Provider/product identity, catalog, taxonomy, policy, readiness and dependency metadata |
| Hugging Face API | Authentication transport, Hub/Inference/Endpoints/Datasets/Models/Spaces/etc. API clients |
| Hugging Face ENGINE | Inference execution, evaluation jobs, queues, retries and deployment execution |
| AI/runtime | Provider runtime adapters and model routing |
| DATABASE/STORAGE | Durable records, model/dataset artifacts, cache and retention |
| APPLICATION | User-facing model hub, organization, billing and inference workflows |

## Security and correctness
- Never store Hugging Face tokens or secret values in CORE, logs or catalog metadata.
- Store credentials in an external secret manager and pass references only.
- Model/dataset licences and gated access must be checked by the owning application/API/runtime before use.
- Billing, organization administration, webhooks, endpoint deployments and destructive actions require explicit authorization and audit in the execution layer.
- Product registration does not prove API implementation, account entitlement, quota, model availability or live connectivity.
- Live connection remains false until authenticated deployment smoke tests pass.
- CORE performs no provider HTTP requests, inference, downloads, billing transactions or deployment operations.

## Validation
Run the focused pytest suite, repository CI, Python compilation and PHP lint. Do not call this production-ready until those checks pass.
