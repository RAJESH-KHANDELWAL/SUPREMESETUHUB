"""Provider-neutral SERVER CORE service layer."""
from __future__ import annotations
from typing import Any
from .constants import CAPABILITIES, ECOSYSTEM_ID, ECOSYSTEM_NAME
from .models import ServerIdentity
from .policy import SUPPORTED_ENVIRONMENTS, SUPPORTED_SERVER_TYPES
from .registry import ServerCoreRegistry
from .catalog import get_catalog
from .provider_catalog import get_provider
from .orchestrator import ServerCoreOrchestrator

class ServerCoreService:
    """Own server identity contracts and local metadata registration only."""
    def __init__(self, registry: ServerCoreRegistry | None = None):
        self.registry = registry or ServerCoreRegistry()
        self.orchestrator = ServerCoreOrchestrator()

    def describe(self) -> dict[str, Any]:
        return {
            "layer": "CORE", "ecosystem_id": ECOSYSTEM_ID,
            "ecosystem": ECOSYSTEM_NAME, "status": "CORE_CATALOG_ONLY",
            "capabilities": list(CAPABILITIES),
            "provider_domains": [x["provider_id"].lower() for x in get_catalog()["providers"]],
            "provider_count": get_catalog()["provider_count"],
            "supported_server_types": list(SUPPORTED_SERVER_TYPES),
            "supported_environments": list(SUPPORTED_ENVIRONMENTS),
            "registered_identities": self.registry.count(),
            "remote_operations_enabled": False,
            "registry_persistence": "PROCESS_LOCAL_ONLY",
        }

    def catalog(self): return get_catalog()
    def list_providers(self): return self.orchestrator.providers()
    def health(self):
        result = self.orchestrator.health()
        result["catalog_status"] = result["status"]
        result["status"] = "HEALTHY"
        result["registered_identities"] = self.registry.count()
        result["remote_operations_enabled"] = False
        return result
    def dependency_map(self): return self.orchestrator.dependency_map()

    def core_domains(self): return self.orchestrator.domains()
    def get_core_domain(self, domain_id: str): return self.orchestrator.domain(domain_id)
    def master_catalog_alignment(self): return self.orchestrator.master_catalog_alignment()
    def manager_status(self):
        from .manager import get_manager
        return get_manager().status()


    def validate_identity(self, payload: dict[str, Any]) -> dict[str, Any]:
        try:
            identity = ServerIdentity(**dict(payload))
            identity.validate()
            provider = get_provider(identity.provider_id)
            if provider is None:
                raise ValueError(f"Unsupported provider_id: {identity.provider_id}")
            server_type = identity.server_type.strip().lower()
            if server_type not in SUPPORTED_SERVER_TYPES:
                raise ValueError(f"Unsupported server_type: {identity.server_type}")
            environment = identity.environment.strip().lower()
            if environment not in SUPPORTED_ENVIRONMENTS:
                raise ValueError(f"Unsupported environment: {identity.environment}")
            return {
                "success": True,
                "identity": {
                    "server_id": identity.server_id.strip(),
                    "provider_id": identity.provider_id.strip().lower(),
                    "server_type": server_type,
                    "server_role": identity.server_role.strip(),
                    "country": identity.country.strip().upper(),
                    "region": identity.region.strip(),
                    "environment": environment,
                    "metadata": dict(identity.metadata),
                },
            }
        except (TypeError, ValueError) as exc:
            return {"success": False, "error": "SERVER_CORE_VALIDATION_FAILED", "message": str(exc)}

    def register_identity(self, payload: dict[str, Any]) -> dict[str, Any]:
        validated = self.validate_identity(payload)
        if not validated["success"]:
            return validated
        try:
            return {"success": True, "identity": self.registry.register(ServerIdentity(**validated["identity"]))}
        except (TypeError, ValueError) as exc:
            return {"success": False, "error": "SERVER_CORE_REGISTRATION_FAILED", "message": str(exc)}

    def get_identity(self, server_id: str):
        item = self.registry.get(server_id)
        return {"success": True, "identity": item} if item is not None else None

    def list_identities(self):
        items = self.registry.list()
        return {"success": True, "count": len(items), "identities": items}

    def health_local(self):
        return {"layer": "CORE", "ecosystem": ECOSYSTEM_NAME, "status": "HEALTHY",
                "registered_identities": self.registry.count(), "remote_operations_enabled": False}
