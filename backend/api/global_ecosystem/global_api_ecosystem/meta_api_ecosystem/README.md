# META API ECOSYSTEM

Canonical provider root for Meta-owned developer APIs and platform integrations in SUPREMESETUHUB.

## Provider structure
- `meta_api_ecosystem.py` — provider registry, service-family metadata and safe catalog listing.
- Each `meta_*_api_ecosystem/` child directory owns its service-family catalog and future adapter boundary.
- Shared integration readiness adapter: `backend/integrations/providers/meta.py`, registered in `backend/integrations/registry.py` and exposed in the Global API provider catalog.
- Server-side configuration names: `META_APP_ID`, `META_APP_SECRET`, `META_REDIRECT_URI`. The readiness check only confirms that these values are present; it does not exchange OAuth codes or validate a live API call.
- Provider credentials must use shared integration and tenant-secret infrastructure.

## Meta API family tree
- **Meta Graph API** — `meta_graph_api_ecosystem/`: core objects, nodes, edges, fields, versioning, permissions, paging and errors.
- **Facebook Pages API** — `meta_facebook_pages_api_ecosystem/`: Page discovery, supported Page management, publishing and insights subject to permissions.
- **Instagram API** — `meta_instagram_api_ecosystem/`: professional-account publishing, comments, mentions, insights and supported messaging capabilities.
- **WhatsApp Business Platform API** — `meta_whatsapp_business_api_ecosystem/`: Cloud API messaging, templates, phone numbers, business profiles and webhooks.
- **Messenger Platform API** — `meta_messenger_api_ecosystem/`: Page-linked conversations, send/receive workflows, policy and webhooks.
- **Threads API** — `meta_threads_api_ecosystem/`: publishing, replies, profile access, discovery and insights where available.
- **Marketing and Ads API** — `meta_marketing_ads_api_ecosystem/`: ad accounts, campaigns, ads, insights and business authorization.
- **Login and Identity API** — `meta_login_identity_api_ecosystem/`: Facebook Login, OAuth, callback security and identity permissions.
- **Business Management API** — `meta_business_management_api_ecosystem/`: Business Portfolio assets, system users, partner access and assignments.
- **Webhooks API** — `meta_webhooks_api_ecosystem/`: subscriptions, callback verification, event validation, retries and signatures.
- **SDK and Developer Tools** — `meta_sdk_developer_tools_ecosystem/`: official SDKs, app configuration and developer tooling references.
- **Meta AI** — `meta_ai_ecosystem/`: discovery/reference only; no generally available public Meta AI API is claimed.

## End-user connection target
The platform owns OAuth routes, callback validation, provider adapters, webhook endpoints, health checks and encrypted tenant-scoped credential storage. End users select a service, complete the official Meta authorization flow, grant required permissions, select eligible assets and connect.

Do not ask users to paste long-lived access tokens into ordinary forms. Collect any required credential only through an authenticated server-side secret flow.

## Authentication, eligibility and security
Meta access is product- and asset-specific. Login product, app mode, permissions, App Review, business verification, account type, region and asset ownership can affect availability.

- Use official OAuth authorization-code flows and validate state and redirect URIs.
- Request minimum permissions and verify asset access after authorization.
- Store tokens server-side in encrypted tenant-scoped storage; handle expiry, refresh where supported, reauthorization, revocation and disconnect.
- Validate webhook challenges and signatures.
- Enforce tenant authorization, rate limits, bounded retries, timeouts and audit logs.
- Never log, return, commit or expose access tokens, app secrets or verification secrets.

## Status semantics
- `CONFIGURED_NOT_VERIFIED`: Meta app configuration is present; no live connection is claimed.
- `NEEDS_CONFIGURATION`: one or more required server-side Meta app settings are missing.
- `NEEDS_CONFIGURATION`: required server configuration is absent.
- `CONFIGURED_NOT_VERIFIED`: configuration exists but no authenticated provider operation has succeeded.
- `CONNECTED_VERIFIED`: use only after tenant-scoped authorization and a service-specific smoke test succeeds.

Folder presence or a successful health endpoint alone does not prove a Meta API operation works.

## Non-duplication rule
Meta-owned services remain canonical under this provider root. Global AI, Communication, Social Media, Security, Developer and Business ecosystems reference these catalogs rather than copying Meta implementations.
