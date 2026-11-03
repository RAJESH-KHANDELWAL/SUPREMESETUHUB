# Employer Branding & Talent Marketing

Independent category package: `employer_branding`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `employer_value_proposition`
- `talent_campaigns`
- `candidate_experience`
- `recruitment_marketing`

## API

- `GET /industries/jobs-careers-employment/category-modules/employer-branding`
- `GET /industries/jobs-careers-employment/category-modules/employer-branding/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
