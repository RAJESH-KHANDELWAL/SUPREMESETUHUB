# GOOGLE ENGINE

**Layer:** `backend/engines/global_ecosystem/google_engine/`  
**Core parent:** `GOOGLE CORE ECOSYSTEM`

This engine package registers and manages Google provider engine metadata. It is not a second Google API client layer.

## Boundaries

- Core ecosystem: `backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/`
- Google API catalogs and adapters: `backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/`
- Existing Google core contracts: `backend/google/google_ecosystem/core/`

## Included engines

The registry derives its initial Google family engine entries from the Google Core catalog, including Gmail, Drive, Calendar, People, Gemini, and Vertex AI. New Google families should be introduced in the core catalog first, then receive an engine entry and tests.

The manager and registry are metadata/orchestration components only. They do not connect to Google, retain credentials, or claim live API status.


## Current Google API family coverage

The Google Core catalog is the source of truth for engine registrations. It covers Gmail, Drive, Calendar, Contacts, Docs, Sheets, Slides, Forms, Chat, Meet, Admin SDK, People, YouTube, Maps Platform, Business Profile, Ads, Analytics, Search Console, Cloud, Firebase, Gemini and Vertex AI.
