"""Telegram provider metadata; catalog presence is not a live integration."""
PROVIDER = {
    "id": "telegram",
    "name": "Telegram",
    "origin": "global",
    "scope": "Bots, messaging, channels and group workflows",
    "authentication": "Bot token",
    "credential_env": "TELEGRAM_BOT_TOKEN",
    "integration_status": "scaffold",
    "live_connection_verified": False,
}

__all__ = ["PROVIDER"]
