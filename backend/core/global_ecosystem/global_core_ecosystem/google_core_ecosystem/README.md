# GOOGLE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Folder:** `backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/`

## Responsibility

The Google Core Ecosystem owns provider-level registration, lifecycle, module discovery, capability metadata, policy boundaries and readiness/status contracts for Google-owned products. It does not duplicate Google API clients.

## Existing integration layers

- Existing shared Google core contracts: `backend/global_ecosystem/google_ecosystem/runtime/core/`
- Google provider API catalog: `backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/`
- Shared backend Google adapter: `backend/integrations/providers/google.py`
- Google engine layer: `backend/engines/global_ecosystem/google_engine/`

The Core catalog references these implementation boundaries. Do not create a second OAuth token manager or duplicate API transport.

## Dedicated Google Core child packages

Every family has its own `google_*_core_ecosystem/` package below this folder:

- Gmail, Drive, Calendar, Contacts, People
- Docs, Sheets, Slides, Forms, Chat, Meet
- Admin SDK, Identity & OAuth
- YouTube, Maps Platform, Business Profile
- Ads, Analytics, Search Console
- Cloud, Firebase, Gemini, Vertex AI

The central catalog currently registers 23 child Core Ecosystems. Each package exposes its Core identity and points to the matching Google API catalog. Gmail also has a Core facade delegating to the existing Gmail API adapter.

## Security and readiness

- OAuth scopes must be least-privilege and consented by the mailbox/user owner.
- Secrets and refresh tokens must be held in a managed, tenant-scoped secret store; never commit credentials.
- Core and Engine catalog status is not evidence of OAuth consent or a live API connection.
- User-specific access, token revocation, disconnect, quota, audit and retries belong to the relevant secure runtime service.
- Product families marked catalog-only need their own runtime adapters and deployment-level tests before use.
