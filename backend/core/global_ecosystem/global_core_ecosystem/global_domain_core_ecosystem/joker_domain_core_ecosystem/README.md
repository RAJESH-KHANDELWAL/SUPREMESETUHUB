# Joker.com Domain Core

Provider identity and metadata contracts for Joker.com within Global Domain Core.

- Provider ID: `joker`
- Source scope: Registrar and domain management
- Official reference: https://joker.com/
- API package reference: `joker_domain_api_ecosystem/joker_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
