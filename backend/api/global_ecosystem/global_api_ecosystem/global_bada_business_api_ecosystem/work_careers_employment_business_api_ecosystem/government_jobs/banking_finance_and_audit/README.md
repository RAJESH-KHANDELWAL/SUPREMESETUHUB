# Banking Finance And Audit

## Scope
Banking and finance posts: public bank officers/clerks, probationary officers, specialist officers, accountants, auditors, tax assistants, treasury officers, finance officers and pension/accounts staff. Separate bank recruitment from government accounts/audit.

## Required child folders
Create separate child folders for each distinct post family, cadre/grade, discipline or operational function. Do not use a generic `tracks/` layer and do not copy Professional Fields taxonomies.

## Required files for each implemented job family
- `README.md` — role scope, duties, eligibility dimensions and classification boundaries
- `__init__.py` — package definition
- `categories.py` — job-specific categories and identifiers
- `models.py` — domain entities and relationships
- `schemas.py` — input/output contracts
- `validators.py` — domain validation
- `services.py` — business rules and operations
- `routes.py` and `api_ecosystem.py` — API integration
- `tests/` — focused tests for the job family

Keep post title, recruiting authority, cadre, grade/pay level, discipline, work location, eligibility, notification and appointment as separate data concerns. Official recruitment notifications remain the source of truth.
