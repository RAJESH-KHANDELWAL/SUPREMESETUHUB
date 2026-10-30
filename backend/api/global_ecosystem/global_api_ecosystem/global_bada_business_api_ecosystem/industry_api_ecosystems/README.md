# Industry API Ecosystems

Master India + Global business-industry taxonomy API under the existing `global_bada_business_api_ecosystem`.

## Endpoints
- `GET /api/v1/global-ecosystem/business/industries/status`
- `GET /api/v1/global-ecosystem/business/industries`
- `GET /api/v1/global-ecosystem/business/industries/{industry_id}`

List filters: `channel=online|offline|hybrid`, `coverage=india|global`, `q=<search>`, `include_adult=true`.

This is a taxonomy API, not a complete worldwide company directory and not a live integration with Google, Microsoft, AWS, Meta, OpenAI or other providers. Add provider adapters only after reviewing official API documentation, permissions, authentication, rate limits and terms. Never commit secrets.

The adult/sexual-wellness domain is separately classified as 18+. The query flag is not age verification; any future service requires applicable-law review, age assurance, consent, privacy and safety controls.
