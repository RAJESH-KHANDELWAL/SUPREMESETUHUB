# Freelancing & Gig Work

Independent category package: `freelancing_and_gig_work`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `freelance_marketplaces`
- `independent_contracting`
- `gig_platforms`
- `project_based_work`

## API

- `GET /industries/jobs-careers-employment/category-modules/freelancing-and-gig-work`
- `GET /industries/jobs-careers-employment/category-modules/freelancing-and-gig-work/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
