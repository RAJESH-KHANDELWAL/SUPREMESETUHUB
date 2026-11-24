# Work, Jobs & Business — Single Ownership Map

**Repository:** `RAJESH-KHANDELWAL/SUPREMESETUHUB`  
**Purpose:** one clear ownership boundary for taxonomy, business records, job/work workflows, freelance services and platform-specific modules.  
**Rule:** one canonical owner per data concept; other modules may expose routes, views, adapters or crosswalks, but must not maintain competing copies of the same catalogue or records.

## 1. Canonical classification and taxonomy owner

The maintained India + Global Bada Business API taxonomy implementation currently lives at:

`backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`

The sole canonical Bada Business product/domain package is:

`backend/global_ecosystem/global_bada_business_ecosystem/`

It owns provider-specific platform identity, links, programs, courses, products, events, registration resources and referrals. Its `api_ecosystem/` adapter exposes the existing API router without duplicating route code. API transport and broad business taxonomy remain in the API layer until a separately tested physical migration is completed.

| What the data describes | Canonical owner |
|---|---|
| Global A–Z umbrella domains | `global_world_catalog.py` |
| Global World → business/domain crosswalk | `global_world_business_map.py` |
| Business category catalogue | `business_catalog.py` |
| Business sector packages | `sectors/<sector>_business_sector/` |
| Detailed industry vertical APIs | `industry_api_ecosystems/<industry>/` |
| Work/business broad A–Z classification and shared discovery facets | `universal_work_business_taxonomy_api_ecosystem/` |
| Employment contexts and job-family specializations | `global_freelancer_gig_independent_work_business_api_ecosystem/jobs_careers_employment_api_ecosystem/` |
| Professional occupations and fields | `global_freelancer_gig_independent_work_business_api_ecosystem/jobs_careers_employment_api_ecosystem/professional_fields/` |
| Freelance, gig and independent-work specialization taxonomy | `global_freelancer_gig_independent_work_business_api_ecosystem/` |
| External classification standards and crosswalks | `classification_standards_business_api_ecosystem/` |

**Current repository structure checked:** 24 employment-context categories; 234 direct-child job-family/specialization folders under those categories; 12 professional-field packages with 81 field subcategories; and 25 freelance/gig specialization packages. These are repository structure counts, not counts of live vacancies, verified businesses, providers or complete worldwide coverage.

Keep these axes separate:
- Industry = what economic sector an activity belongs to.
- Business category = what kind of business/provider it is.
- Occupation/job family = what work a person performs.
- Employment context = how/where/when a role is engaged.
- Freelance service = what independent service is offered.
- Job vacancy = a specific, sourced opening with employer, location, dates and status.
- Business/company/platform = different entity types with separate identity and access controls.

Cross-link these axes with IDs and validated crosswalks; do not copy one catalogue into another.

### Special case: Jobs, Careers & Employment industry vertical

\`industry_api_ecosystems/jobs_careers_employment/\` owns a separate industry/service taxonomy of 15 categories and 60 subcategories (recruitment portals, staffing, HR/payroll, freelance platforms, career guidance, etc.). It exposes the 24-category employment classification by importing the canonical Work & Careers catalogue; it must not copy or fork those 24 employment records. The root-level \`jobs_careers_employment/\` package is a compatibility facade pointing to that maintained industry implementation.

## 2. Operational records and workflow owners

These packages are related, but they are not duplicate taxonomies:

| Capability / records | Owner | Boundary |
|---|---|---|
| Business profiles and owner-scoped business records | `backend/businesses/` | General business entity records and persistence |
| Business profile API | `backend/api/businesses.py` | API over the canonical Business domain |
| Large/enterprise business view | `backend/api/big_businesses.py` | Filtered API view over the same Business records; not a second database |
| General Global Business connection facade | `backend/api/global_business_ecosystem.py` | Connection/search facade; not the Bada Business taxonomy master |
| Freelancer records, provider readiness and public-source research | `backend/api/global_freelancer_ecosystem.py`, `backend/engine/freelancer_ecosystem/`, `backend/freelancer/global_freelancer_ecosystem/` | Freelancer workflow and research; classification remains in the canonical freelance taxonomy |
| Work requests, assignments and payment workflow | `backend/engine/work_business.py` | Operational work lifecycle; not a job-category catalogue |
| Marketplace entry points for work/income | `backend/api/supreme_work_income.py` and `backend/supreme/supreme_ecosystem/work_income/catalog.json` | Marketplace source links, not verified live job listings |
| LINKSETU job experience | `backend/platform/linksetu/job/` | LINKSETU-specific job posting and application workflow |
| LINKSETU business experience | `backend/platform/linksetu/business/` | LINKSETU-specific business presence |
| SUPREME business-system status/connection registry | `backend/supreme/supreme_ecosystem/supreme_business_ecosystem/` | System status and connection metadata, not business profiles |
| Bada Business product/domain root | `backend/global_ecosystem/global_bada_business_ecosystem/` | Provider-specific links, programs, courses, products, events, registration and referral metadata; API router exposed by adapter |


## 3. Duplicate and compatibility paths

- Canonical implementation: `backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`
- Deprecated duplicate path: `backend/api/global_api_ecosystem/global_bada_business_api_ecosystem/`. It now contains only a README pointer. Do not add code or new catalogues there.
- The separate `backend/businesses/`, `backend/freelancer/`, `backend/platform/linksetu/` and `backend/supreme/` packages have distinct operational responsibilities. Do not delete or merge them into the taxonomy package.
- `backend/global_ecosystem/global_bada_business_ecosystem/` is the sole canonical Bada Business product/domain root for provider-specific resources. The API router remains independently owned by `backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`.

## 4. Router and deployment notes

The main FastAPI application imports and registers the Bada Business API router, general Global Business router, Global Freelancer router, Business and Big Business routers, and Supreme Work & Income router. These are separate interfaces over their respective domains.

A router being registered does not prove that a third-party provider, employer, vacancy feed, payment rail or government source is connected. Record source provenance, last-verified time, market/jurisdiction and status for externally sourced data.

## 5. Change-control rules

1. Add each new sector, job family, occupation, freelance specialization or business category only to its canonical owner.
2. Give every specialization its own folder and files under its owning category; keep its tests beside that package.
3. Update the parent registry, API routes, schemas, documentation and tests in the same change.
4. Use stable IDs for cross-links. Do not infer legal form, licence, eligibility or professional authorization from a taxonomy label.
5. Do not represent marketplace links or taxonomy entries as live jobs or verified providers.
6. Before deleting or moving a legacy package, search imports, router registrations, tests, workflows and external consumers; preserve a compatibility facade where needed.
7. Run the relevant GitHub Actions tests after each structural change. Deployment secrets and infrastructure configuration must be handled separately from code changes.
