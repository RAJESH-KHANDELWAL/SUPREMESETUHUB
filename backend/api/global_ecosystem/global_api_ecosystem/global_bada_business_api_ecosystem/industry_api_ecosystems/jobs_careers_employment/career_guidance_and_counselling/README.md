# Career Guidance & Counselling

Independent category package: `career_guidance_and_counselling`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `career_assessment`
- `career_coaching`
- `career_transition`
- `workplace_guidance`

## API

- `GET /industries/jobs-careers-employment/category-modules/career-guidance-and-counselling`
- `GET /industries/jobs-careers-employment/category-modules/career-guidance-and-counselling/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
