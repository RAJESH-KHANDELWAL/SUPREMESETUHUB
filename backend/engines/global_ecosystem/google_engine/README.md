# GOOGLE ENGINE

**Layer:** `backend/engines/global_ecosystem/google_engine/`  
**Core parent:** `GOOGLE CORE ECOSYSTEM`

This provider engine package registers and manages Google engine metadata. It is not a second Google API client layer.

## Layer boundaries

- Google Core Ecosystem: `backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/`
- Google API catalogs and adapters: `backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/`
- Existing shared Google core contracts: `backend/google/google_ecosystem/core/`

## Engine coverage

The Google Engine registry derives entries from all 23 Google Core child modules: Gmail, Drive, Calendar, Contacts, People, Docs, Sheets, Slides, Forms, Chat, Meet, Admin SDK, Identity & OAuth, YouTube, Maps Platform, Business Profile, Ads, Analytics, Search Console, Cloud, Firebase, Gemini and Vertex AI.

The Gmail Engine has a runtime facade and delegates to Gmail Core and the existing Gmail API adapter. The other family engine entries are metadata/catalog registrations only until their family-specific runtime adapters and tests are implemented.

The Google engine manager and registry do not connect to Google, retain credentials or claim live API status.
