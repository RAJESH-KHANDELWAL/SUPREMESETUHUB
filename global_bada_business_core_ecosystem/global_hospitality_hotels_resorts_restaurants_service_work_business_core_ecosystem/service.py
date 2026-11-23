"""Read-only hospitality business service catalog."""
from .contracts import ECOSYSTEM_ID, ECOSYSTEM_VERSION
from .domain_catalog import catalog_snapshot, get_domain, search_domains
class HospitalityBusinessService:
    def catalog(self): return {"ecosystem_id": ECOSYSTEM_ID, "version": ECOSYSTEM_VERSION, "mode": "READ_ONLY_SERVICE_WORK_BUSINESS_CATALOG", **catalog_snapshot()}
    def get_domain(self, domain_id): return get_domain(domain_id)
    def search(self, query=""): return search_domains(query)
    def readiness(self): return {"catalog_ready": True, "live_service_delivery_enabled": False, "payments_enabled": False, "booking_transactions_enabled": False, "external_integrations_enabled": False}
