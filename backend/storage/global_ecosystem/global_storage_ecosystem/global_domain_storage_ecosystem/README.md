# GLOBAL DOMAIN STORAGE ECOSYSTEM

Storage-owned taxonomy and metadata foundation for the global domain-name ecosystem. This layer catalogs domain products, services, assets, configuration metadata, and lifecycle state. Registrar APIs, DNS provider clients, authentication, remote reads/writes, registration, renewal, transfer, and other external operations remain in the API/integration layer.

## Domain storage ecosystems

1. [GLOBAL DOMAIN REGISTRATION STORAGE ECOSYSTEM](global_domain_registration_storage_ecosystem/README.md) — domain registration records, registrar relationships, registration terms, and renewal references.
2. [GLOBAL DNS AND NAMESERVER STORAGE ECOSYSTEM](global_dns_and_nameserver_storage_ecosystem/README.md) — DNS zones, records, nameserver assignments, delegation, and DNSSEC metadata.
3. [GLOBAL DOMAIN PORTFOLIO STORAGE ECOSYSTEM](global_domain_portfolio_storage_ecosystem/README.md) — domain identity, portfolios, ownership references, grouping, and inventory metadata.
4. [GLOBAL DOMAIN HOSTING STORAGE ECOSYSTEM](global_domain_hosting_storage_ecosystem/README.md) — hosting associations, origin references, website mappings, and infrastructure metadata.

## Domain storage capability catalogs

The broader domain storage taxonomy also contains backup and recovery, business and enterprise domains, content classification and policy, data transfer and migration, developer and platform domains, lifecycle management, security and certificates, geographical scope, and domain levels.

## Architecture boundary

- Storage owns domain identity, portfolio metadata, registration references, DNS configuration metadata, lifecycle definitions, domain health metadata, and storage-side governance.
- API/integration layers own registrar and DNS provider clients, authorization, remote reads/writes, registration, renewal, transfer, and provider-specific operations.
- A catalog entry does not prove registrar coverage, domain availability, account entitlement, authorized connectivity, or working operations.
- Mark a provider connected only after authorized live health checks and end-to-end tests pass.

## Security

Never commit registrar credentials, authorization codes, API tokens, private customer records, or personal data. Apply least privilege, encryption, consent, retention, deletion, audit, and jurisdictional controls.
