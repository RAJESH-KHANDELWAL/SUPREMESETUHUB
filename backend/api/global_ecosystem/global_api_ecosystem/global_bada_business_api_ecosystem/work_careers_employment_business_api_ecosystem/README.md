# Work, Jobs & Careers

## Purpose and scope
This domain organizes employment, recruitment, staffing, career support and work-arrangement taxonomy for India and international discovery. It is a classification and API contract package, not a live job board, employer verification service, recruitment agency, licence register or legal eligibility engine.

## Architecture
- `categories.py` is the canonical detailed catalogue for this domain. It defines stable category IDs, descriptions, category dimensions, audience groups, search terms, scope notes, verification requirements and related-category links.
- `models.py` defines typed category records.
- `catalog.py` provides list, lookup, search and catalogue metadata operations from the canonical catalogue.
- `service.py` provides the domain service interface used by the parent ecosystem.
- `routes.py` mounts independently maintained subcategory API routers under `/work-careers`.
- `subcategories/` contains dedicated packages. Each package is intended to own its own detailed taxonomy, models, schemas, services, routes, validators, tests and documentation as it is implemented.

## Current subcategory implementation
### Government Jobs
The `subcategories/government_jobs/` package contains 13 recruitment tracks covering central, state/provincial, local, civil-service, public education, public health, public safety, civilian defence, public research, judiciary/legal, public finance/audit, public infrastructure/engineering and public-sector enterprise recruitment.

Its supporting layers include typed models, a notice provenance schema, structural validators, search and lookup services, API routes, tests and package documentation. The minimum notice contract captures issuing authority, jurisdiction, official URL, notice identifier, publication date and last-verification timestamp.

## API route structure
The domain router is mounted beneath the existing Bada Business API:
- `/api/v1/global-ecosystem/business/work-careers/government-jobs/status`
- `/api/v1/global-ecosystem/business/work-careers/government-jobs/tracks`
- `/api/v1/global-ecosystem/business/work-careers/government-jobs/tracks/{track_id}`
- `/api/v1/global-ecosystem/business/work-careers/government-jobs/search?q=...`
- `/api/v1/global-ecosystem/business/work-careers/government-jobs/integrity`

## Taxonomy boundaries and quality controls
- A category record does not prove a vacancy is active, an employer is genuine, a recruiter is authorized or a candidate is eligible.
- Government, public-sector enterprise and private-sector employment are distinct classifications; preserve the employer's legal identity and classification basis.
- Work arrangement, geography, schedule, engagement type and seniority are independent dimensions and may overlap.
- Do not infer visa sponsorship, domicile, reservation, age limits, qualification equivalence, professional registration or statutory compliance.
- HTTPS shape validation is not proof that a website is official. Verification status must be backed by evidence stored separately.
- Do not store candidate profiles, identity documents, applications, private messages, payment credentials or other sensitive personal data in this taxonomy package.

## Compatibility and maintenance
The package retains `DOMAIN_ID`, `DOMAIN_NAME`, `ADULT_RESTRICTED`, `DEFAULT_DISCOVERY_ENABLED`, `SUBCATEGORY_IDS` and `list_subcategories()` exports. Existing parent registry identifiers remain stable. Add new category IDs rather than renaming established identifiers, and update related-category references and tests together.
