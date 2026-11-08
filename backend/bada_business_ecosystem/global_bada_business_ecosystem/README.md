# GLOBAL ECOSYSTEM

Canonical global provider and platform-resource ecosystem owned by
BADA BUSINESS ECOSYSTEM.

This package owns Bada Business provider profiles, platform links, referral
destinations, programs and related product-resource metadata.

## Structure
- `platform_resources/catalog.py` — canonical provider/resource catalog
- `platform_resources/programs/` — program records
- `__init__.py` — package identity and catalog exports

## API separation
The HTTP API router, schemas, routes, industry taxonomy and integrations stay
in:
`backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`

The API router is exposed through
`backend/bada_business_ecosystem/api_ecosystem/` for stable registration.
API transport code is not duplicated in this package.

Provider links and program records are repository metadata; they do not prove
official API access, partnership, live availability or a live integration.
