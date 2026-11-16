# deSEC DNS Domain Core

Provider identity and metadata contracts for deSEC DNS within Global Domain Core.

- Provider ID: `desec`
- Source scope: DNS hosting service
- Official reference: https://desec.readthedocs.io/
- API package reference: `desec_domain_api_ecosystem/desec_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
