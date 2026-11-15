# GLOBAL WORK & BUSINESS API ECOSYSTEM

**Parent:** Global Bada Business API Ecosystem  
**Coverage intent:** Bharat + Global  
**Route prefix:** `/api/v1/global-ecosystem/business/work-business-directory`

This package is an aggregate discovery facade across distinct work and business classification axes. It reuses canonical catalogues and does not duplicate their records.

## Canonical ownership
- A–Z work/business sectors: `global_universal_work_business_taxonomy_api_ecosystem/`.
- Freelance, gig and independent work: `global_freelancer_gig_independent_work_business_api_ecosystem/`.
- Jobs, Careers & Employment: the `jobs_careers_employment_api_ecosystem/` child of the Freelancer/Gig domain.
- Industry, company, professional-service and provider records remain in their existing canonical packages.

## Endpoints
- `GET /status`
- `GET /sectors`
- `GET /sectors/search?q=...`
- `GET /sectors/{sector_id}`
- `GET /facets`
- `GET /freelance-specializations`
- `GET /jobs-careers/status`

These are taxonomy/discovery APIs, not a live vacancy board, verified client directory, provider availability feed or payment service.
