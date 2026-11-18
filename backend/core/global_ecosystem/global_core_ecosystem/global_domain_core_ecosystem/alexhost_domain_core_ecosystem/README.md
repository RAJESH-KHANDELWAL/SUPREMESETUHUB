# AlexHost Domain Core

Provider identity and metadata contracts for AlexHost within Global Domain Core.

- Provider ID: `alexhost`
- Source scope: Hosting and domain-related services reference; API/registrar support requires verification
- Official reference: https://alexhost.com/
- API package reference: `alexhost_domain_api_ecosystem/alexhost_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
