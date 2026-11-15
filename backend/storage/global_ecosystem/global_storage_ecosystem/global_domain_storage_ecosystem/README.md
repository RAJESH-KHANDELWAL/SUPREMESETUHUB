# GLOBAL DOMAIN STORAGE ECOSYSTEM

Storage-owned taxonomy and metadata foundation for the global domain-name ecosystem. This layer catalogs domain products, services, assets, configuration metadata, and lifecycle state. Registrar APIs, DNS provider clients, OAuth/authentication, remote reads/writes, registration, renewal, transfer, and other external operations remain in the API/integration layer.

## Domain storage ecosystems

1. [GLOBAL DOMAIN REGISTRATION STORAGE ECOSYSTEM](global_domain_registration_storage_ecosystem/README.md) — Domain registration records, registrar relationships, registration terms, acquisition provenance, and renewal references.
2. [GLOBAL DNS & NAMESERVER STORAGE ECOSYSTEM](global_dns_and_nameserver_storage_ecosystem/README.md) — DNS zones, records, nameserver assignments, delegation, DNSSEC metadata, and configuration history.
3. [GLOBAL DOMAIN PORTFOLIO STORAGE ECOSYSTEM](global_domain_portfolio_storage_ecosystem/README.md) — Domain portfolios, normalized domain identity, ownership references, grouping, and inventory metadata.
4. [GLOBAL DOMAIN HOSTING STORAGE ECOSYSTEM](global_domain_hosting_storage_ecosystem/README.md) — Domain-to-hosting associations, origin references, website mappings, deployment relationships, and infrastructure metadata.
5. [GLOBAL DOMAIN SECURITY STORAGE ECOSYSTEM](global_domain_security_storage_ecosystem/README.md) — Domain security posture, DNSSEC state, TLS certificate metadata, verification records, and security events.
6. [GLOBAL DOMAIN LIFECYCLE STORAGE ECOSYSTEM](global_domain_lifecycle_storage_ecosystem/README.md) — Domain creation, activation, expiry, renewal, suspension, restoration, and deletion lifecycle metadata.
7. [GLOBAL DOMAIN TRANSFER STORAGE ECOSYSTEM](global_domain_transfer_storage_ecosystem/README.md) — Domain transfer eligibility metadata, authorization references, transfer status, registrar migration, and audit history.
8. [GLOBAL DOMAIN BACKUP & RECOVERY STORAGE ECOSYSTEM](global_domain_backup_and_recovery_storage_ecosystem/README.md) — Domain configuration snapshots, DNS zone backups, recovery metadata, and restoration history.

## Domain storage capability catalogs

The broader domain storage taxonomy includes registration and acquisition, DNS and nameserver management, portfolio and identity, hosting and infrastructure, security and certificates, backup and recovery, transfer and migration, business and enterprise domains, developer and platform domains, geographical scope, domain levels, lifecycle management, and content classification/policy.

## Architecture boundary

- Storage owns domain identity, portfolio metadata, registration references, DNS configuration metadata, lifecycle definitions, domain health metadata, and storage-side governance.
- API/integration layers own registrar and DNS provider clients, authorization, remote reads/writes, registration, renewal, transfer, and provider-specific operations.
- A catalog entry does not prove registrar coverage, domain availability, account entitlement, authorized connectivity, or working operations.
- Mark a provider connected only after authorized live health checks and end-to-end tests pass.

## Security

Never commit registrar credentials, authorization codes, API tokens, private customer records, or personal data. Apply least privilege, encryption, consent, retention, deletion, audit, and jurisdictional controls.
