# IBM NS1 Connect Domain Core

Provider identity and metadata contracts for IBM NS1 Connect within Global Domain Core.

- Provider ID: `ns1`
- Source scope: DNS traffic steering API
- Official reference: https://ns1.com/api
- API package reference: `ns1_domain_api_ecosystem/ns1_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
