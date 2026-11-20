# GLOBAL INTEGRATIONS CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Layer:** CORE  
**Status:** `CORE_CATALOG_ONLY`

## Mission
Provider-neutral control plane for provider-family identity, integration-domain taxonomy, capability metadata, sensitivity classification, policy boundaries, dependency mapping, readiness metadata and read-only discovery.

## Canonical files
- `registry.py`: single curated source for domain and provider-family definitions.
- `models.py` / `contracts.py`: validated immutable metadata contracts and stable exports.
- `catalog.py`: normalized domain/provider catalog, lookup and search.
- `manager.py`: canonical Python entry point; `manager.php`: PHP metadata interoperability facade.
- `domain_runtime.py`: shared runtime for all domain-scoped managers.
- `orchestrator.py`: discovery, health and dependency mapping.
- `service.py`: public service facade and safe metadata inspection.
- `policy.py`: metadata redaction and restricted-domain guardrails.
- `ecosystem_manifest.json`: machine-readable domain/provider inventory.
- `test_global_integrations_core.py`: structural and behavior tests.
- Each domain package contains a small `README.md`, `__init__.py` and `manager.py`; shared logic is not duplicated.

## Master catalogue relationship
The master taxonomy remains `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` (target: 2,468 meaningful unique ecosystem entries). This package references it as the wider planning source; it does not copy those entries, treat 2,468 as a provider count, or invent records to reach that target. The 31 integration domains and provider-family descriptors are a separate, scoped registry.

## Layer ownership
| Layer | Responsibility |
|---|---|
| CORE | Provider identity, domain taxonomy, capability contracts, policy/readiness metadata, read-only discovery |
| API | Authentication, request validation, HTTP transport, response normalization |
| ADAPTERS / INTEGRATIONS | Provider SDKs, webhooks, protocol translation |
| SECURITY / CONFIGURATION | Secret storage/resolution, authorization, consent, rotation |
| DATABASE / STORAGE | Persistence, tenant isolation, retention, backups |
| ENGINE | Execution, queues, retries, scheduling, lifecycle |
| APP / UI | User sessions, consent UX, user workflows |

## Safety boundaries
1. Never store credentials, tokens, API keys, client secrets, private keys, webhook secrets or raw customer payloads in Core.
2. Store only opaque secret references in approved security/configuration boundaries.
3. Treat imported provider records, API responses and webhook payloads as untrusted.
4. Enforce tenant isolation, least privilege, scopes, consent, rate limits and regional requirements in the authenticated runtime.
5. Restricted domains require applicable age assurance, consent, rights review, moderation and regional legal review before runtime operations.
6. Financial, destructive, administrative, publishing and externally visible actions require explicit authorization, idempotency and audit evidence.
7. Catalog registration does not prove account ownership, entitlement, API availability, adapter readiness or live connectivity.

## Core operations
Status/health, list/search/lookup, metadata inspection/redaction, domain capability summaries and dependency maps.

## Not implemented here
OAuth exchange, provider API calls, SDK execution, webhook processing, secret resolution, persistence, billing, jobs or provisioning.

## Validation
```bash
python -m pytest backend/core/global_ecosystem/global_core_ecosystem/global_integrations_core_ecosystem/test_global_integrations_core.py -q
```
