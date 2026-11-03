# Executive Search & Leadership Hiring

Independent category package: `executive_search`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `c_suite_search`
- `board_search`
- `senior_management_hiring`
- `leadership_assessment`

## API

- `GET /industries/jobs-careers-employment/category-modules/executive-search`
- `GET /industries/jobs-careers-employment/category-modules/executive-search/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
