# Universal Work & Business Taxonomy API Ecosystem

**Parent:** Global Bada Business API Ecosystem  
**Coverage intent:** India + Global  
**Status:** Versioned discovery taxonomy; not a verified business directory, job board, licence register or legal opinion.

## Scope
This package owns a 26-sector India + Global work/business taxonomy and shared discovery facets: work models, delivery modes and audience groups. It is not the umbrella Global World catalogue. The umbrella domain snapshot remains in the parent `global_world_catalog.py`; `global_world_business_map.py` is its business-facing crosswalk. This package is not the storage location for every detailed job, occupation, business, service or freelance work type.

## Canonical ownership — one source per classification layer

Keep detailed records in the package that owns that concept. Do not copy the same catalogue into this A–Z package.

| Classification layer | Canonical owner | Current structure checked in repository |
|---|---|---|
| Global World umbrella domains | Parent `global_world_catalog.py` | Umbrella domain snapshot; keep synchronized with Global World |
| Global World → business mapping | Parent `global_world_business_map.py` | Business-facing crosswalk; not a second master catalogue |
| Business provider categories | Parent `business_catalog.py` and `sectors/` | Provider/business categories and their sector packages |
| Work/business sector taxonomy | `universal_work_business_taxonomy_catalog.py` | 26 broad sector records (A–Z) |
| Employment context | `../global_freelancer_gig_independent_work_business_api_ecosystem/jobs_careers_employment_api_ecosystem/categories.py` | 24 employment-context categories |
| Job-family specializations | Each category's own child package under `../global_freelancer_gig_independent_work_business_api_ecosystem/jobs_careers_employment_api_ecosystem/<category_id>/` | 234 direct-child specialization folders across the 24 categories |
| Professional occupations | `../global_freelancer_gig_independent_work_business_api_ecosystem/jobs_careers_employment_api_ecosystem/professional_fields/` | 12 professional fields and 81 field subcategories |
| Freelance and gig specializations | `../global_freelancer_gig_independent_work_business_api_ecosystem/` | 25 independent specialization packages; each owns its work-type catalogue |
| Core business/work domains | Parent `domain_registry.py` and the 12 registered domain packages | Domain IDs and subcategory IDs are maintained by their owning packages |
| Industry verticals | `../industry_api_ecosystems/` | 39 industry implementation packages; root-level industry folders are compatibility facades |
| Classification standards | `../classification_standards_business_api_ecosystem/` | Standards registry and import/crosswalk boundaries |
| Provider/platform ecosystems | Their individual `*_business_api_ecosystem/` packages | Provider-specific ownership; a package does not prove a live connection |

Employment context, occupation, industry, legal business entity, freelance service, product/service, and vacancy are different classification axes. They may be cross-linked, but must not be collapsed into one list or copied into competing catalogues. A job can have one occupation classification and multiple applicable employment-context facets.

### Repository path rule
The canonical Global Bada Business implementation is:

`backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`

The old `backend/api/global_api_ecosystem/global_bada_business_api_ecosystem/` location is a deprecated pointer only. Do not add implementation files or new catalogues there.

## Mounted API
Base path: `/api/v1/global-ecosystem/business/work-business-taxonomy`
- `GET /status`
- `GET /sectors`
- `GET /sectors/{sector_id}`
- `GET /sectors/search?q=...`
- `GET /facets`
- `GET /integrity`

Adult-restricted sector is excluded by default. Its inclusion flag is taxonomy visibility only, not age verification, consent verification, licensing or legal authorization.

## Data boundaries
- Taxonomy labels are not proof of official classification equivalence.
- NIC/NCO/ISIC/ISCO code datasets and versioned crosswalks require separate ingestion and validation.
- Country/state legal status, licences, job vacancies, employer identities, pricing and live provider connections are not verified here.
- Work modes and audience groups are facets, not industries or personal records.
- Company/Companies, Platforms and Organizations remain in their owning ecosystems.
- The counts above describe repository structure, not complete worldwide coverage, active vacancies, verified businesses or live service availability.
