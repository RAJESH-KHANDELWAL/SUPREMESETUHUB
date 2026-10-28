# GOOGLE API ECOSYSTEM

This is the provider-owned Google ecosystem within GLOBAL API ECOSYSTEM. It groups Google's company identity, official platforms, products, developer APIs and service families under one provider boundary. Shared family folders (AI, Cloud, Storage, Communication, etc.) remain separate; this directory is the Google-specific index and integration boundary.

## Google-owned / Google-operated areas
- **Platforms:** Google Workspace, Google Play, Google Cloud Console, Google Maps Platform, Google Search Console, Google Analytics.
- **API families:** Google Identity/OAuth, Gmail, Calendar, Drive, Sheets, Docs, People, Maps Platform, Analytics, Search Console, YouTube Data API, Cloud APIs, Firebase APIs, Vertex AI/Gemini APIs.
- **Cloud products:** Compute Engine, Cloud Run, Cloud Storage, Cloud SQL, Firestore, BigQuery, Pub/Sub, Cloud DNS, IAM and monitoring APIs.
- **Developer ecosystem:** Google Cloud SDK, client libraries, OAuth consent/configuration, API enablement and quotas.
- **Business and identity:** Google Workspace administration and identity-related APIs where authorized.

## Integration rules
1. This file is a catalog/architecture boundary, not proof that APIs are connected.
2. Each API must be enabled for the correct Google Cloud project, requested scopes must be minimal, and OAuth/service-account authorization must be verified.
3. Store credentials in environment variables or a managed secret store, never in Git.
4. Check each API's current availability, terms, quota and region support before enabling it.
5. Do not treat Google as a generic domain registrar or general-purpose hosting provider; map only official products that actually support the requested operation.

## Canonical cross-links
- Provider adapter: `backend/integrations/providers/google.py`
- Central registry: `backend/api/global_api_ecosystem_catalog.py`
- Related platform index: `../global_platforms_api_ecosystem/`
- Related families: AI, Cloud, Communication, Database, Developer, DNS, Security, Storage, Web and Website.
