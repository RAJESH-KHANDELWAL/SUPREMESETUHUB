"""Slack provider metadata; catalog presence is not a live integration."""
PROVIDER = {
    "id": "slack",
    "name": "Slack",
    "origin": "global",
    "scope": "Team messaging, channels, workflows and collaboration",
    "authentication": "OAuth 2.0 bot token",
    "credential_env": "SLACK_BOT_TOKEN",
    "integration_status": "scaffold",
    "live_connection_verified": False,
}

__all__ = ["PROVIDER"]
