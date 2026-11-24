# GLOBAL ORGANIZATIONS API ECOSYSTEM

## Purpose
A standalone global directory and classification system for institutional and organizational bodies across Bharat and worldwide. It covers public institutions, intergovernmental bodies, civil society, nonprofits, education and research institutions, professional and trade associations, cooperatives, foundations and trusts, community and labor bodies, cultural and faith institutions, sports federations, standards bodies, and civic organizations.

## Entity boundary
An organization is an institutional identity. It is not automatically a Company, Enterprise, Corporate Group, or Platform. A registered company that also functions as an organization keeps its canonical legal/company profile in **Global Company Companies API Ecosystem**; this directory may reference its canonical company ID rather than duplicate that profile. User-owned workspace organizations managed by the existing `/organizations` CRUD API are a separate operational concept and are not imported into this global read-only directory.

## Architecture
- Root modules own shared routes, schemas, services, taxonomy and the canonical organization registry.
- `organization_domain_api_ecosystems/` owns domain taxonomy.
- `organization_type_api_ecosystems/` owns descriptive organization types.
- `country_api_ecosystems/` and the standards metadata package expose readiness information only until authoritative sources and datasets are researched and integrated.
- `integrations/`, `services/`, `tools/`, and `tests/` remain separate.
- Registry is read-only JSON and starts empty. No worldwide completeness is claimed.

## Four-ecosystem integration
1. **Bada Business** owns business categories, business domains and business taxonomy. This package may later use stable category/industry crosswalk IDs; it does not copy Bada Business catalogues or business records.
2. **Company Companies** owns canonical company, enterprise, legal-entity and corporate-group profiles. Organization records must reference those IDs where appropriate rather than creating duplicate company profiles.
3. **Platforms** owns digital/service platform identity. Organization-to-platform relationships use canonical platform IDs.
4. **Global Entity Relationships** centrally owns cross-ecosystem edges such as owns, operates, member_of, affiliated_with, funds, regulates and publishes. This package does not maintain a second relationship graph.

## Classification dimensions
Organization type, domain, legal form, governance model, geographic scope, country and verification status are independent dimensions. A taxonomy label is not legal registration, accreditation, regulatory approval, or identity verification.

## API
Mounted under `/api/v1/global-api-ecosystem`:
- `GET /global/organizations/status`
- `GET /global/organizations/architecture`
- `GET /global/organizations/domains`
- `GET /global/organizations/types`
- `GET /global/organizations/classification`
- `GET /global/organizations/country-sources/status`
- `GET /global/organizations/standards/status`
- `GET /global/organizations/integrations`
- `GET /global/organizations/services`
- `GET /global/organizations/tools`
- `GET /global/organizations` and `GET /global/organizations/search`
- `GET /global/organizations/{organization_id}`

These routes inherit the parent application's private-by-default middleware. They do not make live third-party API calls. Official country sources, standards datasets and classification crosswalks are not connected/ingested yet.

## Accuracy
This is a source-aware discovery directory. It does not establish legal status, good standing, accreditation, eligibility, licensing, or legitimacy. Add records only with source URLs and explicit verification status. Verify jurisdiction, source terms, freshness, and record scope before claiming coverage.
