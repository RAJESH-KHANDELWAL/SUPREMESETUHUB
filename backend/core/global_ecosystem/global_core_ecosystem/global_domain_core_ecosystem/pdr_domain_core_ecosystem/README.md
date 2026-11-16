# Public Domain Registry Domain Core

Provider identity and metadata contracts for Public Domain Registry within Global Domain Core.

- Provider ID: `pdr`
- Source scope: Registrar and reseller ecosystem
- Official reference: https://publicdomainregistry.com/
- API package reference: `pdr_domain_api_ecosystem/pdr_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
