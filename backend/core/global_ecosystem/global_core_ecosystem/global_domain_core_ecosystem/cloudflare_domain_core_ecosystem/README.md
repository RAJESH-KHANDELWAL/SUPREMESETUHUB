# Cloudflare Domain Core

Provider identity and metadata contracts for Cloudflare within Global Domain Core.

- Provider ID: `cloudflare`
- Source scope: DNS zones, registrar domains, DNS records
- Official reference: https://developers.cloudflare.com/api/
- API package reference: `cloudflare_domain_api_ecosystem/cloudflare_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
