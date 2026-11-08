"""Provider-neutral SERVER CORE service layer."""
from __future__ import annotations
from typing import Any
from . import CAPABILITIES, ECOSYSTEM_ID, ECOSYSTEM_NAME
from .models import ServerIdentity
from .policy import SUPPORTED_ENVIRONMENTS, SUPPORTED_SERVER_TYPES
from .registry import ServerCoreRegistry

class ServerCoreService:
    """Owns server identity contracts and local metadata registration only."""
    def __init__(self, registry: ServerCoreRegistry | None = None):
        self.registry = registry or ServerCoreRegistry()

    def describe(self) -> dict[str, Any]:
        return {
            "layer": "CORE",
            "ecosystem_id": ECOSYSTEM_ID,
            "ecosystem": ECOSYSTEM_NAME,
            "capabilities": list(CAPABILITIES),
            "provider_domains": [
                "aws", "google", "microsoft", "cloudflare",
                "digitalocean", "abelohost", "vicetemple",
            ],
            "supported_server_types": list(SUPPORTED_SERVER_TYPES),
            "supported_environments": list(SUPPORTED_ENVIRONMENTS),
            "registered_identities": self.registry.count(),
            "remote_operations_enabled": False,
        }

    def register_identity(self, payload: dict[str, Any]) -> dict[str, Any]:
        try:
            identity = ServerIdentity(**dict(payload))
            return {"success": True, "identity": self.registry.register(identity)}
        except (TypeError, ValueError) as exc:
            return {"success": False, "error": "SERVER_CORE_VALIDATION_FAILED", "message": str(exc)}

    def get_identity(self, server_id: str):
        item = self.registry.get(server_id)
        return {"success": True, "identity": item} if item is not None else None

    def list_identities(self):
        items = self.registry.list()
        return {"success": True, "count": len(items), "identities": items}

    def health(self):
        return {
            "layer": "CORE",
            "ecosystem": ECOSYSTEM_NAME,
            "status": "HEALTHY",
            "registered_identities": self.registry.count(),
            "remote_operations_enabled": False,
        }
