# Google Cloud DNS Domain Core

Provider identity and metadata contracts for Google Cloud DNS within Global Domain Core.

- Provider ID: `google_cloud`
- Source scope: Managed DNS zones and records
- Official reference: https://cloud.google.com/dns/docs/reference/v1
- API package reference: `google_cloud_domain_api_ecosystem/google_cloud_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
