"""Framework-neutral controller for SERVER use cases."""
from .manager import ServerManager

class ServerController:
    def __init__(self, manager=None): self.manager = manager or ServerManager()
    def status(self): return self.manager.health()
    def register(self, **payload): return self.manager.register(**payload)
    def get(self, server_id): return self.manager.get(server_id)
    def list(self): return self.manager.list()
