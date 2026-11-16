# Akamai Domain Core

Provider identity and metadata contracts for Akamai within Global Domain Core.

- Provider ID: `akamai`
- Source scope: Edge DNS and domain services
- Official reference: https://techdocs.akamai.com/
- API package reference: `akamai_domain_api_ecosystem/akamai_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
