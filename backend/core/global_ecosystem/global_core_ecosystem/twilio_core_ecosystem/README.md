# TWILIO CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/twilio_core_ecosystem/`

## Mission
Provider-specific, read-only control plane for Twilio identity, product-family discovery, communication capability classification, tenant-scoped metadata policy, readiness and cross-layer dependency mapping. The design follows the separation-of-responsibilities pattern used by `google_core_ecosystem/`.

## Existing ecosystem alignment
- Provider API metadata: `backend/api/global_ecosystem/global_api_ecosystem/twilio_api_ecosystem/`
- Communication category: `backend/api/global_ecosystem/global_api_ecosystem/global_communication_api_ecosystem/twilio_communication_api_ecosystem/`
- Tools category: `backend/api/global_ecosystem/global_api_ecosystem/global_tools_api_ecosystem/twilio_tools_api_ecosystem/`
- Existing generic Tools provider facade remains owned by Global Tools Core; this package is the provider-wide root and does not duplicate that package.
- Existing Twilio ENGINE and STORAGE namespaces remain independently owned by those layers.

## Canonical files
- `manager.py`: canonical Python entry point and `get_manager()`.
- `manager.php`: thin PHP metadata interoperability facade; Python remains canonical.
- `catalog.py`: provider identity, product families and category references.
- `contracts.py`: tenant context, readiness and structured result contracts.
- `policy.py`: fail-closed metadata policy for sensitive operations.
- `service.py`: read-only status, inventory, health and 2468 master-catalog availability.
- `orchestrator.py`: cross-layer dependency metadata and product discovery.
- `tests/test_twilio_core.py`: focused offline contract and behavior tests.

## Product-family inventory
The initial curated families are Programmable Messaging, Programmable Voice, Programmable Video, Verify and SendGrid Email API. SendGrid is represented as a separately entitled product family; no assumption is made that a Twilio account automatically includes it. Product names are discovery metadata, not a guarantee of regional availability, account entitlement, API coverage or implementation.

## Master catalog
The package reads `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` only to report availability and the 2468 target. It does not write to the master file, manufacture numbered entries or change the 246 current unique entries. A separate module-index registration is architecture metadata and does not increment the numbered target.

## Layer boundaries and security
- CORE: provider identity, product taxonomy, metadata policy and readiness.
- API: credentials/OAuth where applicable, SDK/HTTP transport, webhooks and response normalization.
- ENGINE: execution, retries, queues and scheduling.
- DATABASE/STORAGE: durable records and media artifacts.
- Secrets stay outside source control and outside Core.
- Core policy results do not replace authenticated application authorization or Twilio-side permissions.
- No messages, calls, verification codes, video rooms, phone-number purchases, billing changes or other provider-side actions are executed here.

## Readiness
Current status is `CORE_CATALOG_ONLY`. No credentials are configured, no provider adapter is claimed by this package, and live connectivity remains unverified. A live status requires configured deployment secrets, scoped authorization, provider-specific adapter tests and a successful smoke test.
