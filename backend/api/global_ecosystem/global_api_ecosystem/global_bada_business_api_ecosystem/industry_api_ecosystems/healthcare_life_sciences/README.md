# Healthcare & Life Sciences API Ecosystem

Stable domain identifier: `healthcare_life_sciences`.

## Scope

This package provides a structured India-and-global category taxonomy across online, offline and hybrid channels. It is a discovery/API foundation, not a verified directory of providers, live vacancy/market feed, transaction system, or compliance certification.

## Endpoints

- `GET /industries/healthcare-life-sciences/status`
- `GET /industries/healthcare-life-sciences/categories`
- `GET /industries/healthcare-life-sciences/categories?q=...`
- `GET /industries/healthcare-life-sciences/categories/{category_id}`

The category list contains 15 top-level categories. Search matches category IDs, names and subcategory identifiers. Provider onboarding, source provenance, freshness, verification, permissions and jurisdiction-specific compliance must be implemented before presenting records as verified or operational.
