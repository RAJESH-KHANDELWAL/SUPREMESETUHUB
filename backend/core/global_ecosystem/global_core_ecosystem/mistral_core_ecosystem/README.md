# MISTRAL CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Provider:** Mistral AI (`mistral`)  
**Layer:** CORE  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/mistral_core_ecosystem/`

## Mission
Mistral Core is the provider-level control plane for provider identity, product-family registration, capability taxonomy, tenant-aware policy metadata, readiness, discovery, dependency mapping and read-only master-catalog alignment.

## Canonical architecture
- `catalog.py`: provider identity and the nine existing product-family registrations.
- `product_catalog.py`: unified product offering inventory derived from the canonical catalog.
- `domain_catalog.py`: 18 responsibility domains and product-to-domain coverage.
- `contracts.py`: tenant context, opaque secret reference, readiness and result contracts.
- `master_catalog.py`: read-only mapping to the existing 2468-target master catalog.
- `policy.py`: tenant-context validation, capability classification and safe metadata projection.
- `module_service.py`: shared read-only service for product families.
- `domain_runtime.py`: shared read-only manager for domain metadata.
- `orchestrator.py`: product/domain discovery, health and dependency metadata.
- `service.py`: public provider status and service interface.
- `manager.py`: canonical Python entry point and `get_manager()`.
- `manager.php`: thin PHP interoperability facade; Python remains canonical.
- `product_ecosystem_index.json`: machine-readable inventory and master-catalog references.
- `backend/test/test_mistral_core.py`: structural, policy, mapping and boundary tests.
- `mistral_*_core_ecosystem/`: nine existing product folders, retained in place.

No fixed set of empty subfolders or duplicate product managers is generated. Product folders remain inventory boundaries until distinct, testable Core responsibilities require implementation.

## Existing product families
1. Agents
2. Audio
3. Batch
4. Chat
5. Embeddings
6. FIM Completions
7. Fine-tuning
8. Models
9. OCR

Each family maps to its existing sibling API package. The shared provider engine and runtime are referenced, not duplicated.

## Master catalog (2468 target)
The single source of truth is `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`. Mistral Core references the existing canonical technology topics `S09_artificial_intelligence` and `S09_machine_learning`. The file is read-only and is not copied or changed here. This Core adds **zero** numbered master-catalog entries; 2468 is a planning target, not a count of implemented Mistral products.

## Layer ownership
| Layer | Responsibility |
|---|---|
| Mistral CORE | Provider/product identity, taxonomy, contracts, policy metadata, readiness and discovery |
| Mistral API | Authentication transport, request/response handling and provider endpoint clients |
| Mistral ENGINE | Inference/tool execution, batch execution, retries and job orchestration |
| AI/runtime | Provider runtime adapter, model routing and runtime configuration |
| DATABASE | Shared persistence through the existing central database layer; no provider-specific database |
| STORAGE | Shared artifact/object storage and retention boundaries |
| APPLICATION | User-facing chat, agent, document, audio and model workflows |

## Security and correctness
- Never store API keys, tokens, passwords or secret values in Core.
- Use opaque secret references; resolve credentials only through the approved secret-management path.
- Tenant and actor identity must come from the authenticated application layer.
- A registered capability is not authorization, entitlement, model availability or proof of a successful API call.
- Fine-tuning, batch jobs, tool execution, uploads, writes and billing require explicit authorization in their owning layers.
- No network calls, OAuth exchange, inference, persistence, queue processing or background execution occurs in this Core package.
- Live Mistral connectivity is **not verified** by this metadata implementation.

## Master-catalog and database boundaries
The 2468 master catalog is read-only. Existing `backend/database/config.php` and the central database architecture are not modified. Mistral Core creates no database, table, credential, migration or provider-specific persistence path.
