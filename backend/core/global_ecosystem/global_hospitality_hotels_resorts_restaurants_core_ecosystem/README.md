# Global Hospitality Hotels Resorts Restaurants Core Ecosystem

This is the canonical core layer for hospitality domain taxonomy, geographic hierarchy, identity, discovery contracts, and shared reference data.

## Coverage model
- Global: countries, first-level administrative divisions, districts/counties, cities, towns, villages, localities, streets and geospatial identifiers.
- Bharat: all States and Union Territories, districts, sub-districts/tehsils/blocks, cities, towns, gram panchayats, villages, wards, localities and streets.
- Hospitality entities: hotels, resorts, restaurants, cafes, dhabas, homestays, hostels, serviced apartments, banquet venues, convention facilities and related lodging/food-service categories.
- Shared concepts: ownership, property identity, classification, amenities, accessibility, safety, licensing references, languages, currencies, opening periods and source provenance.

## Directory responsibilities
- `categories/`: canonical hospitality category taxonomy.
- `global/`: global geographic and market reference model.
- `india/`: Bharat-specific administrative hierarchy and data contracts.
- `business/`: hospitality entity and property-domain models.
- `api_core_ecosystem/`: API contracts only.
- `access_tiers/`, `advisors/`, `coaches/`, `consultants/`, `jobs/`: existing focused modules; preserve their ownership.
- `tests/`: automated tests (use this exact directory name).

## Data integrity
Do not fabricate individual hotels, restaurants, street records, operating status, ratings, phone numbers or addresses. Geographic coverage is hierarchical and expandable; populate actual records only from authoritative, licensed or verified sources. Keep source, retrieval date, language, stable IDs and verification status with imported records.

The service/work/business implementation belongs in the separate Global Bada Business Core Ecosystem folder, not here.
