# SUPREMESETUHUB Global World A–Z Ecosystem

This package is the top-level discovery taxonomy for the Global World scope: traditional and emerging work, business and commerce, people and family life, education, jobs, entrepreneurship, professional services, technology, health, relationships, lawful adult-only categories, public services and global locations.

## API

- `GET /api/v1/global-world/status`
- `GET /api/v1/global-world/domains`
- `GET /api/v1/global-world/domains?include_adult=true`
- `GET /api/v1/global-world/domains/search?q=student`
- `GET /api/v1/global-world/domains/{domain_id}`
- `GET /api/v1/global-world/ecosystems`

Adult-only taxonomy entries are excluded by default. The `include_adult` query parameter is a catalog filter only; it is NOT an identity or age-verification control. A production adult service must implement robust age assurance, access control, consent and performer-safety processes, privacy protections, moderation, and jurisdiction-specific legal review. Child protection and survivor support are kept in a separate safeguarding domain.

## Architecture boundaries

- Global World is the umbrella taxonomy and discovery index.
- Global Bada Business owns business sectors, business sizes, business modes and business providers.
- Global People, Work & Life owns people, education, jobs, careers, households and life situations.
- AI, APP, CLOUD, DATABASE and other provider ecosystems own their respective technical provider catalogs.
- Relationship & Intimacy and Adult Industry remain separately classified domains.
- A taxonomy entry does not mean that a provider, integration, service, job or real-world listing exists or is live.

## Coverage model

Domains are extensible and cross-classified by online/offline/hybrid delivery, organization size, work mode, life situation, age band, audience, geography and maturity (traditional/established/emerging/future). The catalog is not a literal exhaustive list of every activity or entity on Earth; it is a maintainable top-level classification that can grow through reviewed sector and subcategory records.
