# GLOBAL PEOPLE, WORK & LIFE API ECOSYSTEM

This is a sibling API ecosystem package, architecturally parallel to the existing
AI, APP, CLOUD and DATABASE API ecosystem packages. It is not nested inside the
Bada Business sector taxonomy.

## Endpoints

- `GET /api/v1/global-people-life/status`
- `GET /api/v1/global-people-life/domains`
- `GET /api/v1/global-people-life/domains?include_adult=true`
- `GET /api/v1/global-people-life/domains/search?q=student`
- `GET /api/v1/global-people-life/domains/{domain_id}`

## Design

The package separates catalog data, service logic, response schemas and FastAPI
routes. People/life situations are represented as domains and cross-cutting facets;
they are not copied into AI, APP, CLOUD or DATABASE provider directories.

Adult-only classifications are excluded by default and require an explicit
`include_adult=true` request. This flag is only a discovery filter: it is not age
verification or permission to access adult content. Any future adult service needs
verified adults, documented and ongoing consent, privacy safeguards, moderation,
and jurisdiction-specific legal review. Family safety and survivor support remain
separate from adult entertainment.

This package is a read-only taxonomy catalog. It is not a live global directory,
job board, booking system, payment service, age-verification system, or live third-
party integration.
