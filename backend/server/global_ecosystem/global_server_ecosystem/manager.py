"""Composition and lifecycle facade for GLOBAL SERVER ECOSYSTEM."""
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

    def register_operation_adapter(self, capability, adapter, *, replace=False):
        return self.service.register_operation_adapter(capability, adapter, replace=replace)

    def execute_operation(self, capability, operation, payload=None):
        return self.service.execute_operation(capability, operation, payload)

    def read_server_record(self, server_id):
        return self.service.read_server_record(server_id)

    def resolve_artifact(self, artifact_id):
        return self.service.resolve_artifact(artifact_id)

    def health(self):
        return self.service.health()

    def status(self):
        return self.service.status()

    def describe(self):
        return self.service.describe()

    def dispatch(self, request: ServerOrchestrationRequest) -> ServerOrchestrationResult:
        return self.service.dispatch(request)

__all__ = ["GlobalServerEcosystemManager"]
