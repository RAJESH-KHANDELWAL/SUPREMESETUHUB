# LEGACY BADA BUSINESS ECOSYSTEM PATH

This path is retained only as a backward-compatible import facade.

The canonical Bada Business product ecosystem and its complete platform resource implementation now live under:

backend/bada_business_ecosystem/

The platform links, referral destinations, programs, courses, products, events and registration resource definitions must be maintained only in that canonical package.

The broader HTTP API router, schemas, taxonomy and industry-specific API implementation currently remain under backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/. The top-level Bada Business package exposes that router through api_ecosystem; API transport code is not duplicated here.
