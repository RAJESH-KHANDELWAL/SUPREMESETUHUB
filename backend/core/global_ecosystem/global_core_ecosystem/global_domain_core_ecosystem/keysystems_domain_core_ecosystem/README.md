# KEY-SYSTEMS Domain Core

Provider identity and metadata contracts for KEY-SYSTEMS within Global Domain Core.

- Provider ID: `keysystems`
- Source scope: Registrar reseller API
- Official reference: https://www.key-systems.net/
- API package reference: `keysystems_domain_api_ecosystem/keysystems_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
