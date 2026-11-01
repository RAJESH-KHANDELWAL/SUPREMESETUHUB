# Global Company & Companies API Ecosystem — Coverage Blueprint

## Purpose

Build one country-aware directory and API for organizations, registered companies, businesses, startups, MSMEs, sole proprietors, freelancers, professional practices, public bodies, nonprofits, and service providers across India and other countries.

The directory is intended to support A–Z navigation and broad industry discovery. A category being defined does not mean that the directory already contains records for that category or that every country has a live data connection.

## Separate dimensions

Do not collapse these concepts into one field:

- **Entity type:** what kind of legal or operating entity this is.
- **Business size:** individual, micro, small, medium, large, or enterprise.
- **Industry:** the sector and optional sub-sector in which it operates.
- **Country and jurisdiction:** where it is registered or operates.
- **Audience/access label:** general, family-friendly, professional-only, or legally age-restricted.
- **Verification status:** how the identity and source evidence were checked.
- **Source connection status:** whether a source is merely catalogued, manually accessible, requires credentials, or is actually connected.

The canonical category definitions are in data/company_taxonomy.json.

## Adult, couples, family, and sexual-wellness classifications

The taxonomy deliberately separates family and relationship services from adult-oriented businesses. It includes categories for parenting, childcare, marriage services, couples counselling, relationship education, sexual-health education, sexual-wellness products, lawful adult retail, adult publishers, and lawful adult-entertainment businesses.

These are business metadata classifications, not permission to host or distribute explicit media. Adult-oriented listings must be lawful in the relevant jurisdictions, restricted to consenting adults, age-gated where required, privacy-protective, and compliant with licensing and platform rules. Any content involving minors, exploitation, trafficking, coercion, non-consensual intimate imagery, or uncertain age must be excluded. If legality or safeguards cannot be established, the listing must be excluded or held for review.

## Global data and verification rules

1. Prefer official company registries, government open-data portals, licensed commercial datasets, and provider-authorized APIs.
2. Keep a source directory separate from connected adapters. Never label a source as connected until a real integration has been tested.
3. Preserve source provenance: source ID, external record ID, evidence URL, retrieval timestamp, source update timestamp, and verification method.
4. Use country-specific registration identifiers. Do not assume CIN, SEC CIK, Companies House number, trade licence, or other identifiers share a global format.
5. Distinguish unverified, source_checked, registry_verified, identity_verified, and suspended. A source URL alone is not proof of identity.
6. Do not scrape access-controlled portals, bypass CAPTCHAs, or violate source terms. Respect API credentials, rate limits, attribution, licensing, and retention rules.
7. Expose coverage gaps and data freshness. Never claim a complete worldwide directory while records or country adapters are missing.
8. Avoid collecting unnecessary personal data, particularly for sole proprietors, freelancers, family services, and adult-oriented businesses.

## Implementation phases

### Phase 1 — Taxonomy and data contract
- Define entity types, business sizes, A–Z industry families, specialized classifications, adult access labels, and verification/source states.
- Add schema validation and tests for category IDs and cross-field rules.
- Extend records with provenance and country-specific identifiers without breaking existing API clients.

### Phase 2 — Registry and API quality
- Add safe filtering by industry, subcategory, entity type, business size, country, verification, and audience label.
- Add record detail, source detail, coverage summary, and data-freshness metadata.
- Keep empty registry status explicit; available must not imply populated or globally complete.

### Phase 3 — Country source onboarding
- Prioritize India, then onboard other jurisdictions through a documented source matrix.
- For each source, record official URL, supported entity coverage, access method, licensing, credentials, rate limits, update cadence, and adapter status.
- Build one tested adapter at a time with idempotent ingestion, deduplication, retries, audit logs, and source attribution.

### Phase 4 — Search, scale, and governance
- Move from a static JSON registry to a suitable persistent datastore when scale and operational needs justify it.
- Add moderation and review workflows for sensitive or age-restricted categories.
- Add monitoring for freshness, connector failures, duplicate records, and source policy changes.

## Current limitations to disclose

- The local company registry may be empty; taxonomy entries are not company records.
- The country source directory may contain references that are not connected APIs.
- Country coverage, legal-entity coverage, and update frequency vary by source.
- A–Z endpoints count only records actually present in the registry.
- No category should be described as fully covered until source ingestion and validation are implemented and tested.
