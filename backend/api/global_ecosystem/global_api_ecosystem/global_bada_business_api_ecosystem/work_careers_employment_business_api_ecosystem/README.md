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

All 24 catalogue categories now have dedicated packages under `subcategories/`. Each package has its own `categories.py`, `models.py`, `services.py`, `routes.py`, `README.md` and `tests/`. Each defined track has its own folder under that package's `tracks/` directory with a dedicated README describing its scope and evidence requirements.

### Employer sector and organization
- `government_jobs/` — 13 tracks, including central, state/provincial, local, civil services, public education, public health, public safety, civilian defence, public research, judiciary/legal, public finance/audit, infrastructure/engineering and public-sector enterprise recruitment.
- `private_sector_jobs/` — 8 tracks, including private companies, SMEs, proprietorships, partnership firms, startups, family-owned businesses, professional firms and retail/service businesses.
- `corporate_jobs/` — 8 tracks, including private limited, public/listed, multinational, corporate groups, large enterprises, head-office, management and government-owned corporations.
- `public_sector_jobs/` — 8 tracks, including central/state public enterprises, public banking and insurance, government-owned corporations, utilities, public education/research and public health.

### Geography and work arrangement
- `international_jobs/`, `local_jobs/`, `remote_jobs/` and `hybrid_jobs/`.

### Working time and engagement
- `full_time_jobs/`, `part_time_jobs/`, `contract_jobs/`, `temporary_jobs/`, `seasonal_jobs/` and `shift_work/`.

### Experience and career pathways
- `entry_level_jobs/`, `experienced_jobs/`, `executive_jobs/`, `career_changes/`, `return_to_work/` and `retirement_work/`.

### Career and workforce services
- `career_guidance/`, `recruitment/`, `staffing/` and `placements/`. These are service categories, not job vacancies.

The domain router imports and mounts all 24 category routers beneath `/work-careers`. Track folders describe classification scope; they do not imply that a vacancy, employer, recruiter, licence or placement outcome has been verified.

## API route structure
Each job category exposes status, track list, track detail and search endpoints under its own prefix. Examples:
- `/api/v1/global-ecosystem/business/work-careers/government-jobs/status`
- `/api/v1/global-ecosystem/business/work-careers/private-jobs/tracks`
- `/api/v1/global-ecosystem/business/work-careers/corporate-jobs/tracks/{track_id}`
- `/api/v1/global-ecosystem/business/work-careers/public-sector-jobs/search?q=...`
- `/api/v1/global-ecosystem/business/work-careers/remote-jobs/tracks`
- `/api/v1/global-ecosystem/business/work-careers/recruitment/tracks`

## Taxonomy boundaries and quality controls
- A category record does not prove a vacancy is active, an employer is genuine, a recruiter is authorized or a candidate is eligible.
- Government, public-sector enterprise and private-sector employment are distinct classifications; preserve the employer's legal identity and classification basis.
- Work arrangement, geography, schedule, engagement type and seniority are independent dimensions and may overlap.
- Do not infer visa sponsorship, domicile, reservation, age limits, qualification equivalence, professional registration or statutory compliance.
- HTTPS shape validation is not proof that a website is official. Verification status must be backed by evidence stored separately.
- Do not store candidate profiles, identity documents, applications, private messages, payment credentials or other sensitive personal data in this taxonomy package.

## Compatibility and maintenance
The package retains `DOMAIN_ID`, `DOMAIN_NAME`, `ADULT_RESTRICTED`, `DEFAULT_DISCOVERY_ENABLED`, `SUBCATEGORY_IDS` and `list_subcategories()` exports. Existing parent registry identifiers remain stable. Add new category IDs rather than renaming established identifiers, and update related-category references and tests together.
