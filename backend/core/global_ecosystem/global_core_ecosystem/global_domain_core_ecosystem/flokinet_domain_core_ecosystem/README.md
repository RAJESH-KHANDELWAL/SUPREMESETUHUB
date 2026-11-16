# FlokiNET Domain Core

Provider identity and metadata contracts for FlokiNET within Global Domain Core.

- Provider ID: `flokinet`
- Source scope: Hosting provider reference; registrar and API capabilities require verification
- Official reference: https://flokinet.is/
- API package reference: `flokinet_domain_api_ecosystem/flokinet_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
