# OpenSRS Domain Core

Provider identity and metadata contracts for OpenSRS within Global Domain Core.

- Provider ID: `opensrs`
- Source scope: Domain reseller and registrar API
- Official reference: https://domains.opensrs.guide/
- API package reference: `opensrs_domain_api_ecosystem/opensrs_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
