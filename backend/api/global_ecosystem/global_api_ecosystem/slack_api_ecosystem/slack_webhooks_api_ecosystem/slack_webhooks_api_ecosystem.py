"""Webhooks Slack service-family catalog; not a live API adapter."""
from __future__ import annotations

SLACK_SERVICE_ECOSYSTEM = {
    "provider_id": "slack",
    "name": "SLACK WEBHOOKS API ECOSYSTEM",
    "service_id": "webhooks",
    "scope": "Incoming and outgoing webhook surfaces and request validation.",
    "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/slack_api_ecosystem",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "documentation": "https://api.slack.com/web",
}

__all__ = ["SLACK_SERVICE_ECOSYSTEM"]
