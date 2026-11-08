"""Lifecycle manager for GLOBAL SERVER ECOSYSTEM."""
from .models import ServerOrchestrationRequest, ServerOrchestrationResult
from .registry import ServerLayerRegistry
from .provider_registry import ServerProviderRegistry
from .service import GlobalServerEcosystemService
class GlobalServerEcosystemManager:
    def __init__(self):
        self.layer_registry = ServerLayerRegistry()
        self.provider_registry = ServerProviderRegistry()
        self.service = GlobalServerEcosystemService(self.layer_registry, self.provider_registry)
    def register_layer(self, layer, adapter, *, replace=False):
        return self.service.register_layer(layer, adapter, replace=replace)
    def register_provider(self, provider_id, provider, *, replace=False):
        return self.service.register_provider(provider_id, provider, replace=replace)
    def health(self):
        return self.service.health()
    def dispatch(self, request: ServerOrchestrationRequest) -> ServerOrchestrationResult:
        return self.service.dispatch(request)
__all__ = ["GlobalServerEcosystemManager"]