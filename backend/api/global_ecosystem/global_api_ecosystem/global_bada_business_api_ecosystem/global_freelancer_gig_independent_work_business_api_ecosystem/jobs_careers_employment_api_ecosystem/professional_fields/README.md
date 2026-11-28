# Professional Fields & Occupation Families

This package adds a second classification axis to Work & Careers: **what kind of profession or work is performed**. The existing 24 Work & Careers categories remain the independent employment-context axis (employer sector, geography, work arrangement, schedule, seniority and workforce services).

## Package architecture
Each of the 12 professional fields is a complete field-level API Ecosystem package. Each field owns:
- `categories.py` — canonical subcategory definitions and stable IDs
- `models.py` — typed occupation/subcategory records
- `schemas.py` — stable response schema
- `services.py` — list, lookup and search operations
- `validators.py` — structural integrity checks
- `routes.py` — field-specific status, occupation list/detail and search endpoints
- `tests/` — field taxonomy integrity and lookup tests
- One child folder per subcategory, with its own `README.md` and `__init__.py`

The shared router mounts the field-owned routers below `/professional-fields/{field_id}`. The registry endpoints remain available for cross-field discovery. Subcategories are taxonomy resources and use the shared registry; they do not receive duplicate independent routers unless separate operations or data ownership become necessary.

## Classification rules
- Professional field describes the occupation or work performed.
- Existing 24 Work & Careers categories describe employment context: employer sector, geography, work arrangement, schedule, seniority and workforce services.
- A role may belong to one professional field and simultaneously be government, private, corporate, remote, hybrid, full-time, contract or international where applicable.
- Do not duplicate occupations to represent employment context.

## Field coverage (12 fields, 81 subcategories)
- `it_technology/` — IT & Digital Technology (8)
- `banking_finance/` — Banking & Finance (8)
- `healthcare_medical/` — Healthcare & Medical (8)
- `education_training/` — Education & Training (7)
- `engineering_construction/` — Engineering & Construction (8)
- `sales_marketing/` — Sales & Marketing (7)
- `legal_compliance/` — Legal & Compliance (5)
- `agriculture_food/` — Agriculture & Food Systems (6)
- `manufacturing_operations/` — Manufacturing & Operations (6)
- `real_estate_facilities/` — Real Estate & Facilities (6)
- `hospitality_tourism/` — Hospitality & Tourism (6)
- `transport_logistics/` — Transport & Logistics (6)

## Shared registry endpoints
- `GET /professional-fields`
- `GET /professional-fields/{field_id}`
- `GET /professional-fields/{field_id}/subcategories`
- `GET /professional-fields/{field_id}/subcategories/{subcategory_id}`
- `GET /professional-fields/integrity`

## Field-owned endpoints
Each field exposes `GET /professional-fields/{field_id}/status`, `/occupations`, `/occupations/{occupation_id}` and `/search?q=...`.

All resources report `taxonomy_only`. They do not verify vacancies, employers, recruiters, professional credentials, licences or legal eligibility.
