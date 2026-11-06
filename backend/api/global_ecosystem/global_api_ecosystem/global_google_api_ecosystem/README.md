# GLOBAL GOOGLE API ECOSYSTEM

Canonical provider root for Google-owned APIs and products in SUPREMESETUHUB.

## Architecture

```text
global_google_api_ecosystem/
├── google_api_ecosystem.py
├── README.md
├── gmail_api_ecosystem/
├── drive_api_ecosystem/
├── calendar_api_ecosystem/
├── contacts_api_ecosystem/
├── sheets_api_ecosystem/
├── docs_api_ecosystem/
├── slides_api_ecosystem/
├── forms_api_ecosystem/
├── chat_api_ecosystem/
├── meet_api_ecosystem/
├── admin_sdk_api_ecosystem/
├── people_api_ecosystem/
├── youtube_api_ecosystem/
├── maps_platform_api_ecosystem/
├── business_profile_api_ecosystem/
├── ads_api_ecosystem/
├── analytics_api_ecosystem/
├── search_console_api_ecosystem/
├── cloud_api_ecosystem/
├── firebase_api_ecosystem/
└── identity_oauth_api_ecosystem/
```

## Rules
- Google provider catalog is the canonical parent; each child owns its API-family catalog and adapter.
- Do not duplicate a Google API in unrelated provider roots. Cross-ecosystem links should be references, not copies.
- Verify official Google API support, availability, scopes, quotas and terms before implementing live integrations.
- Credentials/tokens belong in environment variables or a managed secret store, never in Git.
- Catalog presence is not a live connection. Only successful deployment-level authorization and API tests can mark an adapter connected.
- ChatGPT-connected Google accounts, GitHub OAuth and backend Google OAuth are separate permission grants.

## Gmail
The Gmail adapter is in `gmail_api_ecosystem/` and uses OAuth 2.0 with the least-privilege send scope. Live sending remains unverified until the deployment owner configures Google Cloud OAuth and consents to the mailbox.
