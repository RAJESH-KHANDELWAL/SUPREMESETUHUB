"""Read-only service over the hospitality industry catalog."""
from .domain_catalog import DOMAINS, list_domains, get_domain
class HospitalityCoreService:
    ECOSYSTEM_ID = "GLOBAL-HOSPITALITY-HOTELS-RESORTS-RESTAURANTS-CORE-ECOSYSTEM"
    def catalog(self):
        return {"ecosystem_id": self.ECOSYSTEM_ID, "domains": list_domains(), "domain_count": len(DOMAINS), "mode": "READ_ONLY_CATALOG"}
    def get_domain(self, domain_id):
        return get_domain(domain_id)
    def search(self, query=""):
        term = str(query or "").casefold().strip()
        return [item for item in list_domains() if not term or term in item["id"] or any(term in c.casefold() for c in item["capabilities"])]
    def readiness(self):
        return {"catalog_ready": True, "live_operations_enabled": False, "provider_verification": "EXTERNAL_PROCESS_REQUIRED", "status": "CORE_CATALOG_READY"}
