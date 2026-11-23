"""Stable manager entry point for hospitality service-work business ecosystem."""
from .service import HospitalityBusinessService
class GlobalHospitalityBusinessManager:
    ECOSYSTEM_ID = "GLOBAL-HOSPITALITY-HOTELS-RESORTS-RESTAURANTS-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"
    def __init__(self): self.service = HospitalityBusinessService()
    def health(self): return {"success": True, "health": "HEALTHY", **self.service.readiness()}
    def catalog(self): return self.service.catalog()
    def get_domain(self, domain_id): return self.service.get_domain(domain_id)
    def search(self, query=""): return self.service.search(query)
def get_manager(): return GlobalHospitalityBusinessManager()
__all__ = ["GlobalHospitalityBusinessManager", "get_manager"]
