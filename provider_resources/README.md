# BADA BUSINESS ECOSYSTEM

Canonical product and provider-resource package for Bada Business.

## Structure

- `courses/` — course resource namespace
- `events/` — event and webinar resources
- `links/` — official and referral destinations
- `platform/` — platform identity and profile
- `platform_resources/` — provider catalog and program snapshots
- `products/` — product resources
- `programs/` — program domain namespace
- `referrals/` — referral metadata
- `registration/` — registration resources

There is no nested GLOBAL ECOSYSTEM package and no API facade in this
product/resource package.

## API boundary

HTTP routers, schemas, routes, taxonomy and integrations remain separately
owned by `backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`.
Do not import API transport code from this package.
