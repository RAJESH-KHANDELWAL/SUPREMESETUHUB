"""Stable manager entry point for the global hospitality core."""
from .contracts import ECOSYSTEM_ID, ECOSYSTEM_VERSION
from .service import HospitalityCoreService
class GlobalHospitalityCoreManager:
    def __init__(self): self.service = HospitalityCoreService()
    def health(self): return {"success": True, "ecosystem_id": ECOSYSTEM_ID, "version": ECOSYSTEM_VERSION, **self.service.readiness()}
    def catalog(self): return self.service.catalog()
    def get_domain(self, domain_id): return self.service.get_domain(domain_id)
    def search(self, query=""): return self.service.search(query)
_manager = None
def get_manager():
    global _manager
    if _manager is None: _manager = GlobalHospitalityCoreManager()
    return _manager
__all__ = ["GlobalHospitalityCoreManager", "get_manager"]
