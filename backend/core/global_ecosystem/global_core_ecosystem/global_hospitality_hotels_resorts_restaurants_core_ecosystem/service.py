"""Read-only catalog service for hospitality industry domains."""
from .contracts import ECOSYSTEM_ID, ECOSYSTEM_VERSION
from .domain_catalog import catalog_snapshot, get_domain, search_domains
class HospitalityCoreService:
    def catalog(self): return {"ecosystem_id": ECOSYSTEM_ID, "version": ECOSYSTEM_VERSION, "mode": "READ_ONLY_INDUSTRY_FOUNDATION", **catalog_snapshot()}
    def get_domain(self, domain_id): return get_domain(domain_id)
    def search(self, query=""): return search_domains(query)
    def readiness(self): return {"catalog_ready": True, "live_booking_enabled": False, "payments_enabled": False, "external_integrations_enabled": False}
