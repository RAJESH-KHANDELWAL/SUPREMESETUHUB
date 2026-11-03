# Resume, Interview & Job Readiness

Independent category package: `resume_and_interview_services`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `resume_writing`
- `profile_optimisation`
- `interview_preparation`
- `job_search_support`

## API

- `GET /industries/jobs-careers-employment/category-modules/resume-and-interview-services`
- `GET /industries/jobs-careers-employment/category-modules/resume-and-interview-services/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
