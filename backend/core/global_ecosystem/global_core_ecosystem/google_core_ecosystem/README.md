# GOOGLE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM

**Folder:** `backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/`

## Responsibility

The Google Core Ecosystem owns provider-level core registration, module discovery, capability metadata, configuration boundaries, and readiness/status contracts for Google-owned products. It does not duplicate Google API clients.

## Existing integration layers

- Existing shared Google core contracts: `backend/google/google_ecosystem/core/`
- Google provider API catalog: `backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/`
- Shared backend provider adapter: `backend/integrations/providers/google.py`

The core references those modules as the implementation/catalog boundaries. Do not create a second OAuth token manager or a duplicate API service here.

## Included core children

- Google Gmail Core Ecosystem
- Google Drive Core Ecosystem
- Google Calendar Core Ecosystem
- Google People Core Ecosystem
- Google Gemini Core Ecosystem
- Google Vertex AI Core Ecosystem

The catalog may be expanded to all Google API families as each service needs a distinct core responsibility, configuration policy, tests, and security review.

## Security

- OAuth scopes must be least-privilege and consented by the mailbox/user owner.
- Store secrets and refresh tokens in a managed, tenant-scoped secret store; never commit them.
- Core status is not evidence of OAuth connection or live API verification.
- User-specific access, token revocation, disconnect, quota, audit, and retry rules belong to the relevant secure runtime service.
