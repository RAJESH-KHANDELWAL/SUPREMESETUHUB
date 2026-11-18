# DuckDNS Domain Core

Provider identity and metadata contracts for DuckDNS within Global Domain Core.

- Provider ID: `duckdns`
- Source scope: Dynamic DNS service
- Official reference: https://www.duckdns.org/
- API package reference: `duckdns_domain_api_ecosystem/duckdns_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
