# META CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Provider:** Meta  
**Core root:** `backend/core/global_ecosystem/global_core_ecosystem/meta_core_ecosystem/`  
**API source of truth:** `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_api_ecosystem.py`  
**Status:** `CORE_CATALOG_ONLY`

## Mission and ownership
Meta Core is the provider-level control plane for Meta Graph API, Facebook Pages, Instagram, WhatsApp Business, Messenger, Threads, Marketing/Ads, Business Management, Login/Identity, Webhooks and Meta AI discovery. It owns provider identity, product-family registration, cross-product domain taxonomy, tenant/app/asset context contracts, OAuth/permission policy metadata, readiness, health and dependency discovery.

Core does not perform OAuth code exchange, hold access tokens, call Graph API, deliver messages, publish content, mutate ad accounts, process webhooks or execute jobs. Those belong to the dedicated API, integrations, ENGINE, storage and application layers.

## Product families — sourced from API registry
- **META Graph API** — `meta_graph_core_ecosystem/`; API: `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_graph_api_ecosystem/`; ENGINE: `backend/engine/global_ecosystem/global_engine_ecosystem/meta_engine_ecosystem/meta_graph_engine_ecosystem/`.
- **META Facebook Pages** — `meta_facebook_pages_core_ecosystem/`; API: `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_facebook_pages_api_ecosystem/`; ENGINE: `backend/engine/global_ecosystem/global_engine_ecosystem/meta_engine_ecosystem/meta_facebook_pages_engine_ecosystem/`.
- **META Instagram** — `meta_instagram_core_ecosystem/`; API: `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_instagram_api_ecosystem/`; ENGINE: `backend/engine/global_ecosystem/global_engine_ecosystem/meta_engine_ecosystem/meta_instagram_engine_ecosystem/`.
- **META WhatsApp Business** — `meta_whatsapp_business_core_ecosystem/`; API: `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_whatsapp_business_api_ecosystem/`; ENGINE: `backend/engine/global_ecosystem/global_engine_ecosystem/meta_engine_ecosystem/meta_whatsapp_business_engine_ecosystem/`.
- **META Messenger** — `meta_messenger_core_ecosystem/`; API: `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_messenger_api_ecosystem/`; ENGINE: `backend/engine/global_ecosystem/global_engine_ecosystem/meta_engine_ecosystem/meta_messenger_engine_ecosystem/`.
- **META Threads** — `meta_threads_core_ecosystem/`; API: `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_threads_api_ecosystem/`; ENGINE: `backend/engine/global_ecosystem/global_engine_ecosystem/meta_engine_ecosystem/meta_threads_engine_ecosystem/`.
- **META Marketing and Ads** — `meta_marketing_ads_core_ecosystem/`; API: `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_marketing_ads_api_ecosystem/`; ENGINE: `backend/engine/global_ecosystem/global_engine_ecosystem/meta_engine_ecosystem/meta_marketing_ads_engine_ecosystem/`.
- **META Login and Identity** — `meta_login_identity_core_ecosystem/`; API: `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_login_identity_api_ecosystem/`; ENGINE: `backend/engine/global_ecosystem/global_engine_ecosystem/meta_engine_ecosystem/meta_login_identity_engine_ecosystem/`.
- **META Business Management** — `meta_business_management_core_ecosystem/`; API: `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_business_management_api_ecosystem/`; ENGINE: `backend/engine/global_ecosystem/global_engine_ecosystem/meta_engine_ecosystem/meta_business_management_engine_ecosystem/`.
- **META Webhooks** — `meta_webhooks_core_ecosystem/`; API: `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_webhooks_api_ecosystem/`; ENGINE: `backend/engine/global_ecosystem/global_engine_ecosystem/meta_engine_ecosystem/meta_webhooks_engine_ecosystem/`.
- **META AI Discovery** — `meta_ai_core_ecosystem/`; API: `backend/api/global_ecosystem/global_api_ecosystem/meta_api_ecosystem/meta_ai_ecosystem/`; ENGINE: `backend/engine/global_ecosystem/global_engine_ecosystem/meta_engine_ecosystem/meta_ai_ecosystem/`.

The API registry and Core tree each contain the same 11 product families. Meta AI is discovery/reference only; no generally available public Meta AI API is asserted. SDK and Developer Tools remain outside the canonical family registry until matching API and Core packages are implemented.

