"""Stable manager entry point for hospitality service-work business."""
from .contracts import ECOSYSTEM_ID, ECOSYSTEM_VERSION
from .service import HospitalityBusinessService
class GlobalHospitalityBusinessManager:
    def __init__(self): self.service = HospitalityBusinessService()
    def health(self): return {"success": True, "ecosystem_id": ECOSYSTEM_ID, "version": ECOSYSTEM_VERSION, **self.service.readiness()}
    def catalog(self): return self.service.catalog()
    def get_domain(self, domain_id): return self.service.get_domain(domain_id)
    def search(self, query=""): return self.service.search(query)
_manager = None
def get_manager():
    global _manager
    if _manager is None: _manager = GlobalHospitalityBusinessManager()
    return _manager
__all__ = ["GlobalHospitalityBusinessManager", "get_manager"]
