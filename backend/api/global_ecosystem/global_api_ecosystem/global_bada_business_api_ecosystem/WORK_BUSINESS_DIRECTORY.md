# India + Global Work & Business Directory

This document defines the direct-root domain package plan for this existing directory.

## Existing components preserved
- `business_catalog.py`: business category catalogue.
- `global_world_catalog.py`: master Global World and universal work/business taxonomy.
- `global_world_business_map.py`: cross-domain mapping.
- `routes.py`, `schemas.py`, `service.py`: API and service layer.
- `sectors/`: sector taxonomy.
- `industry_api_ecosystems/`: industry-specific registries.
- `integrations/`, `services/`, `tools/`: adapter and service boundaries.
- Existing `*_business_api_ecosystem/` folders: provider/vendor ecosystems.

## Standardized domain API ecosystem folders (direct children)
1. `work_careers_employment_business_api_ecosystem/` — jobs, employment types, career guidance, recruitment and staffing.
2. `freelance_gig_independent_work_business_api_ecosystem/` — freelance skills, gigs, contracts and independent services.
3. `students_education_skills_business_api_ecosystem/` — school, higher/vocational education, courses, scholarships, internships and skills.
4. `business_companies_trade_business_api_ecosystem/` — entity forms, enterprise sizes, local businesses, wholesale, retail, manufacturing and trade.
5. `entrepreneurship_startups_business_api_ecosystem/` — business ideas, validation, startup formation, incubators, funding and scaling.
6. `home_homemaker_care_economy_business_api_ecosystem/` — home businesses, homemaker livelihoods, caregiving and domestic services.
7. `industries_professional_services_business_api_ecosystem/` — cross-sector industries and professional services; detailed sector registries remain in existing modules.
8. `family_relationships_community_business_api_ecosystem/` — family/community education and provider-side support categories; private personal records remain elsewhere.
9. `adult_18_plus_lawful_industry_business_api_ecosystem/` — restricted adult taxonomy, excluded from default discovery; legal review, age assurance, consent, privacy and safeguarding are prerequisites.
10. `services_platforms_integrations_business_api_ecosystem/` — cloud, domains, websites, payments, CRM, accounting, communications, APIs and integrations.
11. `investment_finance_support_business_api_ecosystem/` — finance education, banking, insurance, tax, grants, MSME and export support.
12. `public_nonprofit_social_impact_business_api_ecosystem/` — government/public services, nonprofits, charities and community development.

## Standard files inside each domain folder
- `__init__.py`: stable domain ID, display name, default discovery flags and canonical subcategory IDs.
- `README.md`: scope, coverage, data boundaries, compliance and maintenance notes.
- `subcategories.py`: canonical `snake_case` subcategory IDs and display-label helper.
- `models.py`: typed `CategoryRecord` data model.
- `catalog.py`: structured category records plus list, detail, search and metadata functions.
- `service.py`: domain-level service facade for listing, detail, search and status.

All 12 standardized domain API ecosystem folders now contain these six files. The central API layer remains in the parent directory; individual domain API ecosystem packages provide their own catalogue/service layers rather than duplicating route registration.

## Architecture rules
These are taxonomy packages, not live listings. Taxonomy membership does not verify a business, employer, job, professional licence, vendor or API connection. India + Global are intended coverage scopes, not a claim of exhaustive country coverage. Do not store personal or sensitive records in taxonomy files. Keep domain IDs synchronized with `global_world_catalog.py`, validate crosswalks and duplicate IDs, add tests, source provenance, jurisdiction and freshness metadata, moderation, authentication, authorization and audit logging before production. Do not merge this branch without explicit approval.

## Functional registry and API surface
- `domain_registry.py` is the central runtime registry assembled from the 12 domain packages.
- `service.py` exposes domain list, detail, search and integrity operations.
- `routes.py` exposes `GET /api/v1/global-ecosystem/business/domains`, `GET /domains/search?q=...`, `GET /domains/{domain_id}` and `GET /domains/integrity` under the existing router prefix.
- The ecosystem status response reports domain package count, subcategory count and the `taxonomy_only` registry status.
- Every domain package provides `subcategories.py` as a stable subcategory accessor.
- `tests/test_global_business_domain_registry.py` validates package counts, unique IDs, adult default exclusion, search, status metrics and route registration.
- `tests/test_domain_package_layers.py` imports all 12 packages and validates their model, catalogue and service layers plus adult-category exclusion.

## Current non-goals
No job board ingestion, employer identity verification, business registration lookup, payment execution, user account storage, live provider API credentials or production integrations are implemented by this taxonomy layer. These require separate source integrations, security design, vendor authorization, legal review and operational monitoring.
