"""Microsoft Teams service-family metadata; catalog scaffold, not a live connector."""
from __future__ import annotations

SERVICE_ECOSYSTEM = {
    "provider_id": "microsoft",
    "service_id": "microsoft_teams_api",
    "name": "MICROSOFT TEAMS API ECOSYSTEM",
    "scope": "Teams, channels, chats, messages, memberships, and meeting resources.",
    "authentication_setup": "Graph Teams/Chat/Channel permissions; application access policies where required.",
    "documentation_required": True,
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}

__all__ = ["SERVICE_ECOSYSTEM"]
