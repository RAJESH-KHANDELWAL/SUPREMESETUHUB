# DNSSEC Domain Core

Provider identity and metadata contracts for DNSSEC within Global Domain Core.

- Provider ID: `dnssec`
- Source scope: DNS security extension ecosystem
- Official reference: https://www.cloudflare.com/dns/dnssec/
- API package reference: `dnssec_domain_api_ecosystem/dnssec_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
