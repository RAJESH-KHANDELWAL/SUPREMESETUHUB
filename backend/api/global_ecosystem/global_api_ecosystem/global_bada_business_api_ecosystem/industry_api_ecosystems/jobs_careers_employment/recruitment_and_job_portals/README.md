# Recruitment & Job Portals

Independent category package: `recruitment_and_job_portals`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `job_boards`
- `employer_job_sites`
- `executive_vacancies`
- `campus_recruitment`

## API

- `GET /industries/jobs-careers-employment/category-modules/recruitment-and-job-portals`
- `GET /industries/jobs-careers-employment/category-modules/recruitment-and-job-portals/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
