"""Bada Business namespaced connection service."""

from ..models import ConnectionRequest
from ..service import GlobalConnectionService
from .policies import validate_bada_business_connection


class BadaBusinessConnectionService:
    def __init__(self, global_service=None):
        self.global_service = global_service or GlobalConnectionService()

    def register(self, request):
        errors = validate_bada_business_connection(request)
        if errors:
            return {"success": False, "errors": list(errors)}
        global_request = ConnectionRequest(
            connection_id=request.connection_id,
            provider_id=request.provider_id,
            server_id=request.server_id,
            connection_type=request.connection_type,
            protocol=request.protocol,
            endpoint=request.endpoint,
            namespace="bada_business",
        )
        return self.global_service.register(global_request)

    def authorize(self, connection_id, approved=False):
        return self.global_service.authorize(connection_id, approved=approved)

    def connect(self, connection_id, adapter_key):
        return self.global_service.connect(connection_id, adapter_key)

    def disconnect(self, connection_id, adapter_key):
        return self.global_service.disconnect(connection_id, adapter_key)

    def diagnostics(self):
        result = self.global_service.diagnostics()
        result["system"] = "Bada Business Connection Ecosystem"
        result["namespace"] = "bada_business"
        return result
