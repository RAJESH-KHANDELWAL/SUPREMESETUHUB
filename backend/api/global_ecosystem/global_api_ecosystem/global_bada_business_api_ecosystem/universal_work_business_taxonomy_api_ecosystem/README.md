# Universal Work & Business Taxonomy API Ecosystem

**Parent:** Global Bada Business API Ecosystem  
**Coverage intent:** India + Global  
**Status:** Versioned discovery taxonomy; not a verified business directory, job board, licence register or legal opinion.

## Scope
A–Z sectors and subgroups, work models, delivery modes and audience facets for students, job seekers, employees, freelancers, homemakers, women, men, couples, families, entrepreneurs and enterprises.

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
