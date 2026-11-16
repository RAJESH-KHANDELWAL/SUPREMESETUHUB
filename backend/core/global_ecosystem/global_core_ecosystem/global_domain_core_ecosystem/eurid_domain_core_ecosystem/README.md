# EURid Domain Core

Provider identity and metadata contracts for EURid within Global Domain Core.

- Provider ID: `eurid`
- Source scope: .eu domain registry
- Official reference: https://eurid.eu/
- API package reference: `eurid_domain_api_ecosystem/eurid_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
