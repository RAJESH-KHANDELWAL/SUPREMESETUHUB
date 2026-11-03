# Jobs, Careers & Employment API Ecosystem

Stable domain identifier: `jobs_careers_employment`.

## Scope

This package provides a structured India-and-global taxonomy across online, offline and hybrid channels. It is a discovery/API foundation, not a verified directory of providers, live vacancy/market feed, transaction system, or compliance certification.

## Independent category packages

The 15 industry-service categories are maintained as separate direct-child Python packages. Each package owns its `catalog.py`, `service.py`, `routes.py`, `README.md`, and `test_category.py`; there is no shared category implementation folder and no nested grouping directory. The aggregate `catalog.py` imports canonical category definitions from these packages, and `category_registry.py` mounts their routers.

- `recruitment_and_job_portals/` — Recruitment & Job Portals — `/category-modules/recruitment-and-job-portals`
- `freelancing_and_gig_work/` — Freelancing & Gig Work — `/category-modules/freelancing-and-gig-work`
- `remote_and_hybrid_work/` — Remote & Hybrid Work — `/category-modules/remote-and-hybrid-work`
- `staffing_and_placement/` — Staffing & Placement — `/category-modules/staffing-and-placement`
- `human_resources_and_payroll/` — Human Resources & Payroll — `/category-modules/human-resources-and-payroll`
- `career_guidance_and_counselling/` — Career Guidance & Counselling — `/category-modules/career-guidance-and-counselling`
- `internships_and_apprenticeships/` — Internships & Apprenticeships — `/category-modules/internships-and-apprenticeships`
- `executive_search/` — Executive Search & Leadership Hiring — `/category-modules/executive-search`
- `workforce_management/` — Workforce Management — `/category-modules/workforce-management`
- `resume_and_interview_services/` — Resume, Interview & Job Readiness — `/category-modules/resume-and-interview-services`
- `employer_branding/` — Employer Branding & Talent Marketing — `/category-modules/employer-branding`
- `employment_compliance/` — Labour & Employment Compliance — `/category-modules/employment-compliance`
- `outsourcing_and_bpo/` — Outsourcing & Business Process Services — `/category-modules/outsourcing-and-bpo`
- `reskilling_and_outplacement/` — Reskilling & Outplacement — `/category-modules/reskilling-and-outplacement`
- `professional_networking/` — Professional Networking & Talent Communities — `/category-modules/professional-networking`

## Domain endpoints

- `GET /industries/jobs-careers-employment/status`
- `GET /industries/jobs-careers-employment/categories`
- `GET /industries/jobs-careers-employment/categories?q=...`
- `GET /industries/jobs-careers-employment/categories/{category_id}`
- `GET /industries/jobs-careers-employment/employment-categories`
- `GET /industries/jobs-careers-employment/employment-categories?q=government`
- `GET /industries/jobs-careers-employment/employment-categories/{category_id}`

Each independent category also exposes `GET /industries/jobs-careers-employment/category-modules/{category-slug}` and its `/status` endpoint.

## Separate employment taxonomy

The detailed employment taxonomy remains sourced from the maintained `work_careers_employment_business_api_ecosystem` domain and is exposed through `/employment-categories`. It includes Government Jobs, Private Jobs, Corporate Jobs, Public Sector Jobs and other job classifications. The two taxonomies serve different purposes: this package classifies employment-industry services/providers, while the Work & Careers domain classifies work and job types. They are intentionally not merged or duplicated.

Provider onboarding, source provenance, freshness, verification, permissions and jurisdiction-specific compliance must be implemented before presenting records as verified or operational.
