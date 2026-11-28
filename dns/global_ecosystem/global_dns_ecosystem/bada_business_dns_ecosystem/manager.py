"""Public Bada Business DNS manager facade."""
from .service import BadaBusinessDNSService


class BadaBusinessDNSManager:
    def __init__(self, service=None, binding_repository=None, dns_service=None):
        self.service = service or BadaBusinessDNSService(
            binding_repository=binding_repository,
            dns_service=dns_service,
        )

    def status(self):
        return self.service.status()

    def get_domain_binding(self, tenant_id, domain):
        return self.service.get_domain_binding(tenant_id, domain)

    def list_records(self, tenant_id, domain):
        return self.service.list_records(tenant_id, domain)

    def apply_change(self, tenant_id, domain, request):
        return self.service.apply_change(tenant_id, domain, request)
