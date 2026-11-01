# Global Company, Business and Freelancer Ecosystem

## Architecture

This package follows the modular domain-package pattern used by `global_bada_business_api_ecosystem`: root-level API and classification registries, dedicated class packages, and separate industry, country and provider support modules.

```text
global_company_companies_api_ecosystem/
├── README.md
├── __init__.py
├── routes.py / schemas.py / service.py
├── company_catalog.py / business_catalog.py / freelancer_catalog.py
├── classification_registry.py / entity_registry.py / global_company_world_map.py
├── company_legal_entities_api_ecosystem/
├── business_enterprises_api_ecosystem/
├── freelancer_independent_professionals_api_ecosystem/
├── industry_api_ecosystems/
├── country_api_ecosystems/
├── provider_api_ecosystems/
├── data/ / integrations/ / services/ / tools/ / tests/
```

## Three distinct record classes

- **company** — registered legal entities and formally constituted organizations.
- **business** — operating businesses not necessarily represented as a separately registered company, including sole proprietors, MSMEs, startups and franchises.
- **freelancer** — independent individual professionals and service providers.

The root package owns one normalized registry and shared search. Each class package owns its taxonomy, profile model, category-specific service facade and routes. This avoids three divergent profile stores.

## API surface

Mounted under `/api/v1/global-api-ecosystem`. Existing unified endpoints remain available: `/global/companies`, `/global/businesses`, `/global/freelancers`, status, A-Z, source directory and profile lookup.

New endpoints:
- `/global/company-directory/architecture`
- `/global/company-directory/classes` and `/classes/{record_type}`
- `/global/company-directory/classes/integrity`
- `/global/company-directory/world-map`
- `/global/company-directory/industries`
- Each class has `/global/company-directory/{company|business|freelancer}/catalog`, `/profiles`, `/search` and `/profiles/{profile_id}`.

## Data integrity and current boundary

Stable IDs must be unique; each record needs a name and subtype. Verified records require traceable source URLs. Industry, legal status, country, business size and verification are independent dimensions. The local JSON registry currently contains zero profiles. Country source metadata is not a live government connection, and provider product APIs are not automatically company-registration data sources. No worldwide completeness or live external adapter is claimed.
