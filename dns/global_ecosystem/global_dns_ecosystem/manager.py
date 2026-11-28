"""Public manager for GLOBAL DNS ECOSYSTEM."""
from .service import GlobalDNSService
from .models import DNSChangeRequest, DNSRecord

class GlobalDNSManager:
    def __init__(self, service=None, provider_clients=None):
        self.service = service or GlobalDNSService(provider_clients)

    def status(self):
        return self.service.status()

    def list_providers(self):
        return self.service.list_providers()

    def get_provider(self, provider_id: str):
        return self.service.get_provider(provider_id)

    def list_records(self, provider_id: str, zone_id: str):
        return self.service.list_records(provider_id, zone_id)

    def apply_change(self, request: DNSChangeRequest):
        return self.service.apply_change(request)
