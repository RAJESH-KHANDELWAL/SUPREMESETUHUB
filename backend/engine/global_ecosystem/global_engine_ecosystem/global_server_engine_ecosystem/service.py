"""SERVER domain service: inventory boundary and cross-layer status.

SERVER owns the canonical provider/service catalog and current inventory
contract. CORE validates identity contracts, ENGINE owns remote provider
execution, DATABASE owns durable records, and STORAGE owns artifacts.
"""
from .registry import ServerRegistrationRegistry, list_providers, list_service_types


class EcosystemService:
    def __init__(self, registry=None):
        self.registry = registry or ServerRegistrationRegistry()

    def describe(self):
        return {
            "layer": "SERVER",
            "ecosystem": "GLOBAL_SERVER_ECOSYSTEM",
            "providers": list_providers(),
            "service_types": list_service_types(),
            "inventory_backend": "IN_MEMORY_REFERENCE_ADAPTER",
            "durable_persistence_enabled": False,
            "live_connections_enabled": False,
        }

    def status(self):
        return {
            "success": True,
            "layer": "SERVER",
            "ecosystem": "GLOBAL SERVER ECOSYSTEM",
            "status": "FOUNDATION_READY",
            "provider_count": len(list_providers()),
            "service_type_count": len(list_service_types()),
            "registered_servers": self.registry.count(),
            "durable_persistence_enabled": False,
            "live_connections_enabled": False,
        }

    def register_server(self, **server):
        try:
            return {"success": True, "server": self.registry.register(server)}
        except (TypeError, ValueError, AttributeError) as exc:
            return {"success": False, "error": "SERVER_REGISTRATION_FAILED", "message": str(exc)}

    def get_server(self, server_id):
        item = self.registry.get(server_id)
        if item is None:
            return {"success": False, "error": "SERVER_NOT_FOUND", "server_id": server_id}
        return {"success": True, "server": item}

    def list_servers(self):
        items = self.registry.list()
        return {"success": True, "count": len(items), "servers": items}

    def authorize_server(self, server_id):
        """Set a local metadata flag; this does not authenticate to a provider."""
        item = self.registry.update(server_id, authorized=True, status="AUTHORIZED")
        if item is None:
            return {"success": False, "error": "SERVER_NOT_FOUND", "server_id": server_id}
        return {"success": True, "server": item}

    def disable_server(self, server_id):
        """Disable local inventory metadata; this does not stop remote compute."""
        item = self.registry.update(server_id, enabled=False, status="DISABLED")
        if item is None:
            return {"success": False, "error": "SERVER_NOT_FOUND", "server_id": server_id}
        return {"success": True, "server": item}

    def health(self):
        return {
            "layer": "SERVER",
            "system": "GLOBAL SERVER ECOSYSTEM inventory",
            "health": "HEALTHY",
            "registered_servers": self.registry.count(),
            "live_provider_connections_verified": False,
            "durable_persistence_verified": False,
        }
