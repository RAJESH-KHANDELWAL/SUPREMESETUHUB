"""Service facade for SERVER inventory and ecosystem metadata."""
from .registry import ServerRegistrationRegistry, list_providers, list_service_types


class EcosystemService:
    """Own local inventory lifecycle; it does not provision remote infrastructure."""
    def __init__(self, registry=None):
        self.registry = registry or ServerRegistrationRegistry()

    def describe(self):
        return {
            "ecosystem": "GLOBAL_SERVER_ECOSYSTEM",
            "providers": list_providers(),
            "service_types": list_service_types(),
            "live_connections_enabled": False,
            "inventory_count": self.registry.count(),
        }

    def status(self):
        return {
            "success": True,
            "ecosystem": "GLOBAL SERVER ECOSYSTEM",
            "status": "FOUNDATION_READY",
            "provider_count": len(list_providers()),
            "service_type_count": len(list_service_types()),
            "registered_servers": self.registry.count(),
            "live_connections_enabled": False,
        }

    def register_server(self, **server):
        try:
            return {"success": True, "server": self.registry.register(server)}
        except (TypeError, ValueError) as exc:
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
        item = self.registry.update(server_id, authorized=True, status="AUTHORIZED")
        if item is None:
            return {"success": False, "error": "SERVER_NOT_FOUND", "server_id": server_id}
        return {"success": True, "server": item}

    def disable_server(self, server_id):
        item = self.registry.update(server_id, enabled=False, status="DISABLED")
        if item is None:
            return {"success": False, "error": "SERVER_NOT_FOUND", "server_id": server_id}
        return {"success": True, "server": item}

    def health(self):
        return {
            "system": "GLOBAL SERVER ECOSYSTEM inventory",
            "health": "HEALTHY",
            "registered_servers": self.registry.count(),
            "live_provider_connections_verified": False,
        }
