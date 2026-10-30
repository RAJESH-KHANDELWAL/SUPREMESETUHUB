# GLOBAL BADA BUSINESS API ECOSYSTEM

The central business-sector and business-classification layer for SUPREMESETUHUB.

## Scope

This ecosystem classifies businesses and organisations across offline, online and
hybrid operations, from self-employed and home-based businesses through MSMEs,
startups, enterprises and multinational groups. It covers sectors, business
entities, products, services, commerce, operations, partnerships, funding,
franchising, trade, compliance and provider ecosystems.

The sector catalogue is intentionally curated and extensible. It is **not** an
exhaustive list of every business, company, provider, licence or opportunity in
the world. New records should use stable IDs and reviewed taxonomy additions.

## Separation of responsibilities

- **Global Bada Business** owns business entities, sectors, business models,
  business capabilities, products/services and commercial provider discovery.
- **Global World** owns the cross-domain world/life taxonomy and links to the
  other ecosystems.
- **Global People, Work & Life** owns person profiles, education, jobs,
  households, family and life situations.
- **Global Relationship & Intimacy** owns relationship and intimacy services.
- Business records may reference people, jobs or relationship services using
  stable IDs and authorised APIs; do not duplicate their source records here.

A person may have several roles (for example, student, employee and founder).
Those roles do not determine business size. A homemaker may also operate a
registered enterprise; model the person role and business entity separately.

## Classification dimensions

The `/dimensions` API exposes controlled vocabularies for entity type, size,
operating model, ownership, lifecycle, revenue model, customer segment, market
scope, business capabilities and verification state.

Business size labels are descriptive only. Apply the relevant country's legal
MSME or company-size thresholds when making statutory determinations.

## API

- `GET /api/v1/global-ecosystem/business/status`
- `GET /api/v1/global-ecosystem/business/modules`
- `GET /api/v1/global-ecosystem/business/modules/{module_id}`
- `GET /api/v1/global-ecosystem/business/dimensions`
- `GET /api/v1/global-ecosystem/business/dimensions/{dimension_id}`
- `GET /api/v1/global-ecosystem/business/catalog`
- `GET /api/v1/global-ecosystem/business/catalog/search?q=...`
- `GET /api/v1/global-ecosystem/business/catalog/{category_id}`

The catalog and dimensions are discovery metadata. They do not create a business
account, verify a company, confirm a licence, provide financial advice, or
establish a live third-party integration. Provider adapters require official
documentation, credentials, terms review, secure secret handling, and tests.

## Adult-industry boundary

Adult-industry business categories remain separately classified and excluded
from ordinary catalog results unless explicitly requested. A query flag is only
a discovery filter; it is **not** age assurance, authorisation or production
access control. Any production adult service requires robust age assurance,
consent and performer-safety processes, privacy, moderation, and jurisdiction-
specific legal review. No minors, coercion, trafficking, exploitation or
non-consensual intimate imagery are permitted.

## Extending the taxonomy

1. Check for an existing category before adding a new one.
2. Use stable, lowercase, hyphenated category IDs.
3. Keep sector categories distinct from cross-cutting dimensions.
4. Add online/offline/hybrid modes and meaningful subcategories.
5. Keep adult-only classification explicit and excluded by default.
6. Add tests for new categories, filtering and API responses.
7. Do not claim global completeness or live integration without evidence.
