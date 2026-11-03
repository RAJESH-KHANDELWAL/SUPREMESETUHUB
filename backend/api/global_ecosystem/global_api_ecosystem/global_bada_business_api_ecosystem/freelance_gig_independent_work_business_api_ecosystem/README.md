# Freelancing, Gig & Independent Work

## Purpose
Independent services, project work, gig assignments and professional contracting across creative, technical, administrative and local-service skills.

## Architecture
Each of the 25 canonical specializations has its own direct-child package folder. Each package owns its own README, work-type catalogue, typed model, catalogue functions, service facade, API routes, response schemas, validators and tests. The specialization's work types are defined in that folder's `work_types.py`; do not add a second copy of those work types to this domain root.

The root `__init__.py` remains the canonical index of stable specialization IDs. `specializations.py` mounts the independent specialization routers. Root `catalog.py` and `service.py` remain the domain-level discovery facade.

## Boundaries
This is a taxonomy and API-contract package, not a live listing or verification service. A category does not prove that a job is open, an employer or client is genuine, a business is registered, a professional is licensed or a third-party API is connected. India + Global describe intended coverage, not exhaustive country-level availability.

Do not store personal profiles, applications, private messages, payment credentials, medical records or other sensitive personal data in this package. Keep operational records in their owning systems and connect them through stable identifiers. Add source provenance, country/jurisdiction, timestamps, verification state, freshness, deduplication and moderation before ingesting listings.

## Maintenance
Keep specialization and work-type IDs stable and lowercase snake_case. Each specialization folder is the sole owner of its work-type definitions. Cross-domain overlaps (for example, SEO as a freelance service and SEO as an employment occupation) must use explicit crosswalk references rather than duplicate detailed records. Add tests for duplicate IDs, empty labels, importability and API serialization. Regulated work must respect local licensing and authorization requirements.
