# easyDNS Domain Core

Provider identity and metadata contracts for easyDNS within Global Domain Core.

- Provider ID: `easydns`
- Source scope: Domain and DNS API
- Official reference: https://www.easydns.com/
- API package reference: `easydns_domain_api_ecosystem/easydns_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
