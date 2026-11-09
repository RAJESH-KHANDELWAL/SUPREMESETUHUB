# OPENAI API ECOSYSTEM

Canonical provider root for OpenAI products, services, developer platforms and API capabilities in SUPREMESETUHUB.

## Naming convention

Each named OpenAI product or developer service gets its own child folder using:

`openai_<product_or_service>_api_ecosystem/`

The display name follows the same provider-first convention:

`OPENAI <PRODUCT OR SERVICE> API ECOSYSTEM`

## Product and service tree

- **OPENAI CHATGPT API ECOSYSTEM** — `openai_chatgpt_api_ecosystem/` — `active_catalog`
- **OPENAI CHATGPT BUSINESS API ECOSYSTEM** — `openai_chatgpt_business_api_ecosystem/` — `active_catalog`
- **OPENAI CHATGPT ENTERPRISE API ECOSYSTEM** — `openai_chatgpt_enterprise_api_ecosystem/` — `active_catalog`
- **OPENAI CHATGPT EDU API ECOSYSTEM** — `openai_chatgpt_education_api_ecosystem/` — `active_catalog`
- **OPENAI CHATGPT HEALTH API ECOSYSTEM** — `openai_chatgpt_health_api_ecosystem/` — `availability_dependent_catalog`
- **OPENAI CODEX API ECOSYSTEM** — `openai_codex_api_ecosystem/` — `active_catalog`
- **OPENAI DOTS API ECOSYSTEM** — `openai_dots_api_ecosystem/` — `availability_dependent_catalog`
- **OPENAI AGENTS API API ECOSYSTEM** — `openai_agents_api_ecosystem/` — `public_beta_catalog`
- **OPENAI AGENTS SDK API ECOSYSTEM** — `openai_agents_sdk_api_ecosystem/` — `active_catalog`
- **OPENAI APPS SDK API ECOSYSTEM** — `openai_apps_sdk_api_ecosystem/` — `active_catalog`
- **OPENAI CHATKIT API ECOSYSTEM** — `openai_chatkit_api_ecosystem/` — `active_catalog`
- **OPENAI OPENAI SDKS API ECOSYSTEM** — `openai_sdk_libraries_api_ecosystem/` — `active_catalog`
- **OPENAI PLUGINS AND MCP API ECOSYSTEM** — `openai_plugins_mcp_api_ecosystem/` — `active_catalog`
- **OPENAI SORA (RETIRED REFERENCE) API ECOSYSTEM** — `openai_sora_api_ecosystem/` — `retired_reference_only`

## Important distinction

This parent catalog is for **named OpenAI products and platforms**, like the Google parent catalog lists Gmail, Drive, Docs and Sheets. API capability families such as Responses, Embeddings, Images, Audio, Files, Batch, Moderation and Webhooks are a separate list in `openai_api_ecosystem.py`; they are not incorrectly presented as user-facing products.

ChatGPT plans/editions (Business, Enterprise and Education) are represented as distinct product/workspace children for discoverability, while remaining plan variants of ChatGPT. ChatGPT features such as voice, search, custom GPTs and deep research remain under ChatGPT unless OpenAI exposes them as separate products.

Sora is included only as a retired historical reference. OpenAI announced discontinuation of the Sora web/app experience and API in 2026; it must not be represented as an active service.

## User connection architecture

For API-enabled services, the intended user flow is:

1. User opens the relevant OpenAI product/service card.
2. User chooses Connect, where the product supports an external API connection.
3. User supplies their own API key or authorizes an official OAuth flow where supported.
4. Backend validates the credential server-side.
5. Backend stores credentials in encrypted, tenant-scoped secret storage.
6. UI displays connection status, supported usage/cost controls, disconnect and rotation actions.

A ChatGPT subscription is not the same as OpenAI API billing or API-key access. Do not request API keys for products that do not expose a supported public API.

## Security and implementation status

- Never commit API keys or place them in source code, logs, URLs, analytics or error responses.
- Use authenticated, tenant-scoped authorization and encrypted secret storage.
- Keep API capabilities separate from products and model families.
- Verify current official documentation, availability, account entitlements, scopes, terms and regional limitations before implementing any adapter.
- Catalog presence does not mean a live integration exists. Each child must report its actual implementation and connection status.

## Official references

- OpenAI products: https://openai.com/
- OpenAI developer platform: https://developers.openai.com/
- OpenAI API documentation: https://developers.openai.com/api/docs/
- Agents API announcement: https://openai.com/index/introducing-the-agents-api/
- Sora discontinuation notice: https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation
