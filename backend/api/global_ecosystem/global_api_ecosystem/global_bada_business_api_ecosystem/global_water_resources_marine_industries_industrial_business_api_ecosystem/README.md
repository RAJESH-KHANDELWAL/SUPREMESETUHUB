# Global Water Resources & Marine Industries Business API Ecosystem

This package is the Global Bada Business entry point for the Water Resources & Marine Industries domain.

## Package ownership

- Global entry point: `global_water_resources_marine_industries_industrial_business_api_ecosystem/`
- Canonical industry implementation: `industry_api_ecosystems/water_resources_marine_industries/`
- Stable industry ID: `water_resources_marine_industries`

The global package re-exports the canonical implementation. Keep the catalogue and API logic in one place; do not create a second copy of the taxonomy.

## Included API surface

The industry router exposes:

- `GET /industries/water-resources-marine-industries/status`
- `GET /industries/water-resources-marine-industries/categories`
- `GET /industries/water-resources-marine-industries/categories/{category_id}`

The categories endpoint supports an optional `q` search parameter.

## Current taxonomy coverage

The catalogue currently has 12 top-level areas:

1. Water Resources Management
2. Water Supply Services
3. Water Treatment
4. Wastewater & Sanitation
5. Irrigation & Agricultural Water
6. Water Technology & Monitoring
7. Marine Transport & Ports
8. Fisheries & Aquaculture
9. Marine Services
10. Coastal & Ocean Management
11. Marine Conservation
12. Blue Economy & Offshore Industries

## Implementation status and limits

Status: `taxonomy_scaffold`.

Coverage labels: India and global. Channels: online, offline and hybrid.

This is a structured taxonomy/API scaffold, not a live operational directory. It does not verify water quality, water suppliers, treatment-plant operations, marine operators, ports, fishing licences, environmental permits, certifications, or regulatory compliance. Such records require authoritative sources, jurisdiction, timestamps, provenance and verification workflows before publication.

## Tests

Run the package service tests from the repository's configured Python test environment:

```bash
python -m unittest backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.industry_api_ecosystems.water_resources_marine_industries.tests.test_service
```
