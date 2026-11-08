# LEGACY BADA BUSINESS ECOSYSTEM PATH

This package is retained for backward-compatible imports only.

The canonical product/domain root is now:

backend/bada_business_ecosystem/

The existing platform resource implementation is temporarily kept here to avoid breaking imports while consumers migrate. The top-level package exposes this catalog through its platform_resources module.

Do not add new Bada Business domain modules here. Add new platform resources, links, programs, courses, products, events, registration definitions and referral metadata under backend/bada_business_ecosystem/.

The API implementation remains under backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/ and is exposed through backend/bada_business_ecosystem/api_ecosystem/.

Catalog snapshots and provider links are not verified evidence of current availability, official API access, partnership or a live connection.
