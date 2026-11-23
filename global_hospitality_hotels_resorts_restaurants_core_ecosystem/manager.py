"""Stable manager entry point for the global hospitality core."""
from .service import HospitalityCoreService
class GlobalHospitalityCoreManager:
    ECOSYSTEM_ID = "GLOBAL-HOSPITALITY-HOTELS-RESORTS-RESTAURANTS-CORE-ECOSYSTEM"
    def __init__(self): self.service = HospitalityCoreService()
    def health(self): return {"success": True, "health": "HEALTHY", **self.service.readiness()}
    def catalog(self): return self.service.catalog()
    def get_domain(self, domain_id): return self.service.get_domain(domain_id)
    def search(self, query=""): return self.service.search(query)
def get_manager(): return GlobalHospitalityCoreManager()
__all__ = ["GlobalHospitalityCoreManager", "get_manager"]
