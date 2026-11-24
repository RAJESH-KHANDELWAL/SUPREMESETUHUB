"""Lists Slack service-family catalog; not a live API adapter."""
from __future__ import annotations

SLACK_SERVICE_ECOSYSTEM = {
    "provider_id": "slack",
    "name": "SLACK LISTS API ECOSYSTEM",
    "service_id": "lists",
    "scope": "Slack Lists resources and item operations.",
    "parent_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/slack_api_ecosystem",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "documentation": "https://api.slack.com/web",
}

__all__ = ["SLACK_SERVICE_ECOSYSTEM"]
