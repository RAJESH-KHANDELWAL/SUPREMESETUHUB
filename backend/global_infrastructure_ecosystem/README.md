# GLOBAL INFRASTRUCTURE ECOSYSTEM

Backend infrastructure domains are kept in separate top-level packages. Each domain follows the same pattern:

`backend/<domain>/global_ecosystem/global_<domain>_ecosystem/`

Domains in this initial scaffold: storage, cloud, server, DNS, VPS, VPN, and SSH. Each domain has its own registry, documentation, tests, and provider-specific directories/files. This is an extensible architecture scaffold, not a claim that provider accounts are connected.

Security rules: use official/authorized APIs; keep credentials in deployment secrets or a secret manager; never commit passwords, private keys, access tokens, VPN profiles, or SSH private keys. Remote actions must be explicitly authorized and audited.
