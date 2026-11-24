"""Lifecycle and access manager for the independent SERVER domain."""
from .service import ServerService


class ServerManager:
    def __init__(self, service=None):
        self.service = service or ServerService()

    def start(self):
        return {"domain": "SERVER", "status": "READY", "health": self.service.health()}

    def stop(self):
        return {"domain": "SERVER", "status": "STOPPED"}

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

    def start_server(self, server_id):
        return self.service.start(server_id)

    def stop_server(self, server_id):
        return self.service.stop(server_id)

    def restart_server(self, server_id):
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
