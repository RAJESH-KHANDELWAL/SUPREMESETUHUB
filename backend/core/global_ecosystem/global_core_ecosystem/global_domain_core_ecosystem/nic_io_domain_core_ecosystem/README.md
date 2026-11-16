# NIC.IO Domain Core

Provider identity and metadata contracts for NIC.IO within Global Domain Core.

- Provider ID: `nic_io`
- Source scope: Registry for .io domains
- Official reference: https://nic.io/
- API package reference: `nic_io_domain_api_ecosystem/nic_io_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
