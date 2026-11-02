# Jobs, Careers & Employment API Ecosystem

Stable domain identifier: `jobs_careers_employment`.

## Scope

This package provides a structured India-and-global category taxonomy across online, offline and hybrid channels. It is a discovery/API foundation, not a verified directory of providers, live vacancy/market feed, transaction system, or compliance certification.

## Endpoints

- `GET /industries/jobs-careers-employment/status`
- `GET /industries/jobs-careers-employment/categories`
- `GET /industries/jobs-careers-employment/categories?q=...`
- `GET /industries/jobs-careers-employment/categories/{category_id}`
- `GET /industries/jobs-careers-employment/employment-categories`
- `GET /industries/jobs-careers-employment/employment-categories?q=government`
- `GET /industries/jobs-careers-employment/employment-categories/{category_id}`

The industry-service category list contains 15 top-level categories (job portals, staffing, HR, career services and related industries). A separate employment taxonomy is also exposed through `/employment-categories`; it is sourced from the maintained Work, Jobs & Careers domain and includes Government Jobs, Private Jobs, Corporate Jobs, Public Sector Jobs and other job classifications. These two taxonomies serve different purposes and are not merged or duplicated. Search matches category IDs, names and subcategory identifiers. This Jobs, Careers & Employment API is mounted last in the Industry API Ecosystem router and registry. Provider onboarding, source provenance, freshness, verification, permissions and jurisdiction-specific compliance must be implemented before presenting records as verified or operational.
