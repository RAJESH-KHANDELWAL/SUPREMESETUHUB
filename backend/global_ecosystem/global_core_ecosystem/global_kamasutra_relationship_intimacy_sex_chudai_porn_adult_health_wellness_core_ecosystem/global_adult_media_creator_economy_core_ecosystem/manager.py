"""Domain-specific read-only manager backed by the shared runtime."""
from ..domain_runtime import get_domain_manager
DOMAIN_ID = "ADULT_MEDIA_AND_CREATOR_ECONOMY"
def get_manager():
    return get_domain_manager(DOMAIN_ID)
__all__ = ["DOMAIN_ID", "get_manager"]