## Domain coverage
1. **Provider Governance** — Provider identity, product-family registration, lifecycle, readiness and ownership.
2. **Graph Platform and Object Model** — Graph nodes, edges, fields, object identifiers, API versions, paging and error contracts.
3. **Facebook Pages and Publishing** — Page discovery, Page-owned assets, supported publishing, moderation and Page insights.
4. **Instagram Creator and Professional Accounts** — Professional account discovery, media publishing, comments, mentions and insights subject to eligibility.
5. **WhatsApp Business Messaging** — Business phone numbers, templates, Cloud API messaging, quality and webhook lifecycle.
6. **Messenger Conversations** — Page-linked conversations, send/receive boundaries, event subscriptions and messaging policy.
7. **Threads Social Network** — Threads profiles, publishing, replies, discovery and insights where supported.
8. **Marketing, Advertising and Campaigns** — Ad accounts, campaign/ad metadata, authorization, reporting and billing boundaries.
9. **Business Portfolio and Asset Governance** — Business portfolios, Pages, Instagram accounts, WhatsApp assets, partners, system users and assignments.
10. **Login, OAuth and Identity** — Authorization code flow metadata, redirect/state validation, consent, scopes, token lifecycle and revocation.
11. **Webhook Events and Delivery** — Subscription metadata, callback verification, signatures, event normalization, retries and delivery status.
12. **Meta AI Discovery** — Discovery/reference metadata only; does not claim a generally available public Meta AI API.
13. **Social Content and Publishing** — Cross-product publishing capability metadata, media constraints, permissions and content lifecycle.
14. **Audience Insights and Analytics** — Page, Instagram and advertising insights metadata, reporting scopes and measurement boundaries.
15. **Media and Asset Management** — Business-owned media assets, account associations, media references and asset eligibility.
16. **Privacy and Data Protection** — Personal data minimization, retention, deletion boundaries, consent and data-protection controls.
17. **App Review, Permissions and Compliance** — App mode, permissions, review, business verification, policy compliance and service eligibility.
18. **Tenant, Account and Asset Governance** — Tenant isolation, Meta app/account context, asset ownership, region/product availability and quotas.

## Required root files
- `manager.py`: canonical entry point and `get_manager()`.
- `manager.php`: thin PHP status/interoperability facade.
- `catalog.py`: provider catalog assembled from the canonical Meta API registry.
- `product_catalog.py`: exact API-family-to-Core/ENGINE routing map.
- `domain_catalog.py`: 18 domains with explicit product-family mappings.
- `contracts.py`: tenant, app, business-account, secret-reference, readiness and result contracts.
- `policy.py`: OAuth, permission, privacy, sensitive-operation and secret-redaction guardrails.
- `module_service.py`: shared read-only product-family service.
- `domain_runtime.py`: shared read-only domain manager.
- `orchestrator.py`: product/domain discovery, health and dependency map.
- `service.py`: public status and parent-registry integration.
- `test_meta_core.py`: structural, mapping, policy and master-catalog tests.

## Master catalog alignment (2468)
The master catalog is planning taxonomy, not provider implementation inventory. Existing canonical topics referenced here are `S07_privacy_and_data_protection`, `S09_artificial_intelligence`, `S09_cybersecurity`, `S09_data_analytics`, `S09_digital_identity`, `S11_privacy_law`, `S08_individual_business`, `S08_small_business`, `S08_medium_business`, `S08_digital_business`, `S08_international_business`. These are related-topic mappings only, not new Meta-specific catalog entries. The master JSON remains unchanged.

## OAuth, privacy and safety
- Use official Meta authorization-code flow in the API/integration layer; validate state, redirect URI and callback ownership.
- Request least-privilege permissions. App Review, app mode, business verification, account type, asset ownership, product eligibility and regional availability can constrain features.
- Store access tokens and app secrets only in tenant-scoped encrypted secret infrastructure. Core stores opaque references only.
- Never accept long-lived access tokens in ordinary UI forms, log tokens, expose app secrets or commit credentials.
- Validate webhook challenge and signatures; use idempotency, bounded retries, rate limits, timeouts and audit logs.
- Require explicit user/tenant authorization for publishing, messaging, ad spend, asset assignment, deletion and other sensitive operations.
- A configured app is not a connected account. Mark a connection verified only after tenant-scoped OAuth, permission/asset checks and a service-specific smoke test.
- Meta AI remains discovery-only unless an official supported public API is independently verified and registered.

## Layer boundaries
| Layer | Responsibility |
|---|---|
| Meta Core | Identity, product/domain catalog, contracts, policy, readiness and discovery |
| Meta API | OAuth adapter, Graph API transport, request/response normalization, webhooks |
| Meta ENGINE | Jobs, queues, execution, retries and workflow handlers |
| Integrations / Storage | Tenant secret references, encrypted credentials, persistence and audit |
| Application | User consent, approvals, asset selection and UI |
