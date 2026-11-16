# Vercel Domain Core

Provider identity and metadata contracts for Vercel within Global Domain Core.

- Provider ID: `vercel`
- Source scope: Project domain configuration
- Official reference: https://vercel.com/docs/rest-api
- API package reference: `vercel_domain_api_ecosystem/vercel_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
