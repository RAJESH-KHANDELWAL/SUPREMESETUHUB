# GLOBAL SERVER ECOSYSTEM

Canonical hierarchy:

`GLOBAL ECOSYSTEM → GLOBAL SERVER ECOSYSTEM → provider ecosystem`

Provider ecosystems in the catalog:

- **HOSTINGER SERVER ECOSYSTEM** — web hosting, WordPress, domains, and MySQL.
- **GOOGLE SERVER ECOSYSTEM** — Google Cloud compute and deployment services.
- **AWS SERVER ECOSYSTEM** — AWS compute and deployment services.
- **MICROSOFT SERVER ECOSYSTEM** — Microsoft Azure compute and deployment services.
- **ORACLE SERVER ECOSYSTEM** — Oracle Cloud compute and virtual machines.
- **DIGITALOCEAN SERVER ECOSYSTEM** — Droplets and App Platform.
- **PROTON STORAGE ECOSYSTEM** — privacy-oriented file storage; not a general-purpose server host.
- **MEGA STORAGE ECOSYSTEM** — cloud file storage; not a general-purpose server host.

## Important status and safety rules

This registry is a **metadata catalog**, not a live provider connection, server, or deployment controller. Entries marked `not_configured` or `catalog_only` are not integrated. A provider becomes connected only after its official API or supported connection is configured with least-privilege credentials and verified with end-to-end tests.

Keep passwords, API keys, OAuth secrets, database credentials, and SSH private keys in deployment secrets or a secret manager. Never commit them to GitHub. Do not perform remote operations without explicit authorization and audit logging.

Proton and MEGA are included because they are relevant to the wider infrastructure/storage ecosystem; they are not represented as compute-server providers.
