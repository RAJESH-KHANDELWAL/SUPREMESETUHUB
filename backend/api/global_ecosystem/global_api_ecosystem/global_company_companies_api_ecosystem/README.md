# GLOBAL COMPANY / COMPANIES API ECOSYSTEM

## Scope
Company-specific ecosystem for India and global jurisdictions. Canonical record classes are **Company**, **Enterprise** and **Corporate Group**. A Freelancer / independent professional is not a Company record class. Legacy profile filtering remains for compatibility, but Freelancer is not included in the canonical class registry or mounted as a Company directory.

## Architecture
Domain packages follow the reference package convention: `README.md`, `__init__.py`, `catalog.py`, `models.py`, `service.py`, `subcategories.py`; route modules are included where HTTP endpoints are exposed. Root registries, catalogues, world crosswalk, schemas, services, routes, integrations, sectors, tools and tests coordinate the ecosystem.

## Distinct concepts
- **Company:** legally constituted legal entity.
- **Enterprise:** operating economic organization; its legal form may vary.
- **Corporate Group:** parent, holding, subsidiary or affiliated entity structure.

A legal company may operate an enterprise or belong to a corporate group, but these concepts must not be silently conflated. The legacy `/global/company-directory/business` routes remain as compatibility endpoints; canonical Enterprise endpoints are under `/global/company-directory/enterprises`.

## Taxonomy and evidence boundaries
Industry and sector catalogues are curated navigation metadata, not an exact statutory classification crosswalk. Country entries are source-directory metadata. Provider entries do not imply connected company-registration APIs. Profile verification requires provenance, jurisdiction, timestamps and evidence. The local company profile registry remains empty until sourced records are added.

## Reference boundary
Global Bada Business API is used only for architecture and package-layout conventions. Its business categories, industry taxonomy, provider data and business-specific content are not imported into this Company ecosystem.

## Company-specific profile adapters

The 26 company packages under `global_companies_ecosystem/` expose a consistent API contract:
- `GET /global/company-profile-adapters/{company_id}` — company discovery profile.
- `GET /global/company-profile-adapters/{company_id}/sources` — declared source provenance.
- `GET /global/company-profile-adapters/{company_id}/status` — adapter configuration and connectivity status.

Each package has its own `schemas.py`, `service.py`, `routes.py` and `__init__.py`, and is mounted by the aggregate company-profile router. Current entries register official company websites as discovery sources only. They deliberately report `source_registered_unverified`, `no_verified_legal_entity_record` and `not_connected` until jurisdiction-specific legal records, credentials, retrieval adapters, freshness controls and integration tests are implemented. These endpoints do not represent legal verification or live third-party data access.
