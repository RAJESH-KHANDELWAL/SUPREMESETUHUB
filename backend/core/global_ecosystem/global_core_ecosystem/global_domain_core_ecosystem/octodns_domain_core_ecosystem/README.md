# octoDNS Domain Core

Provider identity and metadata contracts for octoDNS within Global Domain Core.

- Provider ID: `octodns`
- Source scope: DNS management automation tool
- Official reference: https://github.com/octodns/octodns
- API package reference: `octodns_domain_api_ecosystem/octodns_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
