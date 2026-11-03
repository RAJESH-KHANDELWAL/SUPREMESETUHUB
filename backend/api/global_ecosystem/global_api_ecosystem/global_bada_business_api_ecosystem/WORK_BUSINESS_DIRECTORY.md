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

## Independent Work & Jobs specialization architecture

### Work, Jobs & Careers
- The domain contains 24 independent employment-context category packages.
- Each category owns its own direct-child job-family/specialization folders; the folders are not nested under a redundant `tracks/` directory.
- Each specialization folder owns its README, category definition, models, schemas, services, routes, validators and tests. Its `categories.py` is the source of truth for that job family.
- The parent category catalogue discovers every direct-child specialization package dynamically, including packages not present in older static category lists.
- All individual job-family routers are mounted through `work_careers_employment_business_api_ecosystem/specialization_routes.py` at their canonical `/work-careers/{category_id}/{job_family_id}` paths. Category-level catalogue endpoints remain available for listing, search and detail.

### Freelancing, Gig & Independent Work
- The domain contains 25 direct-child specialization packages, one for each stable subcategory ID.
- Every specialization owns a README, independent work-type catalogue, typed model, catalogue functions, service facade, response schemas, validators, routes and tests.
- Each specialization's `work_types.py` is the only canonical owner of its individual work/gig types. The domain root remains the stable index and discovery facade.
- `specializations.py` mounts all 25 independent specialization routers. The Global World crosswalk imports the canonical ID tuple instead of maintaining a second hard-coded freelance list.

These are taxonomy/API contracts, not live job or gig listings. A registered folder or route does not imply an active vacancy, verified client, payment, licence, or successful placement. Where concepts overlap across employment, occupation and freelance-service taxonomies, use explicit crosswalks and preserve the classification axis rather than duplicating the canonical definition.

## Architecture rules
These are taxonomy packages, not live listings. Taxonomy membership does not verify a business, employer, job, professional licence, vendor or API connection. India + Global are intended coverage scopes, not a claim of exhaustive country coverage. Do not store personal or sensitive records in taxonomy files. Keep domain IDs synchronized with `global_world_catalog.py`, validate crosswalks and duplicate IDs, add tests, source provenance, jurisdiction and freshness metadata, moderation, authentication, authorization and audit logging before production. Do not merge this branch without explicit approval.

## Independent freelance specialization packages

The Freelancing, Gig & Independent Work domain has 25 direct-child specialization packages. Each specialization owns its own `README.md`, `work_types.py`, `models.py`, `catalog.py`, `services.py`, `schemas.py`, `validators.py`, `routes.py` and tests. The work-type catalogue is owned by the specialization folder, not duplicated in the domain root. The aggregate `specializations.py` mounts these independent routers; the domain root remains the stable index and discovery facade. The Global World crosswalk reads the canonical specialization IDs from the domain package rather than maintaining a second hard-coded list.

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
