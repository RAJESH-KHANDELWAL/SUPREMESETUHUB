# LEGACY BADA BUSINESS GLOBAL ECOSYSTEM PATH

This directory is a compatibility facade only.

The canonical Bada Business product/resource ecosystem is:
`backend/bada_business_ecosystem/global_ecosystem/`

Maintain provider profiles, platform links, referral destinations and program
metadata only in that canonical package.

The HTTP API router, schemas, routes, taxonomy and integrations remain in the
separate API layer:
`backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`

No API transport code is duplicated here.
