"""Independent GLOBAL SERVER runtime service."""
from typing import Any
from .catalog import list_providers, get_provider, list_service_types, get_service_type
from .models import ServerNode
from .registry import ServerRegistry
from .provider_registry import ServerProviderRegistry
from .operations import ServerOperationService
from .integrations import ServerProviderGateway
from .services import ServerRuntimeService


class GlobalServerEcosystemService:
    domain = "SERVER"
    ecosystem = "GLOBAL_SERVER_ECOSYSTEM"

    def __init__(self, server_registry=None, provider_registry=None, operation_service=None):
        self.registry = server_registry or ServerRegistry()
        self.providers = provider_registry or ServerProviderRegistry()
        self.operations = operation_service or ServerOperationService()
        self.integrations = ServerProviderGateway(self.providers)
        self.runtime = ServerRuntimeService()

    def register_server(self, server: ServerNode, *, replace: bool = False):
        if not isinstance(server, ServerNode):
            raise TypeError("server must be a SERVER-owned ServerNode")
        return self.registry.register(server, replace=replace)

    def get_server(self, server_id: str):
        return self.registry.get(server_id)

    def list_servers(self):
        return self.registry.list()

    def unregister_server(self, server_id: str):
        return self.registry.unregister(server_id)

    def register_provider(self, provider_id: str, provider: Any, *, replace: bool = False):
        return self.providers.register(provider_id, provider, replace=replace)

    def get_provider_adapter(self, provider_id: str):
        return self.providers.get(provider_id)

    def describe_provider(self, provider_id: str):
        return self.integrations.describe(provider_id)

    def provider_health(self, provider_id: str):
        return self.integrations.health(provider_id)

    def execute_provider_operation(self, provider_id: str, operation: str, payload=None):
        return self.integrations.execute(provider_id, operation, payload)

    def register_operation_adapter(self, capability: str, adapter: Any, *, replace: bool = False):
        return self.operations.register_adapter(capability, adapter, replace=replace)

    def execute_operation(self, capability: str, operation: str, payload=None):
        return self.operations.execute(capability, operation, payload)

    def health(self):
        configured = len(self.providers.list_registered())
        runtime = self.runtime.health()
        # Registration is not proof of a live cloud connection. Keep the
        # domain state explicit and never report HEALTHY without real probes.
        domain_status = "CONFIGURED" if configured else "NOT_CONFIGURED"
        return {
            "domain": self.domain,
            "ecosystem": self.ecosystem,
            "status": domain_status,
            "server_registry": self.registry.status(),
            "providers": list(self.providers.catalog()),
            "operations": self.operations.status(),
            "configured_provider_count": configured,
            "external_connections": "NOT_ATTEMPTED",
            "runtime": runtime,
        }

    def status(self):
        result = self.health()
        return {
            "status": result["status"],
            "registered_servers": result["server_registry"]["registered_servers"],
            "configured_providers": result["configured_provider_count"],
            "external_connections": result["external_connections"],
            "runtime_status": result["runtime"]["status"],
        }

    def describe(self):
        return {
            "domain": self.domain,
            "ecosystem": self.ecosystem,
            "providers": list_providers(),
            "service_types": list_service_types(),
            "server_count": self.registry.count(),
            "live_provider_connections_enabled": False,
            "runtime": self.runtime.describe(),
        }

    def list_providers(self):
        return list_providers()

    def get_provider_catalog_entry(self, provider_id: str):
        return get_provider(provider_id)

    def list_service_types(self):
        return list_service_types()

    def get_service_type(self, service_type_id: str):
        return get_service_type(service_type_id)


EcosystemService = GlobalServerEcosystemService
__all__ = ["GlobalServerEcosystemService", "EcosystemService"]
