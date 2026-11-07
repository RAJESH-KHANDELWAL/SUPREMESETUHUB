# Global Bada Business Ecosystem

Canonical backend home for Bada Business-specific ecosystem capabilities.

## Scope
- Bada Business product taxonomy, modules and product-specific workflows.
- Bada Business classification extensions and product-facing services.
- India and global business coverage, with source and verification metadata.

## Existing implementation
The established implementation currently lives at:
`backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`

Keep that implementation intact while this canonical package is introduced. Migration must be incremental: preserve existing router paths, public imports, data contracts and tests. Prefer thin compatibility imports over copying business logic or registries.

## Boundaries
- General business ecosystem concepts belong in `backend/businesses/global_ecosystem/global_business_ecosystem/`.
- Do not import or copy unrelated Bada Business categories into Company or Platform ecosystems.
- Catalogue metadata is not proof of legal registration, licensing, verification or live provider connectivity.
- Adult-industry classifications must remain lawful, age-restricted and excluded from default discovery, with production-grade safeguards before exposure.

This directory is the canonical product boundary, not a claim that the existing API implementation has already been moved.
