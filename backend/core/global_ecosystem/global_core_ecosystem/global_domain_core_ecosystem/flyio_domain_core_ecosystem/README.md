# Fly.io Domain Core

Provider identity and metadata contracts for Fly.io within Global Domain Core.

- Provider ID: `flyio`
- Source scope: Application domain and certificate management
- Official reference: https://fly.io/docs/machines/api/
- API package reference: `flyio_domain_api_ecosystem/flyio_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
