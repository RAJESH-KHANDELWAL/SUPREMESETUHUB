# Professional Fields & Occupation Families

This package adds a second classification axis to Work & Careers: **what kind of profession or work is performed**. The existing 24 Work & Careers categories remain the independent employment-context axis (employer sector, geography, work arrangement, schedule, seniority and workforce services).

## Design rules
- Professional field and subcategory packages are physically separated into folders.
- Each field has its own taxonomy, typed models, service layer, API router and documentation.
- Each subcategory has its own package folder, README and Python package initializer. Detailed role/specialization records are added under the owning field taxonomy; they are not duplicated across employment-context categories.
- The shared API Ecosystem registry exposes field and subcategory resources. A dedicated API is added only where a field has independent operations or data needs; taxonomy-only subcategories use the shared registry.
- A job can be classified by one or more professional fields and simultaneously by any applicable existing Work & Careers categories.
- This is a taxonomy, not a live vacancy feed, credential verification service, professional licensing authority or legal eligibility engine.

## Current field coverage
- `it_technology/` — IT & Digital Technology (8 subcategories)
- `banking_finance/` — Banking & Finance (8 subcategories)
- `healthcare_medical/` — Healthcare & Medical (8 subcategories)
- `education_training/` — Education & Training (7 subcategories)
- `engineering_construction/` — Engineering & Construction (8 subcategories)
- `sales_marketing/` — Sales & Marketing (7 subcategories)
- `legal_compliance/` — Legal & Compliance (5 subcategories)
- `agriculture_food/` — Agriculture & Food Systems (6 subcategories)
- `manufacturing_operations/` — Manufacturing & Operations (6 subcategories)
- `real_estate_facilities/` — Real Estate & Facilities (6 subcategories)
- `hospitality_tourism/` — Hospitality & Tourism (6 subcategories)
- `transport_logistics/` — Transport & Logistics (6 subcategories)

## API
- `GET /professional-fields`
- `GET /professional-fields/{field_id}`
- `GET /professional-fields/{field_id}/subcategories`
- `GET /professional-fields/{field_id}/subcategories/{subcategory_id}`
- `GET /professional-fields/integrity`

The registry uses stable IDs and reports `taxonomy_only`. It does not claim that any job opening, employer, qualification or professional licence has been verified.
