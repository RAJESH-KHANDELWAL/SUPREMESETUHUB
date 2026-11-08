"""SERVER orchestration; implementation remains with each owning layer."""
from typing import Any
from .catalog import get_layer_catalog, list_providers, list_service_types
from .models import ServerOrchestrationRequest, ServerOrchestrationResult
from .registry import ServerLayerRegistry
from .provider_registry import ServerProviderRegistry
from .runtime import runtime_status
from .operations import ServerOperationService

class GlobalServerEcosystemService:
    domain = "SERVER"
    ecosystem = "GLOBAL_SERVER_ECOSYSTEM"

    def __init__(self, layer_registry=None, provider_registry=None, operation_service=None):
        self.layers = layer_registry or ServerLayerRegistry()
        self.providers = provider_registry or ServerProviderRegistry()
        self.operations = operation_service or ServerOperationService()

    def register_layer(self, layer: str, adapter: Any, *, replace: bool = False):
        return self.layers.register(layer, adapter, replace=replace)

    def register_provider(self, provider_id: str, provider: Any, *, replace: bool = False):
        return self.providers.register(provider_id, provider, replace=replace)

    def register_operation_adapter(self, capability: str, adapter: Any, *, replace: bool = False):
        return self.operations.register_adapter(capability, adapter, replace=replace)

    def execute_operation(self, capability: str, operation: str, payload=None):
        return self.operations.execute(capability, operation, payload)

    def health(self):
        return {
            "domain": self.domain,
            "ecosystem": self.ecosystem,
            "status": self.layers.status(),
            "layers": [
                {"name": item.name, "responsibility": item.responsibility,
                 "owner_path": item.owner_path,
                 "connected": self.layers.get(item.name) is not None}
                for item in get_layer_catalog()
            ],
            "providers": list(self.providers.catalog()),
            "operations": self.operations.status(),
            "external_connections": "NOT_ATTEMPTED",
            "runtime": runtime_status(),
        }

    def status(self):
        return {
            "status": "FOUNDATION_READY",
            "external_connections": "NOT_ATTEMPTED",
            "operations": self.operations.status(),
        }

    def describe(self):
        return {
            "ecosystem": self.ecosystem,
            "providers": list_providers(),
            "service_types": list_service_types(),
            "live_connections_enabled": False,
            "operations": self.operations.status(),
            "runtime": runtime_status(),
        }

    def dispatch(self, request: ServerOrchestrationRequest) -> ServerOrchestrationResult:
        operation = str(request.operation or "").strip()
        if not operation:
            return ServerOrchestrationResult(False, operation, "REJECTED",
                                             error="operation is required")
        core, engine = self.layers.get("CORE"), self.layers.get("ENGINE")
        missing = [name for name, adapter in (("CORE", core), ("ENGINE", engine))
                   if adapter is None]
        if missing:
            return ServerOrchestrationResult(
                False, operation, "NOT_READY", layers={"missing": missing},
                error="Required CORE and ENGINE adapters are not registered")
        try:
            validated = core.validate_request(dict(request.payload))
            output = engine.dispatch(operation, dict(validated))
            if output is not None and not isinstance(output, dict):
                raise TypeError("ENGINE adapter result must be a dict or None")
            return ServerOrchestrationResult(
                True, operation, "COMPLETED",
                layers={"CORE": "VALIDATED", "ENGINE": "DISPATCHED"},
                result=dict(output or {}))
        except Exception as exc:
            return ServerOrchestrationResult(False, operation, "FAILED",
                                             error=f"{type(exc).__name__}: {exc}")

EcosystemService = GlobalServerEcosystemService
__all__ = ["GlobalServerEcosystemService", "EcosystemService"]
