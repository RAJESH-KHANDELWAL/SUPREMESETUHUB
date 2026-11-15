# GLOBAL DOMAIN STORAGE ECOSYSTEM

Storage-owned taxonomy and metadata foundation for the global domain-name ecosystem. This layer catalogs domain products, services, assets, configuration metadata, and lifecycle state. Registrar APIs, DNS provider clients, authentication, remote reads/writes, registration, renewal, transfer, and other external operations remain in the API/integration layer.

## Domain storage ecosystems

1. [GLOBAL DOMAIN REGISTRATION STORAGE ECOSYSTEM](global_domain_registration_storage_ecosystem/README.md) — domain registration records, registrar relationships, registration terms, and renewal references.
2. [GLOBAL DNS AND NAMESERVER STORAGE ECOSYSTEM](global_dns_and_nameserver_storage_ecosystem/README.md) — DNS zones, records, nameserver assignments, delegation, and DNSSEC metadata.
3. [GLOBAL DOMAIN PORTFOLIO STORAGE ECOSYSTEM](global_domain_portfolio_storage_ecosystem/README.md) — domain identity, portfolios, ownership references, grouping, and inventory metadata.
4. [GLOBAL DOMAIN HOSTING STORAGE ECOSYSTEM](global_domain_hosting_storage_ecosystem/README.md) — hosting associations, origin references, website mappings, and infrastructure metadata.

## Domain storage capability catalogs

Additional capability catalogs are organized as dedicated global domain storage ecosystems: GLOBAL_BUSINESS_AND_ENTERPRISE_DOMAINS_STORAGE_ECOSYSTEM, GLOBAL_CONTENT_CLASSIFICATION_AND_POLICY_STORAGE_ECOSYSTEM, GLOBAL_DEVELOPER_AND_PLATFORM_DOMAINS_STORAGE_ECOSYSTEM, GLOBAL_DNS_AND_NAMESERVER_MANAGEMENT_STORAGE_ECOSYSTEM, GLOBAL_DOMAIN_BACKUP_AND_RECOVERY_STORAGE_ECOSYSTEM, GLOBAL_DOMAIN_HOSTING_AND_INFRASTRUCTURE_STORAGE_ECOSYSTEM, GLOBAL_DOMAIN_LEVELS_STORAGE_ECOSYSTEM, GLOBAL_DOMAIN_LIFECYCLE_MANAGEMENT_STORAGE_ECOSYSTEM, GLOBAL_DOMAIN_PORTFOLIO_AND_IDENTITY_STORAGE_ECOSYSTEM, GLOBAL_DOMAIN_REGISTRATION_AND_ACQUISITION_STORAGE_ECOSYSTEM, GLOBAL_DOMAIN_SECURITY_AND_CERTIFICATES_STORAGE_ECOSYSTEM, GLOBAL_DOMAIN_TRANSFER_AND_MIGRATION_STORAGE_ECOSYSTEM, GLOBAL_GEOGRAPHICAL_DOMAIN_STORAGE_ECOSYSTEM.

## Architecture boundary

- Storage owns domain identity, portfolio metadata, registration references, DNS configuration metadata, lifecycle definitions, domain health metadata, and storage-side governance.
- API/integration layers own registrar and DNS provider clients, authorization, remote reads/writes, registration, renewal, transfer, and provider-specific operations.
- A catalog entry does not prove registrar coverage, domain availability, account entitlement, authorized connectivity, or working operations.
- Mark a provider connected only after authorized live health checks and end-to-end tests pass.

## Security

Never commit registrar credentials, authorization codes, API tokens, private customer records, or personal data. Apply least privilege, encryption, consent, retention, deletion, audit, and jurisdictional controls.
