# Gcore Domain Core

Provider identity and metadata contracts for Gcore within Global Domain Core.

- Provider ID: `gcore`
- Source scope: DNS and edge network services
- Official reference: https://api.gcore.com/docs/
- API package reference: `gcore_domain_api_ecosystem/gcore_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
