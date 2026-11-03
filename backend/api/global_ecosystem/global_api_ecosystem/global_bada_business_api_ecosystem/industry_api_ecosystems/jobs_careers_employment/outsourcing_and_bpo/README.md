# Outsourcing & Business Process Services

Independent category package: `outsourcing_and_bpo`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `business_process_outsourcing`
- `customer_support_operations`
- `knowledge_process_outsourcing`
- `staff_augmentation`

## API

- `GET /industries/jobs-careers-employment/category-modules/outsourcing-and-bpo`
- `GET /industries/jobs-careers-employment/category-modules/outsourcing-and-bpo/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
