# SUPREMESETUHUB Infrastructure

The canonical infrastructure control plane and its root-level integration modules remain in this package. All 21 infrastructure domain implementations are physically organized under:

`backend/infrastructure/global_ecosystem/global_infrastructure_ecosystem/`

## Domain ownership

The ecosystem root directly contains: Backup, Billing, CDN, Containers, Database adapters, DNS, Domains, Email, Firewall, FTP, Hosting, IPAM, Load Balancer, Infrastructure Models, Monitoring, Network, Object Storage, Security, Server inventory, SSL and Storage inventory.

Root-level infrastructure modules include controller, repository, service, Hostinger API/catalog and NSFWinfra.

## Compatibility

The `backend.infrastructure` package exposes the ecosystem domain directory on its package search path. Existing imports such as `backend.infrastructure.server` and `backend.infrastructure.model` remain compatible while their implementation files live only in the GLOBAL INFRASTRUCTURE ECOSYSTEM.

## Cross-layer ownership

- CORE: `backend.core` — platform identity, policy and shared foundation.
- GLOBAL CORE ECOSYSTEM: `backend.core.global_ecosystem.global_core_ecosystem`.
- GLOBAL ECOSYSTEM: `backend.global_ecosystem`.
- Database persistence remains owned by `backend.database/`.
- Storage runtime remains owned by `backend.storage/`.
- Canonical server ecosystem remains in `backend.server/global_ecosystem/global_server_ecosystem/`.
- CORE validates identity and policy; ENGINE owns executable operations; API owns HTTP orchestration.

Catalog entries do not prove provider connectivity. Live operations require explicit adapters, configured credentials, scoped authorization, tests and verified connectivity. Never commit credentials, tokens, private keys or customer data.
