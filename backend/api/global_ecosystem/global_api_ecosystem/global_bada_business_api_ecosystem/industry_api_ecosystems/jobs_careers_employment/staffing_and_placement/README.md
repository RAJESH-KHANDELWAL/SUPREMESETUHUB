# Staffing & Placement

Independent category package: `staffing_and_placement`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `temporary_staffing`
- `permanent_placement`
- `contract_staffing`
- `recruitment_process_outsourcing`

## API

- `GET /industries/jobs-careers-employment/category-modules/staffing-and-placement`
- `GET /industries/jobs-careers-employment/category-modules/staffing-and-placement/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
