# Nominet Domain Core

Provider identity and metadata contracts for Nominet within Global Domain Core.

- Provider ID: `nominet`
- Source scope: UK .uk domain registry
- Official reference: https://nominet.uk/
- API package reference: `nominet_domain_api_ecosystem/nominet_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
