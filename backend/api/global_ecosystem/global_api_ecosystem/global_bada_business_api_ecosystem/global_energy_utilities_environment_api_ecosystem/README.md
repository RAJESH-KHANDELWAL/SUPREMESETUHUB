# Energy, Utilities & Environment API Ecosystem

**Canonical package location:** `global_bada_business_api_ecosystem/global_energy_utilities_environment_api_ecosystem/` (maintained directly at the Bada Business root, outside `industry_api_ecosystems/`).

The consolidated canonical package contains the former root-level Energy, Utilities & Environment implementation and its API-ecosystem entry-point behavior. This package provides a 12-category taxonomy and 20 business domains spanning energy generation, grids, storage, water utilities, waste, environmental services and climate/sustainability.

## Package structure
- `categories/`: category reference notes
- `jobs/`: sector-specific roles and vacancies taxonomy
- `business/`: energy companies, utility providers and environmental service business taxonomy
- `india/` and `global/`: jurisdictional reference areas
- `coaches/`, `consultants/`, `advisors/`: separate professional directory areas
- `access_tiers/`: access classifications; adult 18+ is not an energy eligibility category
- `catalog.py`, `service.py`, `schemas.py`, `routes.py`: taxonomy and API implementation

## API endpoints
- GET `/industries/energy-utilities-environment/status`
- GET `/industries/energy-utilities-environment/categories`
- GET `/industries/energy-utilities-environment/categories?q=...`
- GET `/industries/energy-utilities-environment/categories/{category_id}`
- GET `/industries/energy-utilities-environment/domains`
- GET `/industries/energy-utilities-environment/domains?q=...&category_id=...`
- GET `/industries/energy-utilities-environment/domains/{domain_id}`

## Business-domain coverage
Solar, wind, hydropower, biomass/bioenergy, oil and gas, nuclear energy, electricity generation, transmission and distribution, smart grids, battery storage, green hydrogen, water supply, water treatment/desalination, wastewater, waste/recycling, environmental consulting, climate sustainability, carbon markets/ESG, clean technology/efficiency, and utility infrastructure/maintenance.

## Scope and limitations
This is a taxonomy/API scaffold, not live utility coverage, verified company listings, job vacancies, provider integration, regulatory approval or professional certification. Verify sources, licenses, safety requirements and jurisdiction-specific rules before publishing records. Regulated activities (including nuclear, power operations, water supply and hazardous-waste handling) require applicable jurisdictional approvals.
