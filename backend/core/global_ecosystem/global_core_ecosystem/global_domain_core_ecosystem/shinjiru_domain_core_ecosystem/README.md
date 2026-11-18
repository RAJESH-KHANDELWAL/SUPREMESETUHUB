# Shinjiru Domain Core

Provider identity and metadata contracts for Shinjiru within Global Domain Core.

- Provider ID: `shinjiru`
- Source scope: Hosting provider reference; domain services/API capabilities require verification
- Official reference: https://www.shinjiru.com/
- API package reference: `shinjiru_domain_api_ecosystem/shinjiru_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
