# ISC BIND Domain Core

Provider identity and metadata contracts for ISC BIND within Global Domain Core.

- Provider ID: `bind`
- Source scope: DNS server software and management
- Official reference: https://bind9.readthedocs.io/
- API package reference: `bind_domain_api_ecosystem/bind_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
