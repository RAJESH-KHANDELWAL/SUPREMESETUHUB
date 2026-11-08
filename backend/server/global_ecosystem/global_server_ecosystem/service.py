"""SERVER coordinator; each layer remains owner of its own behavior."""
from typing import Any
from .models import LayerDescriptor, ServerOrchestrationRequest, ServerOrchestrationResult
from .registry import ServerLayerRegistry
LAYER_DESCRIPTORS = (
    LayerDescriptor("API","HTTP routes, schemas and transport","backend/api/global_ecosystem/global_api_ecosystem/"),
    LayerDescriptor("CORE","Domain contracts, models, rules and policies","backend/core/global_ecosystem/global_core_ecosystem/"),
    LayerDescriptor("ENGINE","Execution and provider adapters","backend/engine/global_ecosystem/global_engine_ecosystem/"),
    LayerDescriptor("DATABASE","Durable structured records and database access","backend/database/global_ecosystem/global_database_ecosystem/"),
    LayerDescriptor("STORAGE","Files, objects and artifact persistence","backend/storage/global_ecosystem/global_storage_ecosystem/"),
)
class GlobalServerEcosystemService:
    domain = "SERVER"
    ecosystem = "GLOBAL_SERVER_ECOSYSTEM"
    def __init__(self, registry: ServerLayerRegistry | None = None) -> None:
        self.registry = registry or ServerLayerRegistry()
    def register_layer(self, layer: str, adapter: Any, *, replace: bool = False) -> Any:
        return self.registry.register(layer, adapter, replace=replace)
    def health(self) -> dict[str, Any]:
        return {"domain":self.domain,"ecosystem":self.ecosystem,"status":self.registry.status(),
                "layers":[{"name":x.name,"responsibility":x.responsibility,"owner_path":x.owner_path,
                           "connected":self.registry.get(x.name) is not None} for x in LAYER_DESCRIPTORS],
                "provider_connections":"NOT_ATTEMPTED"}
    def dispatch(self, request: ServerOrchestrationRequest) -> ServerOrchestrationResult:
        operation = str(request.operation or "").strip()
        if not operation:
            return ServerOrchestrationResult(False,operation,"REJECTED",error="operation is required")
        core, engine = self.registry.get("CORE"), self.registry.get("ENGINE")
        missing = [name for name,adapter in (("CORE",core),("ENGINE",engine)) if adapter is None]
        if missing:
            return ServerOrchestrationResult(False,operation,"NOT_READY",layers={"missing":missing},
                                             error="Required CORE and ENGINE adapters are not registered")
        try:
            validated = core.validate_request(dict(request.payload))
            output = engine.dispatch(operation,dict(validated))
            return ServerOrchestrationResult(True,operation,"COMPLETED",
                                             layers={"CORE":"VALIDATED","ENGINE":"DISPATCHED"},
                                             result=dict(output or {}))
        except Exception as exc:
            return ServerOrchestrationResult(False,operation,"FAILED",
                                             error=f"{type(exc).__name__}: {exc}")
__all__ = ["GlobalServerEcosystemService","LAYER_DESCRIPTORS"]
