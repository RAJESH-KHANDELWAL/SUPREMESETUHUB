# ACME protocol Domain Core

Provider identity and metadata contracts for ACME protocol within Global Domain Core.

- Provider ID: `acme`
- Source scope: Automated certificate management protocol
- Official reference: https://datatracker.ietf.org/doc/html/rfc8555
- API package reference: `acme_domain_api_ecosystem/acme_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
