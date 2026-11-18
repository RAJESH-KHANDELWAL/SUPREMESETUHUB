# WHOIS Domain Core

Provider identity and metadata contracts for WHOIS within Global Domain Core.

- Provider ID: `whois`
- Source scope: Domain registration lookup protocol/reference
- Official reference: https://www.icann.org/resources/pages/whois-2013-05-03-en
- API package reference: `whois_domain_api_ecosystem/whois_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
