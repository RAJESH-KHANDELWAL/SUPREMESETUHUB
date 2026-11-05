# Industry API Ecosystems

Master India + Global business-industry taxonomy API under the existing `global_bada_business_api_ecosystem`. Industry implementation packages now live as sibling domain folders directly under `global_bada_business_api_ecosystem/`; this directory retains the master registry, schemas, service, routes, router coverage and tests.

## Endpoints
- `GET /api/v1/global-ecosystem/business/industries/status`
- `GET /api/v1/global-ecosystem/business/industries`
- `GET /api/v1/global-ecosystem/business/industries/{industry_id}`

List filters: `channel=online|offline|hybrid`, `coverage=india|global`, `q=<search>`, `include_adult=true`.

This is a taxonomy API, not a complete worldwide company directory and not a live integration with Google, Microsoft, AWS, Meta, OpenAI or other providers. Add provider adapters only after reviewing official API documentation, permissions, authentication, rate limits and terms. Never commit secrets.

International Trade, Import-Export, Customs & Global Commerce is registered and routed as a dedicated cross-border trade taxonomy, separate from generic company/trade categories, agriculture-specific trade and freight execution. Arts, Culture, Heritage & Creative Economy is registered and routed as its own cultural-sector taxonomy, separate from commercial media and entertainment. Manufacturing, Industrial & Industries is maintained directly at the Bada Business root; its dedicated router is mounted through this industry API. The package is not a child of `industry_api_ecosystems/`.

The adult/sexual-wellness domain is separately classified as 18+. The query flag is not age verification; any future service requires applicable-law review, age assurance, consent, privacy and safety controls.
