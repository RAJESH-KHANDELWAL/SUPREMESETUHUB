# BADA BUSINESS PLATFORM RESOURCE COMPATIBILITY PACKAGE

The canonical Bada Business platform resources now live under:

`backend/bada_business/global_ecosystem/global_bada_business_ecosystem/platform_resources/`

This API-side package is retained as a backward-compatible import facade only. It does not own a second copy of platform links or program catalogs.

## API ownership

The broader API implementation remains at:

`backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`

That package owns HTTP routes, taxonomy, industry registries, capability contracts and integrations. It exposes the canonical platform resource catalog through its read-only resource endpoint.

## Verification

The catalog contains user-supplied page snapshots and existing repository referral links. They are not independently verified and do not establish an official public developer API, partnership or live integration. Recheck availability, prices, dates, contact details and terms directly with Bada Business.
