"""MAIN BASE FOUNDATION connection manager."""

from typing import Dict

from .models import Connection


class ConnectionManager:
    """Manage registered provider and server connection state."""

    def __init__(self):
        self.connections: Dict[str, Connection] = {}

    def register(
        self,
        connection_id: str,
        provider_id: str,
        server_id: str,
        connection_type: str,
        protocol: str,
        endpoint: str | None = None,
        namespace: str = "global",
    ) -> dict:
        """Register connection metadata without opening a network connection."""
        if connection_id in self.connections:
            return {"success": False, "error": "CONNECTION_ID_ALREADY_EXISTS", "connection_id": connection_id}

        connection = Connection(
            connection_id=connection_id,
            provider_id=provider_id,
            server_id=server_id,
            connection_type=connection_type,
            protocol=protocol,
            endpoint=endpoint,
            namespace=namespace,
        )
        self.connections[connection_id] = connection
        return {"success": True, "connection": connection.__dict__}

    def get(self, connection_id: str) -> dict:
        connection = self.connections.get(connection_id)
        if connection is None:
            return {"success": False, "error": "CONNECTION_NOT_FOUND", "connection_id": connection_id}
        return {"success": True, "connection": connection.__dict__}

    def list(self) -> dict:
        return {"success": True, "count": len(self.connections), "connections": [item.__dict__ for item in self.connections.values()]}

    def authorize(self, connection_id: str) -> dict:
        connection = self.connections.get(connection_id)
        if connection is None:
            return {"success": False, "error": "CONNECTION_NOT_FOUND"}
        connection.authorized = True
        connection.status = "AUTHORIZED"
        connection.error = None
        return {"success": True, "connection": connection.__dict__}

    def connect(self, connection_id: str) -> dict:
        """Set legacy in-memory state only; use ecosystem adapters for real I/O."""
        connection = self.connections.get(connection_id)
        if connection is None:
            return {"success": False, "error": "CONNECTION_NOT_FOUND"}
        if not connection.authorized:
            return {"success": False, "error": "CONNECTION_NOT_AUTHORIZED", "connection_id": connection_id}
        if not connection.enabled:
            return {"success": False, "error": "CONNECTION_DISABLED", "connection_id": connection_id}
        connection.status = "CONNECTED"
        connection.error = None
        return {"success": True, "connection": connection.__dict__}

    def disconnect(self, connection_id: str) -> dict:
        connection = self.connections.get(connection_id)
        if connection is None:
            return {"success": False, "error": "CONNECTION_NOT_FOUND"}
        connection.status = "DISCONNECTED"
        return {"success": True, "connection": connection.__dict__}

    def disable(self, connection_id: str) -> dict:
        connection = self.connections.get(connection_id)
        if connection is None:
            return {"success": False, "error": "CONNECTION_NOT_FOUND"}
        connection.enabled = False
        connection.status = "DISABLED"
        return {"success": True, "connection": connection.__dict__}

    def health(self) -> dict:
        connected = sum(1 for item in self.connections.values() if item.status == "CONNECTED")
        return {
            "system": "Connection Manager",
            "health": "HEALTHY",
            "registered_connections": len(self.connections),
            "connected": connected,
        }
