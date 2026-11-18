# Namecheap Domain Core

Provider identity and metadata contracts for Namecheap within Global Domain Core.

- Provider ID: `namecheap`
- Source scope: Domain registration, DNS, SSL
- Official reference: https://www.namecheap.com/support/api/
- API package reference: `namecheap_domain_api_ecosystem/namecheap_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
