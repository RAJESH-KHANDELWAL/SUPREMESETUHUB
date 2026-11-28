"""Discord provider metadata; catalog presence is not a live integration."""
PROVIDER = {
    "id": "discord",
    "name": "Discord",
    "origin": "global",
    "scope": "Community servers, messaging, events and bot interactions",
    "authentication": "Bot token",
    "credential_env": "DISCORD_BOT_TOKEN",
    "integration_status": "scaffold",
    "live_connection_verified": False,
}

__all__ = ["PROVIDER"]
