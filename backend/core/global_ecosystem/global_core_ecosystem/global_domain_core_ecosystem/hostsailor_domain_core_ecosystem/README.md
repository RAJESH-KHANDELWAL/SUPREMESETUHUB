# HostSailor Domain Core

Provider identity and metadata contracts for HostSailor within Global Domain Core.

- Provider ID: `hostsailor`
- Source scope: Hosting provider reference; domain services/API capabilities require verification
- Official reference: https://hostsailor.com/
- API package reference: `hostsailor_domain_api_ecosystem/hostsailor_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
