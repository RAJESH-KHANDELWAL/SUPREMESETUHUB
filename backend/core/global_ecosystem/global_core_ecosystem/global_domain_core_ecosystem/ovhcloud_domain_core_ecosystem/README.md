# OVHcloud Domain Core

Provider identity and metadata contracts for OVHcloud within Global Domain Core.

- Provider ID: `ovhcloud`
- Source scope: Domain and DNS management APIs
- Official reference: https://eu.api.ovh.com/
- API package reference: `ovhcloud_domain_api_ecosystem/ovhcloud_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
