# DEEPSEEK API ECOSYSTEM

Canonical provider-owned root for DeepSeek APIs in SUPREMESETUHUB.

## Provider structure
- `deepseek_api_ecosystem.py` — provider registry, API-family metadata and safe catalog listing.
- `deepseek_chat_completions_api_ecosystem/` — Chat Completions API family.
- `deepseek_responses_api_ecosystem/` — Responses API family.
- `deepseek_search_api_ecosystem/` — Search tool API family.
- `deepseek_fetch_api_ecosystem/` — Fetch tool API family.
- Shared provider readiness adapter: `backend/integrations/providers/deepseek.py`.
- Shared integration registration: `backend/integrations/registry.py`.

## Authentication and setup
Use the official DeepSeek platform to create an API key, then configure it server-side as `DEEPSEEK_API_KEY` in the deployment secret manager. The API base URL is `https://api.deepseek.com`. Never commit API keys or expose them in browser code.

## API families
| Family | Endpoint | Purpose |
|---|---|---|
| Chat Completions | `POST /chat/completions` | Conversational and text-generation requests |
| Responses | `POST /responses` | Responses-style model interactions |
| Search | `POST /v1/tools/search` | Search tool requests where enabled |
| Fetch | `POST /v1/tools/fetch` | Fetch tool requests where enabled |

## Model catalog
Model identifiers are maintained as catalog metadata and may change. Verify current availability, account entitlement and pricing in DeepSeek's official documentation before production use.

## Security and operational requirements
- Keep `DEEPSEEK_API_KEY` in a server-side secret manager.
- Never return credentials in metadata, logs or API responses.
- Apply tenant authorization, request timeouts, bounded retries and rate limits.
- Track usage and costs; handle provider errors without exposing secrets.
- Add a live smoke test before marking any connection verified.

## Status semantics
The integration adapter currently checks whether the server-side API key is configured. It does not make network requests, validate the key or prove live connectivity. Each API family is a documentation/catalog scaffold until its request execution and tests are implemented.

## Official documentation
- [DeepSeek API overview](https://api-docs.deepseek.com/api/deepseek-api/)
- [Chat Completions](https://api-docs.deepseek.com/api/create-chat-completion/)
- [Responses API](https://api-docs.deepseek.com/api/create-response/)
- [Search and Fetch tools](https://api-docs.deepseek.com/guides/search/)
- [Models and pricing](https://api-docs.deepseek.com/quick_start/pricing/)
