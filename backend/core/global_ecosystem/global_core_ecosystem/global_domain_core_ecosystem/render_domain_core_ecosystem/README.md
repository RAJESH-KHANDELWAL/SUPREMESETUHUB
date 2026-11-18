# Render Domain Core

Provider identity and metadata contracts for Render within Global Domain Core.

- Provider ID: `render`
- Source scope: Custom domains for services
- Official reference: https://docs.render.com/api
- API package reference: `render_domain_api_ecosystem/render_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
