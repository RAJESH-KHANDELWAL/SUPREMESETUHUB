"""Global connection orchestration service."""

from .models import ConnectionRequest
from .policies import validate_connection_request


class GlobalConnectionService:
    def __init__(self, manager=None, adapters=None):
        from ...manager import ConnectionManager
        self.manager = manager or ConnectionManager()
        self.adapters = dict(adapters or {})

    def register(self, request):
        errors = validate_connection_request(request)
        if errors:
            return {"success": False, "errors": list(errors)}
        return self.manager.register(
            request.connection_id, request.provider_id, request.server_id,
            request.connection_type, request.protocol, request.endpoint,
            namespace=request.namespace,
        )

    def authorize(self, connection_id, approved=False):
        if not approved:
            return {"success": False, "error": "APPROVAL_REQUIRED"}
        return self.manager.authorize(connection_id)

    def connect(self, connection_id, adapter_key):
        connection = self.manager.connections.get(connection_id)
        if connection is None:
            return {"success": False, "error": "CONNECTION_NOT_FOUND"}
        if not connection.authorized or not connection.enabled:
            return {"success": False, "error": "CONNECTION_NOT_READY"}
        adapter = self.adapters.get(adapter_key)
        if adapter is None:
            return {"success": False, "error": "CONNECTION_ADAPTER_NOT_CONFIGURED"}
        result = adapter.connect(connection)
        if not isinstance(result, dict) or not result.get("success"):
            return {"success": False, "error": "ADAPTER_CONNECT_FAILED"}
        connection.status = "CONNECTED"
        connection.error = None
        return {"success": True, "connection": connection.__dict__}

    def disconnect(self, connection_id, adapter_key):
        connection = self.manager.connections.get(connection_id)
        if connection is None:
            return {"success": False, "error": "CONNECTION_NOT_FOUND"}
        adapter = self.adapters.get(adapter_key)
        if adapter is None:
            return {"success": False, "error": "CONNECTION_ADAPTER_NOT_CONFIGURED"}
        result = adapter.disconnect(connection)
        if not isinstance(result, dict) or not result.get("success"):
            return {"success": False, "error": "ADAPTER_DISCONNECT_FAILED"}
        connection.status = "DISCONNECTED"
        return {"success": True, "connection": connection.__dict__}

    def diagnostics(self):
        health = self.manager.health()
        return {
            "system": "Global Connection Ecosystem",
            "registered_connections": health["registered_connections"],
            "connected": health["connected"],
            "configured_adapters": sorted(self.adapters),
            "adapter_configuration": "configured" if self.adapters else "not_configured",
            "live_provider_connectivity": "not_verified",
        }
