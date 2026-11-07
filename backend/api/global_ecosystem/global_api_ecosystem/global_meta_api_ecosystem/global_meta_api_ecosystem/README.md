# META API ECOSYSTEM

Canonical provider root for Meta-owned developer APIs and platform integrations in SUPREMESETUHUB.

## Provider structure

- `meta_api_ecosystem.py` — provider registry, service-family metadata and safe catalog listing.
- Each `meta_*_api_ecosystem/` child directory owns its service-family catalog and future adapter boundary.
- Shared integration adapter target: `backend/integrations/providers/meta.py` (verify implementation before registering).
- Provider credentials must be handled by the shared integration and tenant-secret infrastructure; do not create a second credential store here.

## Meta API family tree

- **Meta Graph API** — `meta_graph_api_ecosystem/` — Core Graph API concepts, versioning, nodes, edges, fields, permissions, paging and error handling.
- **Facebook Pages API** — `meta_facebook_pages_api_ecosystem/` — Page discovery and supported Page management, publishing and insights subject to permissions.
- **Instagram API** — `meta_instagram_api_ecosystem/` — Instagram professional-account content publishing, comments, mentions, insights and messaging capabilities where supported.
- **WhatsApp Business Platform API** — `meta_whatsapp_business_api_ecosystem/` — Cloud API messaging, templates, phone numbers, business profiles and webhook events.
- **Messenger Platform API** — `meta_messenger_api_ecosystem/` — Page-linked Messenger conversations, send/receive workflows, policy constraints and webhooks.
- **Threads API** — `meta_threads_api_ecosystem/` — Threads publishing, replies, discovery and insights capabilities where available.
- **Marketing and Ads API** — `meta_marketing_ads_api_ecosystem/` — Marketing API, ad accounts, campaigns, insights and business-level authorization.
- **Login and Identity API** — `meta_login_identity_api_ecosystem/` — Facebook Login, supported Login products, OAuth authorization and identity permissions.
- **Business Management API** — `meta_business_management_api_ecosystem/` — Business Portfolio assets, system users, partner access and business asset assignments.
- **Webhooks API** — `meta_webhooks_api_ecosystem/` — Subscription configuration, callback verification, event validation, retries and signature checks.
- **SDK and Developer Tools** — `meta_sdk_developer_tools_ecosystem/` — Official SDKs, app configuration, Graph API Explorer and developer tooling references.
- **Meta AI** — `meta_ai_ecosystem/` — Discovery/reference boundary only. Do not imply a generally available public Meta AI API unless an official supported API and entitlement are verified.

## End-user connection target

The platform should own OAuth routes, callback validation, provider permissions, backend adapters, webhook endpoints, health checks and encrypted tenant-scoped credential storage.

The end user should only:
1. Choose the Meta service they want to connect.
2. Start the official Meta authorization or app connection flow.
3. Review and grant the required permissions.
4. Select an eligible Page, Instagram professional account, WhatsApp Business account or other supported asset where the product requires it.
5. Complete connection and see a truthful verification result.

Do not ask users to paste long-lived access tokens into ordinary forms. Where an official API-key or system-user credential flow is genuinely required, collect it only through an authenticated, server-side secret-handling flow.

## Authentication and eligibility

Meta integrations are product- and asset-specific. The exact login product, app mode, permissions, App Review, business verification, account type, region and asset ownership can affect availability.

Implementation should:
- Use the official OAuth authorization-code flow and validate state, redirect URI and callback ownership.
- Request only the permissions required for the selected use case.
- Keep tokens server-side in encrypted tenant-scoped storage.
- Support token expiry, refresh where supported, reauthorization, revocation and disconnect.
- Verify Page, Instagram, WhatsApp and Business Portfolio asset access after authorization.
- Validate webhook challenge requests and signatures before accepting events.
- Enforce tenant authorization, rate limits, bounded retries, request timeouts and audit logs.
- Never log, return, commit or expose access tokens, app secrets or verification secrets.

## Status semantics

- `CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS` means the family catalog exists; no live connection is claimed.
- `NEEDS_CONFIGURATION` means required server-side application configuration is absent.
- `CONFIGURED_NOT_VERIFIED` means configuration is present but an authenticated provider operation has not succeeded.
- `CONNECTED_VERIFIED` may be used only after a tenant-scoped authorization and a suitable service-specific smoke test succeeds.

Folder presence, OAuth configuration or a successful health endpoint alone is not proof that a Meta API operation is authorized or working.

## Non-duplication rule

Meta-owned services remain canonical under this provider root. Global AI, Communication, Social Media, Security, Developer and Business ecosystems should reference these canonical service-family catalogs rather than duplicate Meta-specific implementations. Other companies' products and third-party messaging providers must remain in their own provider roots.
