# Microsoft Azure DNS Domain Core

Provider identity and metadata contracts for Microsoft Azure DNS within Global Domain Core.

- Provider ID: `azure`
- Source scope: DNS zones and records
- Official reference: https://learn.microsoft.com/en-us/rest/api/dns/
- API package reference: `azure_domain_api_ecosystem/azure_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
