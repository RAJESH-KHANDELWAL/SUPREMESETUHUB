# Hurricane Electric DNS Domain Core

Provider identity and metadata contracts for Hurricane Electric DNS within Global Domain Core.

- Provider ID: `he`
- Source scope: Authoritative DNS service
- Official reference: https://dns.he.net/
- API package reference: `he_domain_api_ecosystem/he_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
