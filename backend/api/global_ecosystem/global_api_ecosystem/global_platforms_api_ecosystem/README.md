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

The platform profile registry is read-only and initially empty unless sourced records are added to data/platform_registry.json. Verified records require source URLs. Taxonomy endpoints do not make live third-party API calls or claim complete worldwide coverage.

## Company relationship
The owner/operator is represented by a relationship to a Company/Enterprise record in the Company ecosystem. Platform identity remains separate from the owning legal entity. Relationship edges such as owns, operates, publisher_of and reseller_of belong in a shared relationship layer.
