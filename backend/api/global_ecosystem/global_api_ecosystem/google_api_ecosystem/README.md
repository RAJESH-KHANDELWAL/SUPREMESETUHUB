# GOOGLE API ECOSYSTEM

Canonical provider root for Google-owned APIs and products in SUPREMESETUHUB.

## Architecture

```text
google_api_ecosystem/
├── google_api_ecosystem.py
├── README.md
├── google_gmail_api_ecosystem/
├── google_drive_api_ecosystem/
├── google_calendar_api_ecosystem/
├── google_contacts_api_ecosystem/
├── google_sheets_api_ecosystem/
├── google_docs_api_ecosystem/
├── google_slides_api_ecosystem/
├── google_forms_api_ecosystem/
├── google_chat_api_ecosystem/
├── google_meet_api_ecosystem/
├── google_admin_sdk_api_ecosystem/
├── google_people_api_ecosystem/
├── google_youtube_api_ecosystem/
├── google_maps_platform_api_ecosystem/
├── google_business_profile_api_ecosystem/
├── google_ads_api_ecosystem/
├── google_analytics_api_ecosystem/
├── google_search_console_api_ecosystem/
├── google_cloud_api_ecosystem/
├── google_firebase_api_ecosystem/
└── google_identity_oauth_api_ecosystem/
```

## Rules
- Google provider catalog is the canonical parent; each child owns its API-family catalog and adapter.
- Do not duplicate a Google API in unrelated provider roots. Cross-ecosystem links should be references, not copies.
- Verify official Google API support, availability, scopes, quotas and terms before implementing live integrations.
- Credentials/tokens belong in environment variables or a managed secret store, never in Git.
- Catalog presence is not a live connection. Only successful deployment-level authorization and API tests can mark an adapter connected.
- ChatGPT-connected Google accounts, GitHub OAuth and backend Google OAuth are separate permission grants.

## Gmail
The Gmail adapter is in `google_gmail_api_ecosystem/` and uses OAuth 2.0 with the least-privilege send scope. Live sending remains unverified until the deployment owner configures Google Cloud OAuth and consents to the mailbox.


## Gemini
The dedicated `google_gemini_api_ecosystem/` child provides a Google Gen AI SDK adapter scaffold for Gemini Developer API key validation and explicit generation calls. It supports per-request BYOK or a deployment-managed key. It does not persist per-user credentials or claim a durable connection; production multi-user connection storage requires an encrypted, user-scoped secret store, authenticated routes, quotas, and revocation.
