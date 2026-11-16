# Name.com Domain Core

Provider identity and metadata contracts for Name.com within Global Domain Core.

- Provider ID: `namecom`
- Source scope: Domain registration and DNS
- Official reference: https://www.name.com/api-docs/
- API package reference: `namecom_domain_api_ecosystem/namecom_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
