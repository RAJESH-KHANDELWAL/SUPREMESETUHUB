# Gandi Domain Core

Provider identity and metadata contracts for Gandi within Global Domain Core.

- Provider ID: `gandi`
- Source scope: Registrar domain management
- Official reference: https://api.gandi.net/docs/
- API package reference: `gandi_domain_api_ecosystem/gandi_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
