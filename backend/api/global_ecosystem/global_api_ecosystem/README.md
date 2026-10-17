# GLOBAL API ECOSYSTEM

This directory contains the API-family ecosystems under the GLOBAL API ECOSYSTEM parent. Keep the existing ecosystem packages separate; this index points to their canonical paths rather than copying code.

## API families
AI, App, Business, Cloud, Communication, Companies, Database, Developer, Domain, Freelancer, Hosting, Individual, Integrations, Intimacy, Language, Payment, Platforms, Security, Server, Services, Social Media, Software, Storage, System, Tools, Video, Web and Website.

## Provider ecosystems
The central provider catalog lives in `backend/api/global_api_ecosystem_catalog.py`; its protected FastAPI routes are in `backend/api/global_api_ecosystem_routes.py`. It links Google, Microsoft, AWS and Apple to existing company-specific packages and related platform packages. It also lists other providers by relevant API family without implying those providers are implemented or connected.

## API endpoints
- `GET /api/v1/global-api-ecosystem/status`
- `GET /api/v1/global-api-ecosystem/ecosystems`
- `GET /api/v1/global-api-ecosystem/providers`
- `GET /api/v1/global-api-ecosystem/providers/{provider_id}`
- `GET /api/v1/global-api-ecosystem/ai-providers`

See `docs/GLOBAL_API_ECOSYSTEM_PROVIDER_HIERARCHY.md` for the provider hierarchy, status definitions and integration gates.

The runtime `backend/`, master `BACKEND/`, and visual/documentation `🖥️ BACKEND 🖥️/` layers remain separate. No provider is considered live-connected based on catalog membership alone.
