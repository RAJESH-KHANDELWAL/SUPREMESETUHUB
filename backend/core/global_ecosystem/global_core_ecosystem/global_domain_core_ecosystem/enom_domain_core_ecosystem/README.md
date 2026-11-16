# eNom Domain Core

Provider identity and metadata contracts for eNom within Global Domain Core.

- Provider ID: `enom`
- Source scope: Domain reseller API
- Official reference: https://www.enom.com/api/
- API package reference: `enom_domain_api_ecosystem/enom_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
