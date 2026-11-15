"""Manager facade for Bada Business connections."""

from .catalog import get_bada_business_connection_catalog
from .service import BadaBusinessConnectionService


class BadaBusinessConnectionManager:
    def __init__(self, service=None):
        self.service = service or BadaBusinessConnectionService()

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
        return get_bada_business_connection_catalog()
