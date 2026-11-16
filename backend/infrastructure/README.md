# SUPREMESETUHUB Infrastructure

Infrastructure domain implementations and safe adapters are retained in this package. The central integration and discovery hub is:

`backend/infrastructure/global_ecosystem/global_infrastructure_ecosystem/`

## Domains owned here

Backup, Billing, CDN, Containers, Database adapters, DNS, Domains, Email, Firewall, FTP, Hosting, IPAM, Load Balancer, Infrastructure Models, Monitoring, Network, Object Storage, Security, Server inventory, SSL and Storage inventory.

Root-level infrastructure modules include controller, repository, service, Hostinger API/catalog and NSFWinfra.

## Cross-layer integration

- CORE: `backend.core` — platform identity, policy and shared foundation.
- GLOBAL CORE ECOSYSTEM: `backend.core.global_ecosystem.global_core_ecosystem` — canonical CORE ecosystem hierarchy and registry.
- GLOBAL ECOSYSTEM: `backend.global_ecosystem` — master domain and vendor ecosystem directory.
- GLOBAL INFRASTRUCTURE ECOSYSTEM: central read-only catalog, domain ownership map and governance boundary.

These are integrated through explicit metadata and discovery contracts. Their source implementations remain in their canonical packages; no duplicate copy is created.

## Safety and ownership

- Database persistence remains owned by `backend.database/`; infrastructure database adapters do not create a second persistence engine.
- Storage runtime remains owned by `backend.storage/`; infrastructure storage modules provide infrastructure-facing inventory/adapters.
- The canonical server ecosystem remains in `backend.server/global_ecosystem/global_server_ecosystem/`.
- CORE validates identity and policy; ENGINE owns executable operations; API owns HTTP orchestration.
- Catalog entries do not prove provider connectivity. Live operations require explicit adapters, configured credentials, scoped authorization, tests and verified connectivity.
- Never commit credentials, tokens, private keys or customer data.
