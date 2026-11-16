# IONOS Domain Core

Provider identity and metadata contracts for IONOS within Global Domain Core.

- Provider ID: `ionos`
- Source scope: Domain and DNS management
- Official reference: https://developer.hosting.ionos.com/
- API package reference: `ionos_domain_api_ecosystem/ionos_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
