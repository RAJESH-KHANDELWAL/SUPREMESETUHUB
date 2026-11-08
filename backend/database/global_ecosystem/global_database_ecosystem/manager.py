"""Independent GLOBAL DATABASE manager.

Owns provider discovery and database metadata only. It does not import or
delegate to API, CORE, or ENGINE layers and does not open network connections.
"""
from .catalog import get_catalog
from .registry import GlobalDatabaseEcosystemRegistry

class GlobalDatabaseEcosystemManager:
    def __init__(self):
        self.catalog = get_catalog()
        self.registry = GlobalDatabaseEcosystemRegistry()

    def status(self):
        providers = self.registry.list_providers()
        configured = sum(
            1 for item in providers
            if item.get("connection_status") == "connected"
        )
        return {
            **self.catalog,
            "provider_count": len(providers),
            "configured_provider_count": configured,
            "providers": providers,
            "status": "CATALOG_READY",
            "live_connections_verified": False,
        }

    def list_providers(self):
        return self.registry.list_providers()

    def get_provider(self, provider_id):
        return self.registry.get_provider(provider_id)
