# Public Sector Jobs

Dedicated taxonomy package for public-sector employers and roles.

## Tracks
- `central_public_sector_enterprises` — Central Public Sector Enterprises: Central-government-owned or controlled commercial and industrial enterprises; ownership and control evidence must be recorded.
- `state_public_sector_enterprises` — State Public Sector Enterprises: State-government-owned or controlled enterprises, classified by the relevant state and ownership basis.
- `public_sector_banking` — Public Sector Banking: Roles with government-owned or controlled banks; bank ownership and legal employer must be verified.
- `public_sector_insurance` — Public Sector Insurance: Roles with public-sector insurance companies and institutions; distinguish statutory bodies from companies.
- `government_owned_corporations` — Government-Owned Corporations: Incorporated entities owned or controlled by government; may overlap with Corporate Jobs.
- `public_utilities_and_infrastructure` — Public Utilities and Infrastructure: Employment in public utilities and infrastructure operators, with ownership and regulatory status captured.
- `public_education_and_research_institutions` — Public Education and Research Institutions: Roles with public universities, publicly funded research bodies and education institutions.
- `public_health_institutions` — Public Health Institutions: Roles with government-owned hospitals, health authorities and public healthcare institutions.

## API
- `GET /public-sector-jobs/status`
- `GET /public-sector-jobs/tracks`
- `GET /public-sector-jobs/tracks/{track_id}`
- `GET /public-sector-jobs/search?q=...`

This package describes taxonomy only. It does not contain live vacancies or prove an employer's ownership. Verify the legal employer, jurisdiction, ownership/control basis and original recruitment notice.
