# GLOBAL API ECOSYSTEM — provider hierarchy

## Parent structure

`GLOBAL API ECOSYSTEM` is the provider/API directory above the existing API families. The catalog references existing code paths; it does not move or merge the separate runtime `backend/`, master `BACKEND/`, or visual/documentation `🖥️ BACKEND 🖥️/` systems.

### Existing API-family ecosystems

- AI, App, Business, Cloud, Communication, Companies, Database, Developer, Domain, Freelancer, Hosting, Individual, Integrations, Intimacy, Language, Payment, Platforms, Security, Server, Services, Social Media, Software, Storage, System, Tools, Video, Web and Website.
- The registry returns each family's canonical existing path so the work stays organized without duplicating its implementation.

### Provider API ecosystems

The top-level provider catalog includes Google, Microsoft, AWS, Apple, OpenAI, NSFWInfra, Anthropic, Meta, X, GitHub, Cloudflare, DigitalOcean, Oracle, IBM, NVIDIA, Hugging Face, DeepSeek, Mistral, Cohere, Stripe, PayPal, Twilio, Slack, Zoom, Salesforce, Adobe, Shopify and Atlassian.

Google, Microsoft, AWS and Apple link to the existing company-specific API ecosystem directories, plus their related platform directories when those already exist. They also link to the shared provider readiness adapters in `backend/integrations/providers/`. Existing files are referenced rather than copied.

Other vendors are present as catalog entries and are explicitly marked `CATALOG_ONLY` until a provider-specific adapter, auth lifecycle, durable token handling, least-privilege policy and live tests exist.

### GLOBAL AI API ECOSYSTEM

The AI API catalog is a filtered view of the same provider registry. It includes providers relevant to AI services (Google, Microsoft, AWS, OpenAI, NSFWInfra, Anthropic, Meta, NVIDIA, Hugging Face, DeepSeek, Mistral, Cohere, Oracle and IBM). The existing central runtime provider registry is shown separately, so catalog coverage is never confused with an implemented or connected AI provider.

## API routes

All routes are protected by the existing private-by-default middleware; they are not public unauthenticated endpoints.

- `GET /api/v1/global-api-ecosystem/status`
- `GET /api/v1/global-api-ecosystem/ecosystems`
- `GET /api/v1/global-api-ecosystem/providers`
- `GET /api/v1/global-api-ecosystem/providers/{provider_id}`
- `GET /api/v1/global-api-ecosystem/ai-providers`
- `GET /api/v1/global-ai-ecosystem/status`
- `GET /api/v1/global-ai-ecosystem/providers`
- `GET /api/v1/global-ai-ecosystem/api-ecosystems`

Use `?family=AI`, `?family=CLOUD`, `?family=STORAGE`, `?family=PAYMENT` and other listed family identifiers to filter the provider catalog.

## Status semantics

- `CONFIGURATION_READINESS_SCAFFOLD`: provider readiness metadata/configuration checks exist; this does not mean OAuth/API operations are complete.
- `CENTRAL_AI_ENGINE_REGISTRY`: a provider is registered in the current central AI engine; it still may require credentials and a live call.
- `PUBLIC_REPOSITORY_STATUS_CHECK_EXISTS`: the project has a limited public GitHub repository status check, not a general authenticated GitHub API integration.
- `CATALOG_ONLY`: documented discovery entry only; no live adapter is claimed.
- `live_connection_verified: false`: the catalog makes no live-connectivity claim.

## Next implementation gate

Implement provider-specific OAuth/API operations and token persistence in the appropriate family package, reuse existing company/platform code, and test scopes, ownership, revocation, errors and live sandbox access. Verify durable database/file storage and recovery before enabling production credentials or performing migrations. No account, billing resource, production credential or deployment is created by catalog changes alone.
