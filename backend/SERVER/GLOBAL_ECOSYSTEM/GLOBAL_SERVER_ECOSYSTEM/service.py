"""Read-only service facade for GLOBAL SERVER ECOSYSTEM."""

from .registry import list_providers, list_service_types


class EcosystemService:
    """Describe catalog contents without claiming live provider connections."""

    def describe(self) -> dict:
        return {
            "ecosystem": "GLOBAL_SERVER_ECOSYSTEM",
            "providers": list_providers(),
            "service_types": list_service_types(),
            "live_connections_enabled": False,
        }
