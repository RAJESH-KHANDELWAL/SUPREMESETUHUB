# DNSExit Domain Core

Provider identity and metadata contracts for DNSExit within Global Domain Core.

- Provider ID: `dnsexit`
- Source scope: DNS and dynamic DNS
- Official reference: https://dnsexit.com/
- API package reference: `dnsexit_domain_api_ecosystem/dnsexit_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
