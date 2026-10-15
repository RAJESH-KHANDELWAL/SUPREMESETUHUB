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
