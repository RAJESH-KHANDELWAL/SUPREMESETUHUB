# Work, Jobs & Careers

## Purpose and scope
This domain organizes employment, recruitment, staffing, career support and work-arrangement taxonomy for India and international discovery. It is a classification and API contract package, not a live job board, employer verification service, recruitment agency, licence register or legal eligibility engine.

## Architecture
- `categories.py` is the canonical detailed catalogue for this domain. It defines stable category IDs, descriptions, category dimensions, audience groups, search terms, scope notes, verification requirements and related-category links.
- `models.py` defines typed category records.
- `catalog.py` provides list, lookup, search and catalogue metadata operations from the canonical catalogue.
- `service.py` provides the domain service interface used by the parent ecosystem.
- `routes.py` mounts independently maintained category API Ecosystem routers under `/work-careers`.
- Each category has a dedicated API Ecosystem package directly inside this domain directory. The category-level `categories.py` owns the canonical job-family records. Each child specialization package has its own stable identity, README, model, schema, service adapter, route, validator and tests; its `categories.py` binds to the owning category record rather than duplicating that record.

## Category API Ecosystem packages

All 24 catalogue categories now have dedicated packages directly under this domain directory. Each package has its own `categories.py`, `models.py`, `services.py`, `routes.py`, `README.md` and `tests/`. Every specialization has its own direct-child folder inside its category package, with its own README, categories, models, schemas, services, routes, validators and tests. The parent category catalogue discovers these packages dynamically; the folder package is the source of truth for its job-family details.

### Employer sector and organization
- `government_jobs/` — 23 specializations, including central, state/provincial, local, civil services, public education, public health, public safety, civilian defence, public research, judiciary/legal, public finance/audit, infrastructure/engineering and public-sector enterprise recruitment.
- `private_sector_jobs/` — multiple specializations, including private companies, SMEs, proprietorships, partnership firms, startups, family-owned businesses, professional firms and retail/service businesses.
- `corporate_jobs/` — multiple specializations, including private limited, public/listed, multinational, corporate groups, large enterprises, head-office, management and government-owned corporations.
- `public_sector_jobs/` — multiple specializations, including central/state public enterprises, public banking and insurance, government-owned corporations, utilities, public education/research and public health.

### Geography and work arrangement
- `international_jobs/`, `local_jobs/`, `remote_jobs/` and `hybrid_jobs/`.

### Working time and engagement
- `full_time_jobs/`, `part_time_jobs/`, `contract_jobs/`, `temporary_jobs/`, `seasonal_jobs/` and `shift_work/`.

### Experience and career pathways
- `entry_level_jobs/`, `experienced_jobs/`, `executive_jobs/`, `career_changes/`, `return_to_work/` and `retirement_work/`.

### Career and workforce services
- `career_guidance/`, `recruitment/`, `staffing/` and `placements/`. These are service categories, not job vacancies.

The domain router mounts all 24 category routers beneath `/work-careers`. The parent Bada Business router separately mounts every direct-child job-family router at its canonical `/work-careers/{category_id}/{job_family_id}` path. These folders describe classification scope; they do not imply that a vacancy, employer, recruiter, licence or placement outcome has been verified.

## API route structure
Each job category exposes status, specialization list, specialization detail and search endpoints under its own prefix. Examples:
- `/api/v1/global-ecosystem/business/work-careers/government-jobs/status`
- `/api/v1/global-ecosystem/business/work-careers/private-jobs/specializations`
- `/api/v1/global-ecosystem/business/work-careers/corporate-jobs/specializations/{specialization_id}`
- `/api/v1/global-ecosystem/business/work-careers/public-sector-jobs/search?q=...`
- `/api/v1/global-ecosystem/business/work-careers/remote-jobs/specializations`
- `/api/v1/global-ecosystem/business/work-careers/recruitment/specializations`

## Taxonomy boundaries and quality controls
- A category record does not prove a vacancy is active, an employer is genuine, a recruiter is authorized or a candidate is eligible.
- Government, public-sector enterprise and private-sector employment are distinct classifications; preserve the employer's legal identity and classification basis.
- Work arrangement, geography, schedule, engagement type and seniority are independent dimensions and may overlap.
- Do not infer visa sponsorship, domicile, reservation, age limits, qualification equivalence, professional registration or statutory compliance.
- HTTPS shape validation is not proof that a website is official. Verification status must be backed by evidence stored separately.
- Do not store candidate profiles, identity documents, applications, private messages, payment credentials or other sensitive personal data in this taxonomy package.

