"""Read-only catalog service for hospitality business services."""
from .domain_catalog import DOMAINS, list_domains, get_domain
class HospitalityBusinessService:
    ECOSYSTEM_ID = "GLOBAL-HOSPITALITY-HOTELS-RESORTS-RESTAURANTS-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"
    def catalog(self): return {"ecosystem_id": self.ECOSYSTEM_ID, "domains": list_domains(), "domain_count": len(DOMAINS), "mode": "READ_ONLY_SERVICE_CATALOG"}
    def get_domain(self, domain_id): return get_domain(domain_id)
    def search(self, query=""):
        term = str(query or "").casefold().strip()
        return [item for item in list_domains() if not term or term in item["id"] or any(term in c.casefold() for c in item["capabilities"])]
    def readiness(self): return {"catalog_ready": True, "service_delivery_enabled": False, "provider_verification": "EVIDENCE_AND_EXTERNAL_REVIEW_REQUIRED", "transactions_enabled": False, "status": "SERVICE_CATALOG_READY"}
