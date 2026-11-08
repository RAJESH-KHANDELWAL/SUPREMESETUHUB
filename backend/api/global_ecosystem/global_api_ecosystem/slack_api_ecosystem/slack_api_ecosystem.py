"""Slack provider API ecosystem catalog and service-family registry.

Metadata only. Catalog entries do not imply a Slack app, workspace installation,
granted OAuth scopes, credentials, or live API connectivity.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

PROVIDER_ID = "slack"
PROVIDER_NAME = "SLACK API ECOSYSTEM"
PROVIDER_VENDOR = "Slack"
PROVIDER_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/slack_api_ecosystem"

SLACK_SERVICE_ECOSYSTEMS = [
    {"id": "oauth", "name": "SLACK OAUTH API ECOSYSTEM", "folder": "slack_oauth_api_ecosystem", "status": "catalog_only"},
    {"id": "users", "name": "SLACK USERS API ECOSYSTEM", "folder": "slack_users_api_ecosystem", "status": "catalog_only"},
    {"id": "conversations", "name": "SLACK CONVERSATIONS API ECOSYSTEM", "folder": "slack_conversations_api_ecosystem", "status": "catalog_only"},
    {"id": "messages", "name": "SLACK MESSAGES API ECOSYSTEM", "folder": "slack_messages_api_ecosystem", "status": "catalog_only"},
    {"id": "files", "name": "SLACK FILES API ECOSYSTEM", "folder": "slack_files_api_ecosystem", "status": "catalog_only"},
    {"id": "events", "name": "SLACK EVENTS API ECOSYSTEM", "folder": "slack_events_api_ecosystem", "status": "catalog_only"},
    {"id": "webhooks", "name": "SLACK WEBHOOKS API ECOSYSTEM", "folder": "slack_webhooks_api_ecosystem", "status": "catalog_only"},
    {"id": "reactions", "name": "SLACK REACTIONS API ECOSYSTEM", "folder": "slack_reactions_api_ecosystem", "status": "catalog_only"},
    {"id": "search", "name": "SLACK SEARCH API ECOSYSTEM", "folder": "slack_search_api_ecosystem", "status": "catalog_only"},
    {"id": "workflow", "name": "SLACK WORKFLOW API ECOSYSTEM", "folder": "slack_workflow_api_ecosystem", "status": "catalog_only"},
    {"id": "admin", "name": "SLACK ADMIN API ECOSYSTEM", "folder": "slack_admin_api_ecosystem", "status": "catalog_only"},
    {"id": "canvases", "name": "SLACK CANVASES API ECOSYSTEM", "folder": "slack_canvases_api_ecosystem", "status": "catalog_only"},
    {"id": "lists", "name": "SLACK LISTS API ECOSYSTEM", "folder": "slack_lists_api_ecosystem", "status": "catalog_only"},
    {"id": "bookmarks", "name": "SLACK BOOKMARKS API ECOSYSTEM", "folder": "slack_bookmarks_api_ecosystem", "status": "catalog_only"},
]

PROVIDER_API_ECOSYSTEM: dict[str, Any] = {
    "provider_id": PROVIDER_ID,
    "name": PROVIDER_NAME,
    "vendor": PROVIDER_VENDOR,
    "families": ["COMMUNICATION", "BUSINESS"],
    "scope": "Workspace, messaging, events, users, files, workflow and app APIs subject to workspace installation, granted OAuth scopes and plan availability.",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_EXPANDED_LIVE_API_UNVERIFIED",
    "live_connection_verified": False,
    "provider_catalog_path": PROVIDER_CATALOG_PATH,
    "authentication": {
        "method": "SLACK_OAUTH_V2",
        "credential_source": "environment_or_managed_secret_store",
        "required_environment": ["SLACK_CLIENT_ID", "SLACK_CLIENT_SECRET"],
        "bot_token_environment": "SLACK_BOT_TOKEN",
        "signing_secret_environment": "SLACK_SIGNING_SECRET",
        "secrets_in_repository": False,
    },
    "endpoint_strategy": {
        "web_api_base_url": "https://slack.com/api",
        "oauth_v2_authorize_url": "https://slack.com/oauth/v2/authorize",
        "oauth_v2_access_url": "https://slack.com/api/oauth.v2.access",
        "environment_selection": "explicit_workspace_installation",
    },
    "service_ecosystems": SLACK_SERVICE_ECOSYSTEMS,
    "integration_requirements": [
        "official_api_reference_review",
        "oauth_state_validation_and_secure_callback",
        "least_privilege_scope_review",
        "workspace_and_team_identity_validation",
        "request_signature_verification_for_events",
        "event_retry_and_idempotency_handling",
        "rate_limit_retry_after_handling",
        "pagination_and_cursor_handling",
        "timeouts_retries_and_error_normalization",
        "unit_tests_with_mocked_responses",
        "opt_in_workspace_sandbox_integration_tests",
    ],
    "security": {
        "never_log_bot_tokens_or_client_secrets": True,
        "verify_request_signatures": True,
        "use_least_privilege_scopes": True,
        "live_connection_requires_successful_authenticated_workspace_api_test": True,
    },
    "documentation": [
        "https://api.slack.com/web",
        "https://api.slack.com/authentication/oauth-v2",
        "https://api.slack.com/apis/events-api",
        "https://api.slack.com/apis/connections",
    ],
}

SLACK_API_ECOSYSTEM = PROVIDER_API_ECOSYSTEM

def get_slack_api_ecosystem() -> dict[str, Any]:
    """Return an isolated copy of Slack provider metadata."""
    return deepcopy(PROVIDER_API_ECOSYSTEM)

def list_slack_api_ecosystems() -> dict[str, object]:
    """List Slack service-family catalogs without claiming live connectivity."""
    children = [dict(item) for item in SLACK_SERVICE_ECOSYSTEMS]
    return {
        "success": True,
        "provider": PROVIDER_NAME,
        "status": PROVIDER_API_ECOSYSTEM["status"],
        "live_connection_verified": False,
        "count": len(children),
        "ecosystems": children,
    }

__all__ = [
    "PROVIDER_ID", "PROVIDER_NAME", "PROVIDER_VENDOR", "PROVIDER_CATALOG_PATH",
    "PROVIDER_API_ECOSYSTEM", "SLACK_API_ECOSYSTEM", "SLACK_SERVICE_ECOSYSTEMS",
    "get_slack_api_ecosystem", "list_slack_api_ecosystems",
]
