# GLOBAL DOMAIN STORAGE ECOSYSTEM

Storage-owned taxonomy and metadata foundation for the global domain-name ecosystem. This package follows the same parent-catalog architecture as GOOGLE STORAGE ECOSYSTEM: one canonical taxonomy, one category index, and independent domain storage ecosystem packages.

- `taxonomy/global_domain_storage_taxonomy.json`: canonical domain storage taxonomy.
- `category_index.json`: canonical index of all 17 domain storage child ecosystems and their paths.
- Each child ecosystem owns its README and manifest. Core domain packages and capability packages remain independently addressable.
- Root-level foundation modules define shared configuration, models, registry, services, and tests.

## Core domain storage ecosystems

1. [GLOBAL DOMAIN REGISTRATION STORAGE ECOSYSTEM](global_domain_registration_storage_ecosystem/README.md) — domain registration records, registrar relationships, registration terms, acquisition provenance, and renewal references.
2. [GLOBAL DNS AND NAMESERVER STORAGE ECOSYSTEM](global_dns_and_nameserver_storage_ecosystem/README.md) — DNS zones, records, nameserver assignments, delegation, DNSSEC, and configuration history.
3. [GLOBAL DOMAIN PORTFOLIO STORAGE ECOSYSTEM](global_domain_portfolio_storage_ecosystem/README.md) — domain identity, portfolios, ownership references, grouping, and inventory metadata.
4. [GLOBAL DOMAIN HOSTING STORAGE ECOSYSTEM](global_domain_hosting_storage_ecosystem/README.md) — hosting associations, origin references, website mappings, and infrastructure metadata.

## Domain capability storage ecosystems

5. [GLOBAL BUSINESS AND ENTERPRISE DOMAINS STORAGE ECOSYSTEM](business_and_enterprise_domains/README.md) — business, enterprise, organization, and multi-domain metadata.
6. [GLOBAL CONTENT CLASSIFICATION AND POLICY STORAGE ECOSYSTEM](content_classification_and_policy/README.md) — classification, policy, content labels, and governance metadata.
7. [GLOBAL DEVELOPER AND PLATFORM DOMAINS STORAGE ECOSYSTEM](developer_and_platform_domains/README.md) — developer, platform, application, and service-domain metadata.
8. [GLOBAL DNS AND NAMESERVER MANAGEMENT STORAGE ECOSYSTEM](dns_and_nameserver_management/README.md) — DNS management configuration and operational metadata.
9. [GLOBAL DOMAIN BACKUP AND RECOVERY STORAGE ECOSYSTEM](domain_backup_and_recovery/README.md) — backup inventories, recovery points, and restoration metadata.
10. [GLOBAL DOMAIN HOSTING AND INFRASTRUCTURE STORAGE ECOSYSTEM](domain_hosting_and_infrastructure/README.md) — hosting environments, infrastructure associations, and origin metadata.
11. [GLOBAL DOMAIN LEVELS STORAGE ECOSYSTEM](domain_levels/README.md) — domain levels, hierarchy, and classification metadata.
12. [GLOBAL DOMAIN LIFECYCLE MANAGEMENT STORAGE ECOSYSTEM](domain_lifecycle_management/README.md) — lifecycle states, milestones, expiration, renewal, and transition metadata.
13. [GLOBAL DOMAIN PORTFOLIO AND IDENTITY STORAGE ECOSYSTEM](domain_portfolio_and_identity/README.md) — identity, ownership references, portfolio grouping, and inventory metadata.
14. [GLOBAL DOMAIN REGISTRATION AND ACQUISITION STORAGE ECOSYSTEM](domain_registration_and_acquisition/README.md) — registration, acquisition, provenance, and registrar-reference metadata.
15. [GLOBAL DOMAIN SECURITY AND CERTIFICATES STORAGE ECOSYSTEM](domain_security_and_certificates/README.md) — security posture, certificate inventory, expiry, and trust metadata.
16. [GLOBAL DOMAIN TRANSFER AND MIGRATION STORAGE ECOSYSTEM](domain_transfer_and_migration/README.md) — transfer requests, migration plans, status, and audit metadata.
17. [GLOBAL GEOGRAPHICAL DOMAIN STORAGE ECOSYSTEM](geographical_domain_ecosystem/README.md) — geographic scope, jurisdiction, regional allocation, and localization metadata.

## Architecture boundary

- Storage owns domain identity, portfolio metadata, registration references, DNS configuration metadata, lifecycle definitions, domain health metadata, taxonomy, and storage-side governance.
- API/integration layers own registrar and DNS provider clients, authorization, remote reads/writes, registration, renewal, transfer, and provider-specific operations.
- A catalog entry does not prove registrar coverage, domain availability, account entitlement, authorized connectivity, or working operations.
- Mark a provider connected only after authorized live health checks and end-to-end tests pass.

## Security

Never commit registrar credentials, authorization codes, API tokens, private customer records, or personal data. Apply least privilege, encryption, consent, retention, deletion, audit, and jurisdictional controls.

These packages are taxonomy and metadata foundations; they do not claim live registrar, DNS, hosting, or certificate integrations.
