# Reskilling & Outplacement

Independent category package: `reskilling_and_outplacement`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `career_reskilling`
- `redeployment_support`
- `outplacement_services`
- `workforce_transition`

## API

- `GET /industries/jobs-careers-employment/category-modules/reskilling-and-outplacement`
- `GET /industries/jobs-careers-employment/category-modules/reskilling-and-outplacement/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
