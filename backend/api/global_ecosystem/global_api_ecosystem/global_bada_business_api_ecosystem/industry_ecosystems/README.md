# Bada Business Industry Ecosystems

This package organizes business-facing industries under the existing `global_bada_business_api_ecosystem`.

## Scope

- India and international provider coverage.
- Offline, online and hybrid business models.
- Businesses, companies, products, services, marketplaces, professional providers and integrations.
- Audience and people records (students, job seekers, households, couples, etc.) should remain in their owning people/work/life systems; this package catalogs the businesses and services that serve them.
- Adult and sexual-wellness business categories are explicitly 18+ and require jurisdiction-aware legal, consent, privacy and safety controls.

## Important status

This is a structural taxonomy scaffold, not a complete worldwide company directory and not a live integration with the listed providers. Provider records and API adapters must be added only after their official documentation, authentication method, permitted use, rate limits and terms are verified. Never commit API keys or secrets.

## Standard domain layout

Each domain package can grow into these modules as needed:

- `catalog.py`: curated categories and provider metadata.
- `schemas.py`: validated request/response models.
- `service.py`: business logic.
- `routes.py`: API endpoints.
- `integrations/`: provider-specific adapters.
- `tests/`: unit and contract tests.
- `README.md`: coverage, data provenance, API status and compliance notes.

Do not create empty or misleading live integrations. Mark each provider as `catalog_only`, `planned`, `sandbox` or `live_verified`.
