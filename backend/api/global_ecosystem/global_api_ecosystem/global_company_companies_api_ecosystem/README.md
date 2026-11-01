# GLOBAL COMPANY / COMPANIES API ECOSYSTEM

## Scope
Company-specific ecosystem for India and global jurisdictions. Canonical record classes are **Company**, **Enterprise** and **Corporate Group**. A Freelancer / independent professional is not a Company record class; its independent-professional package is not mounted as a Company class.

## Architecture
Domain packages follow the reference package convention: `README.md`, `__init__.py`, `catalog.py`, `models.py`, `service.py`, `subcategories.py`; route modules are added where HTTP endpoints are exposed. Root registries, catalogues, world crosswalk, schemas, services, routes, integrations, sectors, tools and tests coordinate the ecosystem.

## Distinct concepts
- **Company:** legally constituted legal entity.
- **Enterprise:** operating economic organization; its legal form may vary.
- **Corporate Group:** parent, holding, subsidiary or affiliated entity structure.

A legal company may operate an enterprise or belong to a corporate group, but these concepts must not be silently conflated.

## Evidence boundary
Taxonomies are not exhaustive world registries. A module does not prove a company profile exists. Verification requires provenance, jurisdiction, timestamps and evidence. No live provider connection is claimed unless explicitly configured and tested.

## Reference boundary
Global Bada Business API is used only for architecture and package-layout conventions. Its business categories, industry taxonomy, provider data and business-specific content are not imported into this Company ecosystem.
