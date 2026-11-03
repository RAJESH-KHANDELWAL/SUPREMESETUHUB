# Human Resources & Payroll

Independent category package: `human_resources_and_payroll`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `hr_consulting`
- `payroll_services`
- `benefits_administration`
- `hr_technology`

## API

- `GET /industries/jobs-careers-employment/category-modules/human-resources-and-payroll`
- `GET /industries/jobs-careers-employment/category-modules/human-resources-and-payroll/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
