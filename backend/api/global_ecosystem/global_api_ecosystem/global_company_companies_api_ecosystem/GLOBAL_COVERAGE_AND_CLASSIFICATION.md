# Global Company, Business and Freelancer Ecosystem

## One directory, three distinct record classes

The ecosystem exposes one normalized search and profile model with three mutually exclusive top-level classes:

- **company** — registered legal entities and other formally constituted organizations.
- **business** — operating businesses that are not necessarily represented as a registered company, including sole proprietors, MSMEs, startups and franchises.
- **freelancer** — individual independent professionals and service providers.

The detailed `entity_type` remains the legal or operational subtype. `record_type` is the directory-level class. Industry, size, legal status, country and verification are independent dimensions.

## API surface

The parent router mounts this module under `/api/v1/global-api-ecosystem`.

- `GET /global/companies/status` — readiness and registry/source counts.
- `GET /global/companies` — unified search; accepts `category=company|business|freelancer`.
- `GET /global/companies/search` — explicit search alias.
- `GET /global/companies/alphabet` — A–Z counts across all classes.
- `GET /global/companies/{company_id}` and `GET /global/company/{company_id}` — profile lookup.
- `GET /global/businesses` — business-only listing.
- `GET /global/freelancers` — freelancer-only listing.
- `GET /global/companies/sources` and `/sources/{source_id}` — source directory metadata.

## Data integrity and verification

- Stable IDs must be unique; every record needs a name and entity subtype.
- Explicit `record_type` must be company, business or freelancer. Legacy records infer this class from `entity_type`.
- `source_checked`, `registry_verified` and `identity_verified` records must carry source URLs. A website alone is not proof of legal registration.
- Country-specific identifiers must remain namespaced and jurisdiction-specific.
- Source directory metadata does not mean a provider API is connected. Live adapters require documented official/authorized interfaces, credentials where required, rate-limit handling and tests.
- Never bypass access controls or claim worldwide completeness from a partial registry.

## Current implementation boundary

The JSON registry is read-only through the API and currently contains zero profiles. The country source file is a curated directory, not a live connector. Status explicitly reports `registry_empty` until records are added. Google, Microsoft, AWS and Apple provider folders remain catalog/readiness metadata unless a real, tested company-data adapter is implemented.
