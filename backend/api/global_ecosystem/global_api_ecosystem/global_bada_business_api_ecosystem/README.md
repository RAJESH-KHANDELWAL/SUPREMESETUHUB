# GLOBAL BADA BUSINESS API ECOSYSTEM

This package is the API implementation exposed by the top-level BADA BUSINESS ECOSYSTEM.

Product/domain ownership belongs to:

backend/global_ecosystem/global_bada_business_ecosystem/

The API package owns HTTP transport, route handlers, request/response schemas, business taxonomy, industry registries, capability contracts and integrations. It consumes platform-owned links and program resources from the top-level Bada Business Ecosystem catalog; it must not maintain duplicate provider referral/course catalogs.

## API router
The existing router and nested API modules remain in this location to preserve current import paths, route registration and integration compatibility. The top-level package exposes the router through:

backend/global_ecosystem/global_bada_business_ecosystem/api_ecosystem/

## Integration status
Provider references are metadata only. They do not imply a partnership, official developer API access, authentication or live external connectivity.
