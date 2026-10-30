# GLOBAL BADA BUSINESS API ECOSYSTEM

Global Bada Business is the business-sector and business-provider ecosystem for SUPREMESETUHUB.

## Relationship with Global World A-Z

Global World is the umbrella discovery taxonomy. This package now includes a **business-facing crosswalk for all 32 Global World domains** through `global_world_business_map.py`.

The crosswalk distinguishes:
- **Direct business domains**: business sectors and business entities owned by Global Bada Business.
- **Provider-side domains**: businesses that serve education, employment, family, healthcare, public-service or similar areas can be discoverable here.
- **Cross-reference-only domains**: personal records and interactions remain in their dedicated ecosystems and are linked by stable IDs or authorized APIs.
- **Restricted domains**: adult-only references remain excluded by default and require separate age assurance, consent, privacy, moderation and jurisdiction-specific controls.

This is deliberate integration, not duplication. People, students, job seekers, employee profiles, households, personal relationships, and safeguarding case records are not redefined as businesses.

## Business taxonomy

`business_catalog.py` remains the source of business categories and subcategories. It covers online, offline and hybrid businesses. Provider directories and integrations remain in their dedicated folders.

## Global World crosswalk

- `global_world_business_map.py` maps all 32 umbrella domains to their business-facing category IDs and owning ecosystem.
- The map is a classification and routing index, not a live registry of every company, person, job, service or location.
- Related category IDs must refer to entries in `business_catalog.py`.
- New World domains should be added to the crosswalk when Global World expands.

## API endpoints

Existing:
- `GET /api/v1/global-ecosystem/business/status`
- `GET /api/v1/global-ecosystem/business/modules`
- `GET /api/v1/global-ecosystem/business/modules/{module_id}`
- `GET /api/v1/global-ecosystem/business/catalog`
- `GET /api/v1/global-ecosystem/business/catalog/search?q=...`
- `GET /api/v1/global-ecosystem/business/catalog/{category_id}`

New:
- `GET /api/v1/global-ecosystem/business/world-map`
- `GET /api/v1/global-ecosystem/business/world-map?include_adult=true`
- `GET /api/v1/global-ecosystem/business/world-map/{domain_id}`

The `include_adult` parameter is a catalog filter only. It is not age verification or authorization.

## Architecture rule

Business entities and providers belong here. Personal identities, life situations, student records, job-seeker profiles, employment applications, relationship records and safeguarding records remain in their owning ecosystems. Connect them through stable IDs and permission-checked APIs; do not copy their source records into this business catalog.


## Full Global World A-Z catalogue embedded here

The earlier `global_world_business_map.py` is a routing crosswalk. The complete 32-domain taxonomy snapshot is now separately stored in `global_world_catalog.py`, including each domain's subgroup list, delivery modes, owning ecosystem, business-facing scope and linked business category IDs where applicable.

New full-catalogue endpoints:
- `GET /api/v1/global-ecosystem/business/world-catalog`
- `GET /api/v1/global-ecosystem/business/world-catalog?include_adult=true`
- `GET /api/v1/global-ecosystem/business/world-catalog/search?q=...`
- `GET /api/v1/global-ecosystem/business/world-catalog/{domain_id}`

The full catalogue is a taxonomy snapshot, not a live database. Personal records, student/job-seeker profiles, household records and relationship interactions are not copied into business entities; only business providers and relevant business categories are discoverable here.
