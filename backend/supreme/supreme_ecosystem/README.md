# SUPREME ECOSYSTEM

This is the child ecosystem of **SUPREME**. The canonical domain layout is:

```text
backend/
└── supreme/
    └── supreme_ecosystem/
        ├── supreme_api_ecosystem/
        ├── supreme_business_ecosystem/
        ├── supreme_cloud_ecosystem/
        └── supreme_ai_ecosystem/
```

Domain responsibilities:
- **SUPREME API ECOSYSTEM** — API routing, endpoint contracts, request/response handling, and API adapters.
- **SUPREME BUSINESS ECOSYSTEM** — business services, business workflows, and the Global Business Ecosystem.
- **SUPREME CLOUD ECOSYSTEM** — cloud orchestration and cloud-provider adapters.
- **SUPREME AI ECOSYSTEM** — SUPREME-specific AI capabilities and AI integrations.

Existing domain paths:
- Global Business Ecosystem: `supreme_business_ecosystem/global_business_ecosystem/`
- SUPREME AI Ecosystem: `supreme_ai_ecosystem/`
- The legacy Global AI API source remains under `backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/` to avoid breaking existing source paths. It is bridged by `/api/v1/global-ai-ecosystem`, while the existing Central AI and SUPREME PERSONAL AI APIs remain registered.

**Safe migration rule:** the new API and Cloud packages establish the target structure. Existing modules are not blindly moved because imports, route registration, tests, and deployment entry points must be updated together. Migrate each module only after its dependencies and runtime wiring are checked.

Private owner-control routes:
- `/api/v1/supreme-ecosystem/business/status`
- `/api/v1/supreme-ecosystem/ai/status`

Public API route registration does not imply public data access; the backend's owner-only middleware applies. Provider credentials and live runtime behavior still require deployment configuration and tests.


## CRM Ecosystem boundary

The shared people-facing CRM domain is implemented in `backend/crm/`. The CRM
Ecosystem integration point is `backend/supreme/supreme_ecosystem/crm.py` and
belongs only to this Supreme Ecosystem layer. Do not create a nested
`backend/crm/people_crm_ecosystem/` package or merge the owner's private CRM data.

Google Contacts and Google Sheets must remain NOT_CONNECTED until OAuth,
least-privilege scopes, secure token storage, provider adapters, sync policies,
and integration tests are complete. Read-only preview is not live synchronization.

## Functional ecosystem catalog

The capability catalog and its functional ecosystem folders live directly in this package:

- `registry.py` — read-only capability registry; it does not initialize services or claim deployment status.
- `SUPREME-API-ECOSYSTEM/` — API routing, authentication boundaries, status and delivery responsibilities.
- `SUPREME-BUSINESS-ECOSYSTEM/` — business, project, opportunity, matching, work/income and marketplace responsibilities.

These folders document functional ownership. Live routers and services remain at their registered runtime paths until their imports, tests and deployment wiring are migrated together.
