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


## Requested ecosystem ownership and routing

The following ownership rules are the canonical routing guide for the Global Bada Business ecosystem. Keep each detailed catalogue in its owning package; root-level folders that are documented as compatibility facades must remain facades rather than duplicate implementations.

| Topic / provider | Canonical destination | Routing rule |
|---|---|---|
| Google, AWS, Microsoft and Apple digital/cloud/software/platform services | `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/` | Keep provider-specific business ecosystems under this Global Digital Infrastructure & Technology domain. The Google, AWS, Microsoft and Apple provider folders are already present here. |
| Sexual health, reproductive health, sexual wellness and adult intimacy education | `global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_coach_consultant_advisor_professional_services_work_business_api_ecosystem/` | Keep only the sexual/reproductive/adult-wellness scope here. General healthcare, hospitals, diagnostics, medicines and non-sexual wellness remain in the healthcare/life-sciences ecosystems. Adult-restricted visibility must retain the existing lawful, consent and age-gating boundaries. |
| Water resources and marine industries | `industry_api_ecosystems/water_resources_marine_industries/` | Use the root `water_resources_marine_industries/` package only as its existing compatibility facade. |
| Travel and tourism | `industry_api_ecosystems/travel_tourism_hospitality/` | Use the root `travel_tourism_hospitality/` package only as its existing compatibility facade. This is the Global Travel industry destination; do not merge it into hotels/restaurants-only hospitality. |
| Startups, entrepreneurship and MSMEs/SMEs | `industry_api_ecosystems/startups_entrepreneurship/` | Use the root `startups_entrepreneurship/` package only as its existing compatibility facade. Keep startup formation, founder support, incubation, funding and MSME growth in this industry domain. |

### Important separation

- General healthcare is **not** moved into Kamasutra; only sexual/reproductive health and adult sexual wellness belong there.
- Global Hospitality (hotels, resorts and restaurants) remains a distinct industry from Global Travel & Tourism, with cross-links where useful.
- Agriculture-specific startup/MSME records may remain in the agriculture ecosystem; cross-link them to Startups & Entrepreneurship rather than duplicating the same records.
- This routing guide records the intended canonical ownership. It does not claim that provider APIs are connected, that external services are live, or that every cross-reference/import has been audited.

## Next 12 industry-domain ownership audit (2026-11-05)

The following ownership map was checked against the current repository tree and the available package documentation. These are canonical destinations, not instructions to duplicate packages or move files.

| Requested domain | Canonical owner in this repository | Routing / boundary |
|---|---|---|
| Finance | `industry_api_ecosystems/finance_banking_insurance/` | Banking, payments, lending, insurance, investments and finance discovery stay together. |
| Education | `industry_api_ecosystems/education_learning_training/` | Schools, higher education, coaching, EdTech, skills and business education stay here. |
| Agriculture | `industry_api_ecosystems/agriculture_food_natural_resources/` | Agriculture, food systems and natural-resource business taxonomy; keep agriculture-specific trade linked here while cross-border trade execution remains in its dedicated trade domain. |
| Energy | `global_energy_utilities_environment_api_ecosystem/` | Maintained directly at the Bada Business root; do not create a duplicate under `industry_api_ecosystems/`. |
| Real Estate | `industry_api_ecosystems/real_estate_construction/` | Property, real estate and construction discovery; keep the similarly named legacy/infrastructure packages as compatibility or cross-reference layers until import usage is audited. |
| Manufacturing | `manufacturing_industrial_services/` | Maintained directly at the Bada Business root, outside `industry_api_ecosystems/`; do not duplicate its taxonomy. |
| Automotive | `industry_api_ecosystems/automotive_mobility/` | Vehicles, EVs, automotive manufacturing, parts and vehicle-specific mobility; general freight/logistics stays in transport/logistics. |
| Fashion | `industry_api_ecosystems/fashion_textiles_apparel/` | Fashion/textile production and industry services; retail discovery may cross-link to retail, without duplicating production taxonomy. |
| Media | `industry_api_ecosystems/marketing_media_entertainment/` | Unified marketing, advertising, media and entertainment taxonomy; `media_entertainment_creative_industries/` should remain an alias/crosswalk unless code audit proves separate ownership is required. |
| Legal | `global_legal_services_api_ecosystem/` and the legal-specific root domain packages | Legal advice, lawyers, litigation and representation stay separate from `industry_api_ecosystems/professional_legal_business_services/`, which explicitly excludes legal practice. |
| Retail & E-commerce | `industry_api_ecosystems/retail_ecommerce_consumer_goods/` | Retail, marketplaces, wholesale/distribution and consumer goods; fashion production remains with Fashion. |
| Sports | `industry_api_ecosystems/sports_recreation_community/` | Sports, recreation and community activity discovery. |

### Audit safeguards

- Existing canonical packages are reused; no parallel industry package should be created just to make names look uniform.
- Energy and Manufacturing are intentionally root-maintained packages, not missing industry packages.
- Media, Real Estate and Legal have overlapping legacy/root names. Do not delete or physically relocate those paths until Python imports, route mounts, registry entries and tests have been checked.
- This update records verified ownership and routing guidance only. It does not claim that every provider integration is live, that listings are verified, or that all legacy imports have been migrated.

