# GLOBAL PLATFORMS API ECOSYSTEM

## Purpose
A global directory and classification system for digital and service platforms used in Bharat and worldwide. A platform is a service or infrastructure surface through which users, businesses, developers, creators or public bodies interact. It is not the same thing as its owner company.

## Architecture
This package uses the modular package-layout discipline of the Global Bada Business ecosystem, without importing its business categories or records. Root modules own shared routes, schemas, services, taxonomy and the canonical platform registry. Provider-specific packages live in *_platforms_api_ecosystem directories. Integrations, services, tools and tests remain separate.

## Classification
Domains include AI/data, communication, media, commerce, finance/payments, work/business, cloud/infrastructure, software development, education, health/wellness, travel/transport, public services and lawful adult industry. Domain, platform type, ownership, business model, country and verification are independent dimensions.

"Normal", "advanced" and "supreme" are not legal entity types. If maturity tiers are desired, model them separately as optional capability/maturity metadata.

## Adult-industry safeguards
Lawful adult-industry platforms are classified in a separate adult-only domain and excluded from lists/search by default. Explicit include_adult=true changes catalogue filtering only; it is not age verification, legal approval or permission to access content. Any future live service must implement jurisdiction restrictions, robust age assurance, consent and safety controls before enabling adult access.

## API
- GET /global/platforms/status
- GET /global/platforms/architecture
- GET /global/platforms/domains?include_adult=false
- GET /global/platforms/domains/{domain_id}?include_adult=false
- GET /global/platforms/classification
- GET /global/platforms and /global/platforms/search
- GET /global/platforms/{platform_id}?include_adult=false

The platform profile registry is read-only and now contains 76 unverified discovery entries: 28 Bharat-focused, 34 global and 14 lawful adult-industry entries. All entries remain explicitly unverified; no legal status, ownership, current availability or live third-party API connection is asserted. Verified records require source URLs. Taxonomy endpoints do not make live third-party API calls or claim complete worldwide coverage.

## Company relationship
The owner/operator is represented by a relationship to a Company/Enterprise record in the Company ecosystem. Platform identity remains separate from the owning legal entity. Relationship edges such as owns, operates, publisher_of and reseller_of belong in a shared relationship layer.


## Runtime directory and provider packages

The nested `global_platforms_ecosystem/` package now delegates to the canonical
parent platform registry; it does not maintain a second profile store.

- `GET /global/platforms/directory` lists and filters platform profiles.
- `GET /global/platforms/directory/{platform_id}` retrieves a profile.
- `GET /global/platforms/directory/domains` lists domains with adult filtering.
- `GET /global/platforms/directory/status` reports registry status.
- `GET /global/platforms/providers` lists provider-specific packages.
- `GET /global/platforms/providers/{provider_id}` retrieves provider metadata.

The provider directory covers Apple, AWS, Google and Microsoft, plus 14 separate
lawful adult-industry provider packages. Adult-only provider metadata is
excluded by default and requires explicit `include_adult=true`; the directory
is metadata-only and is not age verification or a live provider connection.
