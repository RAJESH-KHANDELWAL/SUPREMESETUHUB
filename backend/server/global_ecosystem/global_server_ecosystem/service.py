"""SERVER coordinator; each layer remains owner of its own behavior."""
from typing import Any
from .catalog import get_layer_catalog
from .models import ServerOrchestrationRequest, ServerOrchestrationResult
from .registry import ServerLayerRegistry

class GlobalServerEcosystemService:
    domain = "SERVER"
    ecosystem = "GLOBAL_SERVER_ECOSYSTEM"

    def __init__(self, registry: ServerLayerRegistry | None = None) -> None:
        self.registry = registry or ServerLayerRegistry()

    def register_layer(self, layer: str, adapter: Any, *, replace: bool = False) -> Any:
        return self.registry.register(layer, adapter, replace=replace)

    def health(self) -> dict[str, Any]:
        return {
            "domain": self.domain,
            "ecosystem": self.ecosystem,
            "status": self.registry.status(),
            "layers": [
                {
                    "name": item.name,
                    "responsibility": item.responsibility,
                    "owner_path": item.owner_path,
                    "connected": self.registry.get(item.name) is not None,
                }
                for item in get_layer_catalog()
            ],
            "provider_connections": "NOT_ATTEMPTED",
        }

    def dispatch(self, request: ServerOrchestrationRequest) -> ServerOrchestrationResult:
        operation = str(request.operation or "").strip()
        if not operation:
            return ServerOrchestrationResult(False, operation, "REJECTED", error="operation is required")
        core, engine = self.registry.get("CORE"), self.registry.get("ENGINE")
        missing = [name for name, adapter in (("CORE", core), ("ENGINE", engine)) if adapter is None]
        if missing:
            return ServerOrchestrationResult(
                False, operation, "NOT_READY", layers={"missing": missing},
                error="Required CORE and ENGINE adapters are not registered",
            )
        try:
            validated = core.validate_request(dict(request.payload))
            output = engine.dispatch(operation, dict(validated))
            return ServerOrchestrationResult(
                True, operation, "COMPLETED",
                layers={"CORE": "VALIDATED", "ENGINE": "DISPATCHED"},
                result=dict(output or {}),
            )
        except Exception as exc:
            return ServerOrchestrationResult(
                False, operation, "FAILED", error=f"{type(exc).__name__}: {exc}"
            )

__all__ = ["GlobalServerEcosystemService"]