## Compatibility and maintenance
The package retains `DOMAIN_ID`, `DOMAIN_NAME`, `ADULT_RESTRICTED`, `DEFAULT_DISCOVERY_ENABLED`, `SUBCATEGORY_IDS` and `list_categories()` exports. Existing parent registry identifiers remain stable. Add new category IDs rather than renaming established identifiers, and update related-category references and tests together.


## Hierarchical API Ecosystem architecture

The 24 catalogue categories are exposed as separately addressable API Ecosystems while retaining their stable Python package IDs and existing route prefixes. This avoids breaking imports and clients that already use the established taxonomy identifiers.

Category API Ecosystem IDs follow `{CATEGORY_ID}_API_ECOSYSTEM`, for example:
- `GOVERNMENT_JOBS_API_ECOSYSTEM`
- `PRIVATE_SECTOR_JOBS_API_ECOSYSTEM` (display name: Private Jobs API Ecosystem)
- `CORPORATE_JOBS_API_ECOSYSTEM`
- `PUBLIC_SECTOR_JOBS_API_ECOSYSTEM`

Every specialization is also exposed as a child API Ecosystem resource. Its ID follows `{CATEGORY_ID}_{TRACK_ID}_API_ECOSYSTEM`. For example, a Government Jobs specialization such as `central_government_recruitment` is represented as `GOVERNMENT_JOBS_CENTRAL_GOVERNMENT_RECRUITMENT_API_ECOSYSTEM`.

### API Ecosystem registry endpoints

- `GET /api/v1/global-ecosystem/business/work-careers/api-ecosystems` — list all 24 category API Ecosystems.
- `GET /api/v1/global-ecosystem/business/work-careers/api-ecosystems?q=government` — search category API Ecosystems.
- `GET /api/v1/global-ecosystem/business/work-careers/api-ecosystems/{category_id}` — category API Ecosystem contract and catalogue record.
- `GET /api/v1/global-ecosystem/business/work-careers/api-ecosystems/{category_id}/specializations` — list the child specialization API Ecosystems.
- `GET /api/v1/global-ecosystem/business/work-careers/api-ecosystems/{category_id}/specializations/{specialization_id}` — retrieve one specialization API Ecosystem and its taxonomy record.

The category-specific routers remain available under their existing paths (for example `/government-jobs`, `/private-jobs` and `/corporate-jobs`). The registry is an additional stable discovery layer, not a replacement for those routes.

Specialization-level API Ecosystems are currently addressable taxonomy resources served by the shared registry. Their own independent external data integrations, write operations, vacancy feeds and employer verification are not implied. All responses retain `taxonomy_only` status unless separately verified live-data integrations are implemented.


## Professional Fields & Occupation Families

The domain now separates **professional occupation** from the existing 24 employment-context categories. The new `professional_fields/` package contains dedicated field packages for IT & Digital Technology, Banking & Finance, Healthcare & Medical, Education & Training, Engineering & Construction, Sales & Marketing, Legal & Compliance, Agriculture & Food Systems, Manufacturing & Operations, Real Estate & Facilities, Hospitality & Tourism, and Transport & Logistics. Each field owns its canonical subcategory catalogue; subcategory documentation is organized in child folders.

The shared Professional Fields API Ecosystem is mounted under the existing `/work-careers` router:
- `GET /api/v1/global-ecosystem/business/work-careers/professional-fields` — list and search professional fields.
- `GET /api/v1/global-ecosystem/business/work-careers/professional-fields/{field_id}` — field detail and its subcategories.
- `GET /api/v1/global-ecosystem/business/work-careers/professional-fields/{field_id}/subcategories` — list/search subcategories.
- `GET /api/v1/global-ecosystem/business/work-careers/professional-fields/{field_id}/subcategories/{subcategory_id}` — subcategory detail.
- `GET /api/v1/global-ecosystem/business/work-careers/professional-fields/integrity` — structural integrity report.

The field and subcategory API Ecosystem identifiers are stable registry resources. Separate child routers are intentionally not created for taxonomy-only folders unless they later require independent operations, data ownership or external integrations. A role can be tagged with a professional field and simultaneously with any applicable existing employment-context categories; this avoids duplicating the same occupation for remote, government, private, corporate or international work.

Coverage remains `taxonomy_only`: this change does not add live vacancy feeds, employer verification, recruiter authorization, credential validation or legal eligibility decisions.
