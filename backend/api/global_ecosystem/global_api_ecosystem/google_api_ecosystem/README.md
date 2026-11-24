# GOOGLE API ECOSYSTEM

Canonical provider root for Google-owned APIs and products in SUPREMESETUHUB.

## Provider structure

- `google_api_ecosystem.py` — provider registry and child catalog metadata.
- `google_gemini_api_ecosystem/` — Gemini Developer API adapter scaffold.
- `google_vertex_ai_api_ecosystem/` — Vertex AI catalog and future adapter boundary.
- Other `google_*_api_ecosystem/` folders — product-specific API catalogs.

## Integration contract

Provider metadata is catalog information, not proof of live connectivity. The shared backend provider adapter lives at:

`backend/integrations/providers/google.py`

Its health response reports whether OAuth configuration is present. A successful health response does not prove that Google OAuth consent, token refresh or an API operation succeeded.

## Setup

Configure server-side environment variables in the deployment secret manager:

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REDIRECT_URI`

Gemini Developer API is separate from Google Workspace OAuth. Configure `GOOGLE_GEMINI_API_KEY` or use a user-supplied key only through a secure, server-side secret flow. Never commit credentials.

## Security and ownership

- Use least-privilege OAuth scopes and validate redirect URIs.
- Store refresh tokens in encrypted, tenant-scoped secret storage.
- Never log, return, or expose access tokens, refresh tokens, or API keys.
- Implement disconnect, revocation, rotation, quota and request-timeout handling before enabling multi-user connections.
- Keep Google-owned APIs under this provider; use cross-ecosystem references rather than duplicating catalogs.

## Status semantics

`NEEDS_CONFIGURATION` means required environment settings are absent.
`CONFIGURED_NOT_VERIFIED` means settings are present, not that a provider call succeeded.
Only successful deployment-level authorization and API smoke tests may mark an integration connected.
