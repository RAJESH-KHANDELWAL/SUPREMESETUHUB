# Certbot Domain Core

Provider identity and metadata contracts for Certbot within Global Domain Core.

- Provider ID: `certbot`
- Source scope: ACME TLS certificate automation tool
- Official reference: https://certbot.eff.org/
- API package reference: `certbot_domain_api_ecosystem/certbot_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
