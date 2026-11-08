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


## Expanded India and global taxonomy

The catalog covers India/Bharat and global people, work and life domains, including education, careers, entrepreneurship, family, relationships, dating, digital communities, health education, civic services and local needs. Geographic scope is a classification facet, not a claim that every service is available in every country.

## Service capability tiers

The catalog includes the following service tiers: Normal, Standard, Advanced, Premium, Enterprise and Supreme. These are classification labels only; they do not imply that a tier has been implemented, priced or operationally approved.

## Adult-only classifications (18+)

Adult-only domains are separately classified and excluded from the default domain listing. They include lawful adult media and pornography platforms, adult creator businesses, production and studio operations, distribution and licensing, subscriptions, live streaming, performer rights and consent, age assurance, moderation, privacy and compliance, and consensual adult-couple education.

Adult-only classifications are for lawful services involving verified adults who meet the applicable local age threshold. Require freely given and ongoing consent, performer rights, privacy safeguards, moderation, reporting and jurisdiction-specific legal review. Do not support minors, coercion, trafficking, exploitation, non-consensual intimate imagery or unlawful content. These classifications do not authorize or facilitate illegal sexual services.

## Scope and implementation status

This remains a read-only taxonomy catalog. It does not itself provide dating, adult media, employment, booking, counselling, payments, age verification or live integrations. New domain entries and service-tier facets are classifications only; production capabilities require separate implementation, testing, provider approval where applicable and legal review.
