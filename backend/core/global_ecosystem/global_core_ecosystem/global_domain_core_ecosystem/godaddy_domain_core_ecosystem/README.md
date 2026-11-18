# GoDaddy Domain Core

Provider identity and metadata contracts for GoDaddy within Global Domain Core.

- Provider ID: `godaddy`
- Source scope: Domain registration and DNS
- Official reference: https://developer.godaddy.com/
- API package reference: `godaddy_domain_api_ecosystem/godaddy_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
