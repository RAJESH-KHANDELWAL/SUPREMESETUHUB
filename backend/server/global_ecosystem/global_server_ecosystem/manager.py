"""Manager facade for the independent GLOBAL SERVER runtime."""
from .registry import ServerRegistry
from .provider_registry import ServerProviderRegistry
from .service import GlobalServerEcosystemService

class GlobalServerEcosystemManager:
    def __init__(self):
        self.server_registry = ServerRegistry()
        self.provider_registry = ServerProviderRegistry()
        self.service = GlobalServerEcosystemService(self.server_registry, self.provider_registry)

    def register_server(self, server, *, replace=False):
        return self.service.register_server(server, replace=replace)
    def get_server(self, server_id):
        return self.service.get_server(server_id)
    def list_servers(self):
        return self.service.list_servers()
    def unregister_server(self, server_id):
        return self.service.unregister_server(server_id)
    def register_provider(self, provider_id, provider, *, replace=False):
        return self.service.register_provider(provider_id, provider, replace=replace)
    def register_operation_adapter(self, capability, adapter, *, replace=False):
        return self.service.register_operation_adapter(capability, adapter, replace=replace)
    def execute_operation(self, capability, operation, payload=None):
        return self.service.execute_operation(capability, operation, payload)
    def health(self):
        return self.service.health()
    def status(self):
        return self.service.status()
    def describe(self):
        return self.service.describe()

__all__ = ["GlobalServerEcosystemManager"]
