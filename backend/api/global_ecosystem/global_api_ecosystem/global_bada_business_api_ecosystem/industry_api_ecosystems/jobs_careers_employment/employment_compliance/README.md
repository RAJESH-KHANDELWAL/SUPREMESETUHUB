# Labour & Employment Compliance

Independent category package: `employment_compliance`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `employment_contracts`
- `workplace_policies`
- `labour_compliance_advisory`
- `workplace_safety_training`

## API

- `GET /industries/jobs-careers-employment/category-modules/employment-compliance`
- `GET /industries/jobs-careers-employment/category-modules/employment-compliance/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
