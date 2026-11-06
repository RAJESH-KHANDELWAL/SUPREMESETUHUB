# Aviation, Aerospace & Space Technology API Ecosystem

Stable package ID: `aviation_aerospace_space_technology`

India and global discovery taxonomy covering aviation operators and services, aircraft and aerospace manufacturing, drones, satellites, launch services and space research.

## Business-domain coverage

The ecosystem exposes **20 business domains** through the `/domains` API, mapped to 12 maintained API categories to avoid duplicate package structures.

1. Commercial Aviation
2. Airlines & Airline Operations
3. Airports & Airport Services
4. Aircraft Manufacturing
5. Aircraft Maintenance, Repair & Overhaul
6. Aircraft Parts & Components
7. Aviation Technology & Software
8. Air Cargo & Aviation Logistics
9. Private & Business Aviation
10. Helicopter Services
11. Drone & UAV Technology
12. Drone Services & Operations
13. Aerospace Manufacturing
14. Space Technology
15. Satellite Manufacturing
16. Satellite Communication
17. Space Launch Services
18. Space Research & Exploration
19. Aviation Training & Certification
20. Aviation Safety & Compliance

## API endpoints

- `GET /industries/aviation-aerospace-space-technology/status`
- `GET /industries/aviation-aerospace-space-technology/categories`
- `GET /industries/aviation-aerospace-space-technology/categories/{category_id}`
- `GET /industries/aviation-aerospace-space-technology/domains`
- `GET /industries/aviation-aerospace-space-technology/domains?q=...`
- `GET /industries/aviation-aerospace-space-technology/domains/{domain_id}`

## Regulatory and scope boundaries

- Taxonomy and discovery only: this package does not issue flight permissions, air operator certificates, airworthiness approvals, pilot credentials, drone permissions, launch licenses or spectrum authorizations.
- Training and certification entries are informational discovery only; regulated credentials must be issued by the competent authority or authorized training organization.
- Air cargo covers aviation-specific cargo handling and air-freight services. General freight, warehousing, customs and multimodal logistics remain in Transport, Logistics & Supply Chain.
- Space and satellite entries do not imply launch availability, orbital rights, spectrum rights or government affiliation.
- No live flight schedules, launch availability, operator licensing or certification records are included.

## Implementation status

`taxonomy_scaffold` — domain/category discovery endpoints only. Parent-router registration, provider integrations and integration tests remain separate production-readiness tasks.
