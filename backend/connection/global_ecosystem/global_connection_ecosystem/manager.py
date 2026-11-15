"""Manager facade for the Global Connection Ecosystem."""

from .catalog import get_global_connection_catalog
from .service import GlobalConnectionService


class GlobalConnectionManager:
    def __init__(self, service=None):
        self.service = service or GlobalConnectionService()

    def register(self, request):
        return self.service.register(request)

    def authorize(self, connection_id, approved=False):
        return self.service.authorize(connection_id, approved=approved)

    def connect(self, connection_id, adapter_key):
        return self.service.connect(connection_id, adapter_key)

    def disconnect(self, connection_id, adapter_key):
        return self.service.disconnect(connection_id, adapter_key)

    def diagnostics(self):
        return self.service.diagnostics()

    def catalog(self):
        return get_global_connection_catalog()
