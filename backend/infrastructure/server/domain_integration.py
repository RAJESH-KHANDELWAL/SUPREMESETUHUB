"""Bridge the canonical SERVER domain into infrastructure/server.

The original backend.server package remains the source of truth. This adapter
makes its capabilities available from the infrastructure server facade without
copying, moving, or creating a second implementation of the domain.
"""
from backend.server import ServerService as BackendServerDomainService


class ServerDomainIntegration:
    """Expose the independent SERVER domain through infrastructure/server."""

    def __init__(self, service=None):
        self.service = service or BackendServerDomainService()

    def health(self):
        return self.service.health()

    def describe(self):
        return self.service.describe()

    def register(self, **kwargs):
        return self.service.register(**kwargs)

    def get(self, server_id):
        return self.service.get(server_id)

    def list(self):
        return self.service.list()

    def update(self, server_id, **changes):
        return self.service.update(server_id, **changes)

    def delete(self, server_id):
        return self.service.delete(server_id)

    def start(self, server_id):
        return self.service.start(server_id)

    def stop(self, server_id):
        return self.service.stop(server_id)

    def restart(self, server_id):
        return self.service.restart(server_id)

    def register_provider(self, provider_id, adapter, *, replace=False):
        return self.service.register_provider(provider_id, adapter, replace=replace)

    def describe_provider(self, provider_id):
        return self.service.describe_provider(provider_id)

    def provider_health(self, provider_id):
        return self.service.provider_health(provider_id)

    def execute_provider_operation(self, provider_id, operation, payload=None):
        return self.service.execute_provider_operation(provider_id, operation, payload)

    def register_operation_adapter(self, capability, adapter, *, replace=False):
        return self.service.register_operation_adapter(capability, adapter, replace=replace)

    def execute_operation(self, capability, operation, payload=None):
        return self.service.execute_operation(capability, operation, payload)


__all__ = ["ServerDomainIntegration"]
