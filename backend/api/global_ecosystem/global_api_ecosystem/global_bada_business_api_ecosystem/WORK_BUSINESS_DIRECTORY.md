# India + Global Work & Business Directory

This document defines the direct-root domain package plan for this existing directory.

## Dedicated Global Services and Work & Business API facades

Two dedicated API packages are mounted under the existing Global Bada Business router:

- `global_services_api_ecosystem/` — service-category API facade. It reuses the canonical `services_platforms_integrations_business_api_ecosystem/` catalogue; it does not duplicate category records or claim live provider connections.
- `global_work_business_api_ecosystem/` — aggregate Work & Business discovery facade. It references the canonical A–Z work/business taxonomy, Freelance/Gig specialization registry and Jobs/Careers service.

Routes are mounted beneath `/api/v1/global-ecosystem/business`:
- `/services/status`, `/services/categories`, `/services/categories/search`, `/services/categories/{category_id}`
- `/work-business-directory/status`, `/work-business-directory/sectors`, `/work-business-directory/sectors/search`, `/work-business-directory/sectors/{sector_id}`, `/work-business-directory/facets`, `/work-business-directory/freelance-specializations`, `/work-business-directory/jobs-careers/status`

The facades provide classification and discovery only. They do not represent live service availability, verified employers/clients, vacancies, payment execution or placement outcomes.

## Existing components preserved
- `global_world_catalog.py`: umbrella Global World A–Z domain snapshot; not the detailed occupation or vacancy catalogue.
- `global_world_business_map.py`: crosswalk from Global World domains to business-facing categories and owning ecosystems.
- `business_catalog.py`: curated business-provider category catalogue.
- `sectors/`: individual business-sector packages owned by the business-sector layer.
- `universal_work_business_taxonomy_api_ecosystem/`: separate 26-sector work/business taxonomy with work-model, audience and delivery facets.
- `routes.py`, `schemas.py`, `service.py`: parent API and service layer.
- `industry_api_ecosystems/`: industry-specific registries.
- `integrations/`, `services/`, `tools/`: adapter and service boundaries.
- Existing `*_business_api_ecosystem/` folders: provider/vendor ecosystems.

## Standardized domain API ecosystem folders (direct children)
1. `global_freelancer_gig_independent_work_business_api_ecosystem/` — global freelancing, gig work, independent services and contracting.
   - `jobs_careers_employment_api_ecosystem/` — Jobs, Careers & Employment, including employment contexts, professional fields, recruitment, staffing and job-family specializations.
2. `network_marketing_direct_selling_business_api_ecosystem/` — Bharat + Global network marketing, MLM and direct-selling businesses only.
3. `global_education_learning_training_api_ecosystem/students_education_skills_business_api_ecosystem/` — school, higher/vocational education, courses, scholarships, internships and skills.
4. `business_companies_trade_business_api_ecosystem/` — entity forms, enterprise sizes, local businesses, wholesale, retail, manufacturing and trade.
5. `global_entrepreneurs_entrepreneurship_msme_sme_startups_solo_women_digital_ai_technology_innovation_business_creation_development_growth_api_ecosystem/` — entrepreneurs, MSME, SME, startups, solo and women entrepreneurship, digital, AI, technology, innovation, business creation and growth.
6. `home_homemaker_care_economy_business_api_ecosystem/` — home businesses, homemaker livelihoods, caregiving and domestic services.
7. `industries_professional_services_business_api_ecosystem/` — cross-sector industries and professional services; detailed sector registries remain in existing modules.
8. `family_relationships_community_business_api_ecosystem/` — family/community education and provider-side support categories; private personal records remain elsewhere.
9. `adult_18_plus_lawful_industry_business_api_ecosystem/` — restricted adult taxonomy, excluded from default discovery; legal review, age assurance, consent, privacy and safeguarding are prerequisites.
10. `services_platforms_integrations_business_api_ecosystem/` — cloud, domains, websites, payments, CRM, accounting, communications, APIs and integrations.
11. `industry_api_ecosystems/finance_banking_insurance/` — the single canonical Finance, Banking & Insurance API Ecosystem; the former finance-support package is a compatibility facade.
12. `industry_api_ecosystems/government_public_services_social_impact/` — the single canonical Government, Public Services & Social Impact API Ecosystem; the former public/nonprofit package is a compatibility facade.

## Standard files inside each domain folder
- `__init__.py`: stable domain ID, display name, default discovery flags and canonical subcategory IDs.
- `README.md`: scope, coverage, data boundaries, compliance and maintenance notes.
- `subcategories.py`: canonical `snake_case` subcategory IDs and display-label helper.
- `models.py`: typed `CategoryRecord` data model.
- `catalog.py`: structured category records plus list, detail, search and metadata functions.
- `service.py`: domain-level service facade for listing, detail, search and status.

The 10 canonical standardized core-domain API ecosystem folders follow these six-file conventions. Finance and Government/Public Services are maintained as industry API ecosystems, with compatibility facades retained for older imports. The central API layer remains in the parent directory; individual domain API ecosystem packages provide their own catalogue/service layers rather than duplicating route registration.

