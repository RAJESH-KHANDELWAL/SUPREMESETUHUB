"""Framework-neutral controller for SERVER use cases."""
from .manager import ServerManager


class ServerController:
    def __init__(self, manager=None):
        self.manager = manager or ServerManager()

    def status(self):
        return self.manager.health()

    def register(self, **payload):
        return self.manager.register(**payload)

    def get(self, server_id):
        return self.manager.get(server_id)

    def list(self):
        return self.manager.list()

    def update(self, server_id, **changes):
        return self.manager.update(server_id, **changes)

    def delete(self, server_id):
        return self.manager.delete(server_id)

    def start(self, server_id):
        return self.manager.start_server(server_id)

    def stop(self, server_id):
        return self.manager.stop_server(server_id)

    def restart(self, server_id):
        return self.manager.restart_server(server_id)

    def provider_health(self, provider_id):
        return self.manager.provider_health(provider_id)

    def execute_provider_operation(self, provider_id, operation, payload=None):
        return self.manager.execute_provider_operation(provider_id, operation, payload)

    def execute_operation(self, capability, operation, payload=None):
        return self.manager.execute_operation(capability, operation, payload)
