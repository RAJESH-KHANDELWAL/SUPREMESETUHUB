# ICANN Domain Core

Provider identity and metadata contracts for ICANN within Global Domain Core.

- Provider ID: `icann`
- Source scope: Global domain name coordination and registrar accreditation
- Official reference: https://www.icann.org/
- API package reference: `icann_domain_api_ecosystem/icann_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
