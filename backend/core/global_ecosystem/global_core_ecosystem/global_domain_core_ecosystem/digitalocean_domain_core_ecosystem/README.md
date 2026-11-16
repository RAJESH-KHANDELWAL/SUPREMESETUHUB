# DigitalOcean Domain Core

Provider identity and metadata contracts for DigitalOcean within Global Domain Core.

- Provider ID: `digitalocean`
- Source scope: DNS records and domain zones
- Official reference: https://docs.digitalocean.com/reference/api/
- API package reference: `digitalocean_domain_api_ecosystem/digitalocean_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
