# Industries & Professional Services

## Scope
Cross-sector industry and professional service classification. Detailed industry registries and sector implementations remain in the existing industry_api_ecosystems/ and sectors/ packages.

## Package contract
The adjacent __init__.py exposes the stable domain ID, domain name, discovery flags, subcategory identifiers and list_subcategories() helper.

## Data boundaries
This is a classification package, not a live directory. Category membership does not verify a business, job, employer, professional licence, government affiliation or API integration. India + Global are intended coverage scopes, not an assertion of exhaustive country coverage. Do not store private or sensitive personal records here.

## Maintenance
Keep identifiers stable and synchronized with global_world_catalog.py. Validate crosswalk coverage and duplicate IDs. Before production listing ingestion, add source provenance, jurisdiction, timestamps, verification status, freshness, deduplication, moderation, authentication, authorization and audit logging. Add import and unit tests.