## Independent Work & Jobs specialization architecture

### Work, Jobs & Careers
- The domain contains 24 independent employment-context category packages.
- Each category owns its own direct-child job-family/specialization folders; the folders are not nested under a redundant `tracks/` directory.
- Each specialization folder owns its README, stable package identity, models, schemas, service adapter, routes, validators and tests.
- The owning employment category's `categories.py` is the canonical source for the job-family record; the child specialization's `categories.py` binds its `TRACK_ID` and `CATEGORY_ID` to that record. This keeps one definition per job family while preserving a separate folder and API resource for each specialization.
- The parent category catalogue discovers every direct-child specialization package dynamically, including packages not present in older static category lists.
- All individual job-family routers are mounted through `global_freelancer_gig_independent_work_business_api_ecosystem/jobs_careers_employment_api_ecosystem/specialization_routes.py` at their canonical `/work-careers/{category_id}/{job_family_id}` paths. Category-level catalogue endpoints remain available for listing, search and detail.

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
- `domain_registry.py` is the central runtime registry assembled from canonical core and industry domain packages.
- `service.py` exposes domain list, detail, search and integrity operations.
- `routes.py` exposes `GET /api/v1/global-ecosystem/business/domains`, `GET /domains/search?q=...`, `GET /domains/{domain_id}` and `GET /domains/integrity` under the existing router prefix.
- The ecosystem status response reports domain package count, subcategory count and the `taxonomy_only` registry status.
- Every domain package provides `subcategories.py` as a stable subcategory accessor.
- `tests/test_global_business_domain_registry.py` validates package counts, unique IDs, adult default exclusion, search, status metrics and route registration.
- `tests/test_domain_package_layers.py` imports all 12 packages and validates their model, catalogue and service layers plus adult-category exclusion.

## Current non-goals
No job board ingestion, employer identity verification, business registration lookup, payment execution, user account storage, live provider API credentials or production integrations are implemented by this taxonomy layer. These require separate source integrations, security design, vendor authorization, legal review and operational monitoring.


## Verified detailed work and occupation ownership

The canonical Work & Careers package separates these dimensions instead of placing every kind of work into one mixed catalogue:

- **24 employment-context categories** are defined in `global_freelancer_gig_independent_work_business_api_ecosystem/jobs_careers_employment_api_ecosystem/categories.py`.
- **234 direct-child job-family/specialization folders** exist under those 24 category packages. Each specialization belongs to its parent category.
- **12 professional-field packages and 81 professional subcategories** are maintained separately under `global_freelancer_gig_independent_work_business_api_ecosystem/jobs_careers_employment_api_ecosystem/professional_fields/`. This is the occupation/professional-field axis, not a 25th employment category.
- **25 freelance/gig specialization packages** exist under `global_freelancer_gig_independent_work_business_api_ecosystem/`. Each specialization owns its own work-type catalogue.

These counts were derived from the repository tree and the current category/field registries. They are structural counts, not counts of live jobs, active gigs or verified providers.

## Single canonical repository location

Use only:

`backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`

The alternate path `backend/api/global_api_ecosystem/global_bada_business_api_ecosystem/` is deprecated and contains only a README pointer. Its duplicate documentation-only career stubs were removed after confirming that the maintained career-change specialization packages already exist in the canonical Work & Careers package.

Do not create another Work & Careers, Freelance, business catalogue or industry catalogue at the deprecated path. Add new records and specializations to their owning canonical package, update its registry and tests, and use crosswalks for relationships between classification layers.


## Test contract for dynamically discovered specializations

Work & Careers tests validate the live package registry rather than hard-coded folder totals. Each specialization test resolves its stable `TRACK_ID` and `CATEGORY_ID` through the canonical category record and verifies the API resource. Category integrity tests compare the reported count with the discovered catalogue, validate unique IDs and required labels, and exercise lookup/search. Adding a specialization therefore does not require editing an unrelated fixed-count assertion.


The specialization test suite supports both established package contracts: (1) independent job-family packages exposing `JOB_FAMILY_ID` and `get_job_family()`, and (2) track adapters exposing `TRACK_ID`, `get_track_definition()` and `get_track_api_resource()`. Tests verify the contract actually implemented by each folder rather than assuming one interface for every historical package.


## Consolidated technology and payment ecosystems

- `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/` is the single top-level home for digital infrastructure, telecommunications, IT, software, AI, cloud and the related Apple, AWS, Google, IBM, Microsoft and Oracle provider folders.
- `global_finance_banking_insurance_api_ecosystem/global_payment_business_api_ecosystem/` is the single home for payment-platform folders, including PayPal, Stripe, Epoch, Paxum, Segpay, Verotel and CCBill.
- The old separate root-level technology, employment and payment entry folders have been consolidated. Canonical detailed industry implementations under `industry_api_ecosystems/` remain the implementation owner where documented; the new global folders are the consolidated business-facing structure.
