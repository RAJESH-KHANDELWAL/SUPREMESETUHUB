"""Domain-specific facade backed by the shared cultural Core runtime."""
from ..domain_runtime import CulturalCoreDomainManager
class DomainManager(CulturalCoreDomainManager):
    DOMAIN_ID = "BHARAT_SANSKRITI"
def get_manager(): return DomainManager()
__all__ = ["DomainManager", "get_manager"]
