# Agriculture, Food & Natural Resources API Ecosystem

Standalone ecosystem package **#02** under `global_api_ecosystem/`. This package is intentionally outside `global_bada_business_api_ecosystem/` and outside `industry_api_ecosystems/`.

## Purpose
A modular API taxonomy for agriculture, food systems, allied industries and natural resources across Bharat and global markets.

## Package structure
- `__init__.py` — package exports
- `subcategories.py` — canonical domain registry
- `domains_catalog.py` — domain descriptions and coverage vocabulary
- `models.py` — typed domain model
- `catalog.py` — catalog access and validation
- `service.py` — service layer
- `schemas.py` — API response/request schemas
- `routes.py` — FastAPI router
- Domain folders — independent domain packages with README, catalog and package initializer

## API
Router prefix: `/agriculture-food-natural-resources`
Endpoints: `GET /status`, `GET /domains`, `GET /domains/{domain_id}`

## Governance
- Use jurisdiction-specific compliance and licensing checks before enabling regulated workflows.
- Do not represent a listed provider, certification, licence or commodity as verified unless evidence and verification timestamps are stored.
- Preserve food safety, animal welfare, environmental safeguards, traceability and responsible sourcing.
- This taxonomy is not a substitute for professional agricultural, veterinary, food-safety, environmental or legal advice.

## Implementation status
Initial taxonomy and API scaffolding. Parent application router registration, automated tests, database persistence, provider verification and live integrations remain separate follow-up tasks.
