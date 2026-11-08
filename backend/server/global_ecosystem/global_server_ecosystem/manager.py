"""Lifecycle facade for the independent GLOBAL SERVER ECOSYSTEM."""
from typing import Any
from .models import ServerOrchestrationRequest, ServerOrchestrationResult
from .registry import ServerLayerRegistry
from .service import GlobalServerEcosystemService

class GlobalServerEcosystemManager:
    """Owns SERVER orchestration lifecycle, not the implementation of other layers."""
    def __init__(self, registry: ServerLayerRegistry | None = None) -> None:
        self.registry = registry or ServerLayerRegistry()
        self.service = GlobalServerEcosystemService(self.registry)

    def register_layer(self, layer: str, adapter: Any, *, replace: bool = False) -> Any:
        return self.service.register_layer(layer, adapter, replace=replace)

    def health(self) -> dict[str, Any]:
        return self.service.health()

    def dispatch(self, request: ServerOrchestrationRequest) -> ServerOrchestrationResult:
        return self.service.dispatch(request)

__all__ = ["GlobalServerEcosystemManager"]
