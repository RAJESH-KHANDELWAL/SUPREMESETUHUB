# SLACK CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/slack_core_ecosystem/`

## Responsibility
Slack provider Core control plane for product identity, tenant contracts, capability inventory, domain classification, policy boundaries, lifecycle and readiness. It does not install apps or call Slack APIs.

## Shared architecture
- `manager.py`: canonical Python entry point.
- `catalog.py`, `product_catalog.py`, `domain_catalog.py`: provider, product and domain inventories.
- `contracts.py`: tenant, opaque secret-reference and result contracts.
- `policy.py`: capability classification, tenant validation and secret filtering.
- `module_service.py`: shared product service.
- `orchestrator.py`, `service.py`: discovery, dependency metadata and status.
- `manager.php` and `slack_php_core_ecosystem/SlackCoreContract.php`: PHP interoperability only.
- `ecosystem_manifest.json`: machine-readable inventory.

## Product packages
- `slack_admin_core_ecosystem/`: Workspace administration and policy metadata.
- `slack_bookmarks_core_ecosystem/`: Bookmark discovery and lifecycle metadata.
- `slack_canvases_core_ecosystem/`: Canvas collaboration content metadata.
- `slack_conversations_core_ecosystem/`: Channels, direct messages and membership metadata.
- `slack_events_core_ecosystem/`: Event subscription and delivery lifecycle metadata.
- `slack_files_core_ecosystem/`: File discovery, sharing and lifecycle metadata.
- `slack_lists_core_ecosystem/`: Lists, records and fields metadata.
- `slack_messages_core_ecosystem/`: Messages, threads and lifecycle metadata.
- `slack_oauth_core_ecosystem/`: OAuth installation and scope metadata only.
- `slack_reactions_core_ecosystem/`: Emoji reaction lifecycle metadata.
- `slack_search_core_ecosystem/`: Search capability and query classification metadata.
- `slack_users_core_ecosystem/`: User, profile and presence metadata.
- `slack_webhooks_core_ecosystem/`: Webhook subscription and delivery metadata.
- `slack_workflow_core_ecosystem/`: Workflow, trigger and automation lifecycle metadata.

Each product package contains only `__init__.py` and its product-specific `manager.py`; shared behavior is centralized to avoid duplicated code.

## Security and integration boundaries
OAuth installation/token exchange, Slack Web API and Events API transport, webhook signature verification, durable event delivery, file/message operations, background jobs and UI belong in API, security, storage, runtime and application layers. Use authenticated tenant identity, least-privilege scopes, encrypted external secret storage, request-signature verification, replay protection, idempotent event processing, audit logs and explicit authorization for sensitive actions. Catalog registration is not proof of app installation, granted scopes, workspace entitlement or live connectivity.
