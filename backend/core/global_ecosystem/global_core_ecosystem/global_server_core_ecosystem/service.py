"""GLOBAL SERVER CORE public read-only control-plane service."""
from __future__ import annotations
from typing import Any
from .catalog import get_catalog
from .constants import CAPABILITIES, ECOSYSTEM_ID, ECOSYSTEM_NAME
from .models import ServerIdentity
from .orchestrator import ServerCoreOrchestrator
from .policy import ServerCorePolicy
from .provider_catalog import get_provider
from .registry import ServerCoreRegistry

class ServerCoreService:
    """Expose catalog, policy and local identity metadata; never provision servers."""
    NAME=ECOSYSTEM_NAME
    def __init__(self, registry: ServerCoreRegistry | None=None) -> None:
        self.registry=registry or ServerCoreRegistry()
        self.orchestrator=ServerCoreOrchestrator()
    def describe(self) -> dict[str, Any]:
        """Return the stable CORE boundary description without live operations."""
        catalog = get_catalog()
        from .policy import SUPPORTED_ENVIRONMENTS, SUPPORTED_SERVER_TYPES

        return {
            "layer": "CORE",
            "ecosystem_id": ECOSYSTEM_ID,
            "ecosystem": ECOSYSTEM_NAME,
            "status": "CORE_CATALOG_ONLY",
            "capabilities": list(CAPABILITIES),
            "provider_domains": [
                str(item["provider_id"]).lower()
                for item in catalog["providers"]
            ],
            "provider_count": catalog["provider_count"],
            "supported_server_types": list(SUPPORTED_SERVER_TYPES),
            "supported_environments": list(SUPPORTED_ENVIRONMENTS),
            "registered_identities": self.registry.count(),
            "remote_operations_enabled": False,
            "registry_persistence": "PROCESS_LOCAL_ONLY",
        }

    def status(self) -> dict[str, Any]:
        catalog=get_catalog()
        health=self.orchestrator.health()
        manager=self.manager_status()
        return {"success":True,"ecosystem_id":ECOSYSTEM_ID,"name":self.NAME,
                "provider":"provider-neutral","status":catalog["status"],
                "registry_status":manager["registered"],"provider_count":catalog["provider_count"],
                "core_domain_count":health["core_domain_count"],
                "workload_domain_count":health["workload_domain_count"],
                "service_tier_count":health["service_tier_count"],
                "registered_identities":self.registry.count(),
                "live_provider_connections_verified":0,"api_calls_performed":0,
                "remote_operations_enabled":False,"health":health}
    def catalog(self): return self.orchestrator.catalog()
    def list_providers(self): return self.orchestrator.providers()
    def list_domains(self): return self.orchestrator.domains()
    def list_workload_domains(self):
        items=self.catalog()["workload_domains"]
        return {"success":True,"count":len(items),"domains":items}
    def get_provider(self, provider_id: str): return self.orchestrator.provider(provider_id)
    def health(self): return self.orchestrator.health()
    def dependency_map(self): return self.orchestrator.dependency_map()
    def manager_status(self):
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            record=GlobalEcosystemManager().get(ECOSYSTEM_ID)
        except Exception as exc:
            return {"success":False,"registered":False,"ecosystem":None,"error":type(exc).__name__}
        return {"success":record is not None,"registered":record is not None,
                "ecosystem":record,"live_connection_verified":False}
    def validate_identity(self, payload: dict[str, Any]) -> dict[str, Any]:
        try:
            identity=ServerIdentity(**dict(payload))
            identity.validate()
            if get_provider(identity.provider_id) is None:
                raise ValueError(f"Unsupported provider_id: {identity.provider_id}")
            from .policy import SUPPORTED_ENVIRONMENTS, SUPPORTED_SERVER_TYPES
            server_type=identity.server_type.strip().lower()
            environment=identity.environment.strip().lower()
            if server_type not in SUPPORTED_SERVER_TYPES:
                raise ValueError(f"Unsupported server_type: {identity.server_type}")
            if environment not in SUPPORTED_ENVIRONMENTS:
                raise ValueError(f"Unsupported environment: {identity.environment}")
            safe=ServerCorePolicy.safe_summary({
                "server_id":identity.server_id.strip(),"provider_id":identity.provider_id.strip().lower(),
                "server_type":server_type,"server_role":identity.server_role.strip(),
                "country":identity.country.strip().upper(),"region":identity.region.strip(),
                "environment":environment,"metadata":dict(identity.metadata)})
            return {"success":True,"identity":safe}
        except (TypeError,ValueError) as exc:
            return {"success":False,"error":"SERVER_CORE_VALIDATION_FAILED","message":str(exc)}
    def register_identity(self, payload: dict[str, Any]) -> dict[str, Any]:
        validated=self.validate_identity(payload)
        if not validated["success"]: return validated
        try:
            return {"success":True,"identity":self.registry.register(ServerIdentity(**validated["identity"])),
                    "persistence":"PROCESS_LOCAL_ONLY"}
        except (TypeError,ValueError) as exc:
            return {"success":False,"error":"SERVER_CORE_REGISTRATION_FAILED","message":str(exc)}
    def get_identity(self, server_id: str):
        item=self.registry.get(server_id)
        return {"success":True,"identity":item} if item is not None else None
    def list_identities(self):
        items=self.registry.list()
        return {"success":True,"count":len(items),"identities":items,
                "persistence":"PROCESS_LOCAL_ONLY"}
