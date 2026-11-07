# GLOBAL DEEPSEEK API ECOSYSTEM

Provider-owned catalog and integration boundary for official DeepSeek APIs.

## Official API capabilities represented here
- **Chat Completions API** — `POST /chat/completions`
- **Responses API** — `POST /responses`
- **Search API** — `POST /v1/tools/search`
- **Fetch API** — `POST /v1/tools/fetch`

Official OpenAI-compatible API base URL: `https://api.deepseek.com`
Authentication: server-side Bearer API key supplied through `DEEPSEEK_API_KEY`.

## Current model identifiers
- `deepseek-flash`
- `deepseek-v4-pro`

Model availability and features can change; consult DeepSeek's official model documentation before enabling a model in production.

## Setup
1. Create an API key in the official DeepSeek platform.
2. Add `DEEPSEEK_API_KEY` to the backend's secret/environment configuration.
3. Keep the key server-side; never commit it to Git or expose it to browser code.
4. Check provider readiness through the integration registry.
5. Implement and run an authorized live API smoke test before marking connectivity verified.

## Implementation status
The provider adapter currently checks whether the server-side key is configured. It does **not** make network requests, validate the key, or prove live connectivity. Chat/Responses/Search/Fetch request execution must be implemented and tested separately.

## Official documentation
- Chat Completions: https://api-docs.deepseek.com/api/create-chat-completion/
- Responses API: https://api-docs.deepseek.com/api/create-response/
- Authentication and API overview: https://api-docs.deepseek.com/api/deepseek-api/
- First API call: https://api-docs.deepseek.com/quick_start/agent_integrations/
- Search & Fetch: https://api-docs.deepseek.com/guides/search/
- Models and pricing: https://api-docs.deepseek.com/quick_start/pricing/
