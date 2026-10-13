# GLOBAL SERVER ECOSYSTEM

Canonical hierarchy:

`GLOBAL ECOSYSTEM → GLOBAL SERVER ECOSYSTEM`

This canonical package keeps two related catalogs separate.

## Provider ecosystems

- **HOSTINGER SERVER ECOSYSTEM** — web hosting, WordPress, domains and MySQL.
- **GOOGLE SERVER ECOSYSTEM** — Google Cloud compute and deployment.
- **AWS SERVER ECOSYSTEM** — AWS compute and deployment.
- **MICROSOFT SERVER ECOSYSTEM** — Azure compute and deployment.
- **ORACLE SERVER ECOSYSTEM** — Oracle Cloud compute and virtual machines.
- **DIGITALOCEAN SERVER ECOSYSTEM** — Droplets and App Platform.
- **PROTON STORAGE ECOSYSTEM** — privacy-oriented file storage, not a general-purpose server host.
- **MEGA STORAGE ECOSYSTEM** — cloud file storage, not a general-purpose server host.

## Server service types

- **VPN SERVER** — encrypted remote-access or site-to-site networking.
- **VPS SERVER** — virtual private server / virtual machine.
- **CLOUD SERVER** — on-demand cloud compute and networking.
- **WEB SERVER** — HTTP/HTTPS serving, reverse proxy and static content.
- **CLOUD WEB SERVER** — cloud-hosted web deployment, with TLS/scaling where supported.

Provider entries identify vendors/services; service types describe what infrastructure may run. A VPN is a network service, not a hosting vendor. Proton and MEGA are storage providers, not general-purpose compute hosts.

## Integration status

This is a metadata catalog and read-only facade, not a live provider integration or deployment controller. Provider entries remain `not_configured` or `catalog_only`; service types remain `catalog_only`. No VPN or server is provisioned by these files.

Keep API keys, passwords, database credentials and SSH private keys in a deployment secret manager, never in Git. Verify official integrations end to end before changing a provider's status.
