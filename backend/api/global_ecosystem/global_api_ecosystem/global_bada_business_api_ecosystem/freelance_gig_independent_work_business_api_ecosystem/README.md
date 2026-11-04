# Freelancing, Gig & Independent Work

## Purpose
Independent services, project work, gig assignments and professional contracting across creative, technical, administrative and local-service skills.

## Architecture
Each of the 25 canonical specializations has its own direct-child package folder. Each package owns its README, work-type catalogue, typed model, catalogue functions, service facade, API routes, response schemas, validators and tests. The specialization's `work_types.py` is the single source of truth for stable work-type IDs, names and descriptions.

Every canonical work type now also has its own child API package under its owning specialization:
- one folder per work-type ID;
- its own README, `__init__.py`, `categories.py`, `models.py`, `catalog.py`, `schemas.py`, `services.py`, `routes.py` and `validators.py`;
- its own `tests/` package and test module;
- its own API route, mounted by the owning specialization router.

Leaf packages resolve their metadata from the parent specialization's `work_types.py`. This preserves a single source of truth and prevents duplicate or drifting work-type records.

The root `__init__.py` remains the canonical index of stable specialization IDs. `specializations.py` mounts the specialization routers, and each specialization mounts its own work-type routers. Root `catalog.py` and `service.py` remain the domain-level discovery facade.

## Boundaries
This is a taxonomy and API-contract package, not a live listing or verification service. A category does not prove that a job is open, an employer or client is genuine, a business is registered, a professional is licensed or a third-party API is connected. India + Global describe intended coverage, not exhaustive country-level availability.

Do not store personal profiles, applications, private messages, payment credentials, medical records or other sensitive personal data in this package. Keep operational records in their owning systems and connect them through stable identifiers. Add source provenance, country/jurisdiction, timestamps, verification state, freshness, deduplication and moderation before ingesting listings.

## Maintenance
Keep specialization and work-type IDs stable and lowercase snake_case. Each specialization folder is the sole owner of its work-type definitions. Each work-type child package is a dedicated API/validation boundary and must continue to resolve its canonical record from the owning specialization. Cross-domain overlaps (for example, SEO as a freelance service and SEO as an employment occupation) must use explicit crosswalk references rather than duplicate detailed records. Add tests for duplicate IDs, empty labels, importability and API serialization. Regulated work must respect local licensing and authorization requirements.
