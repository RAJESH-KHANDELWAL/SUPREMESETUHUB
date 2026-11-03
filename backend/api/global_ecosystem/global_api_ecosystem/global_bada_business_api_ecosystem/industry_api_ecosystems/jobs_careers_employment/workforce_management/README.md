# Workforce Management

Independent category package: `workforce_management`.

## Ownership

This package owns its category taxonomy, read-only service boundary, API routes, and package tests. Its canonical data is maintained in `catalog.py`; it is aggregated by the Jobs, Careers & Employment domain without copying the category definition into a shared list.

## Subcategories

- `workforce_planning`
- `shift_scheduling`
- `attendance_management`
- `field_workforce`

## API

- `GET /industries/jobs-careers-employment/category-modules/workforce-management`
- `GET /industries/jobs-careers-employment/category-modules/workforce-management/status`

## Scope

Taxonomy/discovery scaffold only. This package does not claim live vacancies, verified providers, payment processing, or legal/regulatory certification.
