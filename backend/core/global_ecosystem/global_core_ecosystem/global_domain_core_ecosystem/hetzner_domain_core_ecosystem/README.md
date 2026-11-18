# Hetzner Domain Core

Provider identity and metadata contracts for Hetzner within Global Domain Core.

- Provider ID: `hetzner`
- Source scope: DNS and infrastructure services
- Official reference: https://dns.hetzner.com/
- API package reference: `hetzner_domain_api_ecosystem/hetzner_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
