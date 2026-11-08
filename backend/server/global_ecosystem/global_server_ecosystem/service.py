"""SERVER orchestration; all layer behavior remains with its owning package."""
from typing import Any
from .catalog import get_layer_catalog, list_providers, list_service_types
from .models import ServerOrchestrationRequest, ServerOrchestrationResult
from .registry import ServerLayerRegistry
from .provider_registry import ServerProviderRegistry
class GlobalServerEcosystemService:
    domain = "SERVER"
    ecosystem = "GLOBAL_SERVER_ECOSYSTEM"
    def __init__(self, layer_registry=None, provider_registry=None):
        self.layers = layer_registry or ServerLayerRegistry()
        self.providers = provider_registry or ServerProviderRegistry()
    def register_layer(self, layer: str, adapter: Any, *, replace: bool = False):
        return self.layers.register(layer, adapter, replace=replace)
    def register_provider(self, provider_id: str, provider: Any, *, replace: bool = False):
        return self.providers.register(provider_id, provider, replace=replace)
    def health(self):
        return {
            "domain": self.domain, "ecosystem": self.ecosystem,
            "status": self.layers.status(),
            "layers": [{"name": x.name, "responsibility": x.responsibility,
                        "owner_path": x.owner_path,
                        "connected": self.layers.get(x.name) is not None}
                       for x in get_layer_catalog()],
            "providers": list(self.providers.catalog()),
            "external_connections": "NOT_ATTEMPTED",
        }
    def status(self):
        return {"status": "FOUNDATION_READY", "external_connections": "NOT_ATTEMPTED"}
    def describe(self):
        return {"ecosystem": self.ecosystem, "providers": list_providers(),
                "service_types": list_service_types(), "live_connections_enabled": False}
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
            return ServerOrchestrationResult(
                True, operation, "COMPLETED",
                layers={"CORE": "VALIDATED", "ENGINE": "DISPATCHED"},
                result=dict(output or {}))
        except Exception as exc:
            return ServerOrchestrationResult(False, operation, "FAILED",
                                             error=f"{type(exc).__name__}: {exc}")
EcosystemService = GlobalServerEcosystemService
__all__ = ["GlobalServerEcosystemService", "EcosystemService"]