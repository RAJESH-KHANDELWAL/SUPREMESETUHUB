# Global Water Resources & Marine Industries Business API Ecosystem

This directory owns the complete Water Resources & Marine Industries API implementation.

## Package structure
- `catalog.py`: 12-category industry taxonomy
- `schemas.py`: response schemas
- `service.py`: category lookup, filtering and status service
- `routes.py`: FastAPI endpoints
- `tests/`: service regression tests

Stable industry ID: `water_resources_marine_industries`.

## API surface
The parent ecosystem router mounts this package at the established industry path:
- `GET /industries/water-resources-marine-industries/status`
- `GET /industries/water-resources-marine-industries/categories`
- `GET /industries/water-resources-marine-industries/categories/{category_id}`

The categories endpoint accepts optional `q` search.

## Taxonomy
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

## Status and data limitations
Status: `taxonomy_scaffold`. Coverage labels: India and global. Channels: online, offline and hybrid.

This is a taxonomy/API scaffold, not a live operational directory. It does not verify water quality, suppliers, treatment-plant operations, marine operators, ports, fishing licences, environmental permits, certifications or regulatory compliance. Those require authoritative sources, timestamps, provenance and verification workflows.

## Tests
Run from the repository root:
```bash
python -m unittest backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_water_resources_marine_industries_industrial_business_api_ecosystem.tests.test_service
```
