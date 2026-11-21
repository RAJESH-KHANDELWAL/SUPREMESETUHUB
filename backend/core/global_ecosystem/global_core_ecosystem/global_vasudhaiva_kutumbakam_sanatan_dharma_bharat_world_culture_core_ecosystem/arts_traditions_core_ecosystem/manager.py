"""Domain-specific facade backed by the shared cultural Core runtime."""
from ..domain_runtime import CulturalCoreDomainManager
class DomainManager(CulturalCoreDomainManager):
    DOMAIN_ID = "ARTS_AND_TRADITIONS"
def get_manager(): return DomainManager()
__all__ = ["DomainManager", "get_manager"]
