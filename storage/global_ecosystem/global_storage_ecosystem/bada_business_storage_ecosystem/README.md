# BADA BUSINESS Storage Ecosystem

STORAGE-owned catalog and metadata namespace for BADA BUSINESS.

## Stored link catalogs

- `platform_links.json` — 9 platform, program, event and digital-store destination URLs.
- `course_links.json` — 11 Bada Business Community course destination URLs.
- `links_catalog_README.md` — catalog scope, provenance and handling rules.

**Total stored destinations: 20.**

## Responsibility
This package owns storage-side identity, metadata, taxonomy and provider destination catalogs. Provider API clients, authentication and external operations remain in their respective API/integration layers.

## Readiness boundary
The stored URLs are catalog records only. Their presence does not prove that a page is active, an account is authenticated, a course is included in a subscription, or a transaction/enrollment can be completed. Do not mark the provider connected without authorized live health checks and end-to-end tests. Never commit credentials or personal data.
