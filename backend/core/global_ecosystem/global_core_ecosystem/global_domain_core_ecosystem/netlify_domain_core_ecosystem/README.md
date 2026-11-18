# Netlify Domain Core

Provider identity and metadata contracts for Netlify within Global Domain Core.

- Provider ID: `netlify`
- Source scope: Custom domain management
- Official reference: https://docs.netlify.com/api/get-started/
- API package reference: `netlify_domain_api_ecosystem/netlify_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
