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

## Dedicated service and work/business APIs

- `global_services_api_ecosystem/` exposes the canonical Services, Platforms & Technology Integrations category catalogue through dedicated service routes.
- `global_work_business_api_ecosystem/` aggregates the A–Z work/business taxonomy, freelance/gig specialization registry and Jobs/Careers status without copying their canonical records.

Both routers are mounted by this package's main `routes.py` under the existing `/api/v1/global-ecosystem/business` prefix. These endpoints are taxonomy/discovery APIs; they do not imply live providers, vacancies, verified clients or payment execution.

