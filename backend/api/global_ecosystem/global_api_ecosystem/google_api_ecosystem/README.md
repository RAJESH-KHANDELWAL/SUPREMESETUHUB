# Google API Ecosystem

Canonical provider root: `google_api_ecosystem`. Each child directory is a Google product/API family with its own adapter and setup notes.

## Ecosystem families
- Workspace: Admin SDK, Calendar, Chat, Contacts/People, Docs, Drive, Forms, Gmail, Meet, Sheets, Slides.
- Growth and presence: Ads, Analytics, Business Profile, Maps Platform, Search Console, YouTube.
- Cloud and identity: Google Cloud, Firebase, Identity/OAuth, Vertex AI.
- AI: Google Gemini Developer API (`google_gemini_api_ecosystem`) and the unified Google AI provider facade (`google_ai_api_ecosystem`).

## Intended end-user experience
The platform owns backend deployment, routes, dependencies, API adapters, validation, health checks, and secret-management infrastructure. An end user should only select a provider, enter the required account data or authorize Google OAuth, and press **Connect**. They should not configure Python, server routes, package dependencies, or backend environment files.

## Important implementation boundary
The API adapters and client factories are code-level integrations, not proof of live connectivity. OAuth consent, API enablement, billing, IAM, quotas, product eligibility, and user authorization remain provider-controlled. A production multi-user Connect experience additionally requires:
1. Authenticated platform account identity (tenant identity must come from verified server-side authentication, never a body field).
2. Encrypted per-tenant credential storage with key rotation and access auditing.
3. OAuth state/PKCE validation and token refresh/revocation handling where OAuth is used.
4. Redaction of secrets from logs, traces, errors, analytics, and support exports.
5. Per-tenant rate limits, quotas, disconnect/delete controls, and integration health checks.

Gemini API keys are passed to the Gemini adapter at runtime and are not persisted by that adapter. Vertex AI and Google Workspace use their own Google Cloud/OAuth credential models. Do not reuse credentials across products.

## Security
Never commit API keys, OAuth client secrets, refresh tokens, service-account JSON, or user data. Use a managed secret store for platform-owned credentials and an authenticated encrypted vault for user-owned credentials. A connection is only "verified" after a real provider API request succeeds.
