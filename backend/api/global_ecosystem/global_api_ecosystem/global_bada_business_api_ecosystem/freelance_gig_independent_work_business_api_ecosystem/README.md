# Freelancing, Gig & Independent Work

## Purpose
Independent services, project work, gig assignments and professional contracting across creative, technical, administrative and local-service skills.

## Package contract
The adjacent `__init__.py` defines `DOMAIN_ID`, `DOMAIN_NAME`, `ADULT_RESTRICTED`, `DEFAULT_DISCOVERY_ENABLED`, `SUBCATEGORY_IDS` and `list_subcategories()`.

## Boundaries
This is a taxonomy package, not a live listing or verification service. A category does not prove that a job is open, an employer is genuine, a business is registered, a professional is licensed or a third-party API is connected. India + Global describe intended coverage, not exhaustive country-level availability.

Do not store personal profiles, applications, private messages, payment credentials, medical records or other sensitive personal data in this package. Keep operational records in their owning systems and connect them through stable identifiers. Add source provenance, country/jurisdiction, timestamps, verification state, freshness, deduplication and moderation before ingesting listings.

## Maintenance
Keep IDs stable and lowercase snake_case. Synchronize identifiers with `global_world_catalog.py`; check the business catalogue and Global World crosswalk for collisions or unmapped IDs. Add unit tests for duplicate IDs, empty labels, importability and API serialization.
