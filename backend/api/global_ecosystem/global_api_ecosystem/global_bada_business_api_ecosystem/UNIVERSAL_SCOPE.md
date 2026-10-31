# Universal India + Global Work & Business Scope

## Purpose

This package adds a shared classification layer for the India + worldwide
work, careers, freelancing, gig work, education, businesses, entrepreneurship,
homemaker economy, professional industries, family/community services,
investment support, public/social-impact services and lawful adult 18+ industry.

It complements the existing 67-category business catalog and 39-industry
scaffold. It does not replace those registries and does not claim that every
worldwide company, vacancy, service or person is already listed.

## Implemented in this change

- `universal_scope_registry.py`: 12 top-level domains with stable IDs and
  curated subcategory IDs, audience groups, delivery modes and adult flags.
- Shared dimensions: India/global coverage, work arrangements, audience
  groups, business sizes and business lifecycle stages.
- Helper functions: list domains, get one domain, search subcategories and
  validate registry structure.
- FastAPI routes:
  - `GET /api/v1/global-ecosystem/business/universal/domains`
  - `GET /api/v1/global-ecosystem/business/universal/domains/{domain_id}`
  - `GET /api/v1/global-ecosystem/business/universal/search?q=...`
  - `GET /api/v1/global-ecosystem/business/universal/integrity`

## Adult 18+ handling

The adult domain is excluded from list/search results by default. The
`include_adult=true` query parameter only exposes taxonomy metadata; it is
NOT age verification, access control or legal authorization. A production
application must enforce age assurance, consent, privacy, moderation,
safeguarding and country-specific legal requirements server-side. Do not
expose adult records to minors or jurisdictions where the activity is unlawful.

## Important status boundary

The registry status is `taxonomy_catalog_only`. Structural validation checks
IDs and duplicate/empty taxonomy entries; it does not prove market coverage,
business legitimacy, API connectivity, live job availability, payment
processing, user identity or legal compliance. Provider integrations must be
implemented separately using official documentation, explicit authorization,
secure secrets, rate-limit handling and provider terms.

## Next implementation phases

1. Add unit tests and connect the registry to the existing search/facets layer.
2. Normalize the existing 67 categories and 39 industry packages against the
   universal IDs; resolve duplicates and ownership boundaries.
3. Add jurisdiction-aware geography, language, currency and compliance data.
4. Design verified business, employer, opportunity and service records with
   provenance, freshness and moderation states.
5. Build opt-in official provider adapters and integration health checks.
6. Implement authentication, authorization, adult age assurance, privacy,
   consent, audit logging, abuse prevention and data-retention controls.
7. Run backend tests, route tests, security checks and deployment verification.

A taxonomy is a classification system, not a live worldwide directory. Do not
label a domain as fully operational until its data, APIs, tests and safeguards
have been independently verified.
