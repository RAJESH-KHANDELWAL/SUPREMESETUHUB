# GLOBAL SERVER ECOSYSTEM

Canonical hierarchy:

`GLOBAL ECOSYSTEM → GLOBAL SERVER ECOSYSTEM`

The ecosystem has two distinct catalogs beneath it:

1. **Provider ecosystems** — organizations/services where infrastructure may be hosted.
2. **Server service types** — kinds of server or networking service that can run on infrastructure.

## Provider ecosystems

- **HOSTINGER SERVER ECOSYSTEM** — web hosting, WordPress, domains, and MySQL.
- **GOOGLE SERVER ECOSYSTEM** — Google Cloud compute and deployment services.
- **AWS SERVER ECOSYSTEM** — AWS compute and deployment services.
- **MICROSOFT SERVER ECOSYSTEM** — Microsoft Azure compute and deployment services.
- **ORACLE SERVER ECOSYSTEM** — Oracle Cloud compute and virtual machines.
- **DIGITALOCEAN SERVER ECOSYSTEM** — Droplets and App Platform.
- **PROTON STORAGE ECOSYSTEM** — privacy-oriented file storage; not a general-purpose server host.
- **MEGA STORAGE ECOSYSTEM** — cloud file storage; not a general-purpose server host.

## Server service types

- **VPN SERVER** — encrypted remote-access or site-to-site networking.
- **VPS SERVER** — a virtual private server/virtual machine with supported administrative control.
- **CLOUD SERVER** — on-demand cloud compute and networking.
- **WEB SERVER** — serves HTTP/HTTPS content, often using a web server or reverse proxy.
- **CLOUD WEB SERVER** — cloud-hosted web application/static-site deployment, potentially with managed TLS and scaling where supported.

These are service categories, not separate vendors. For example, a VPS or cloud server can host a web server and a VPN server if its provider, operating system, network rules, and applicable terms support them. A VPN is a network service, not itself a server-hosting company.

## Integration and safety status

This registry is a **metadata catalog only**, not a live provider connection, server, VPN, or deployment controller. Service types currently use `catalog_only`; provider entries marked `not_configured` or `catalog_only` are not integrated. Do not claim a service is live until its infrastructure is configured and verified with end-to-end tests.

Keep passwords, API keys, OAuth secrets, database credentials, and SSH private keys in deployment secrets or a secret manager. Never commit them to GitHub. Do not perform remote operations without explicit authorization and audit logging.
