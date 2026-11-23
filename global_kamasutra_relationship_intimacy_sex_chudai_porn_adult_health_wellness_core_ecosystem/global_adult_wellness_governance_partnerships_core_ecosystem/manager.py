"""Domain-specific read-only manager backed by the shared runtime."""
from ..domain_runtime import get_domain_manager
DOMAIN_ID = "GLOBAL_AND_REGIONAL_GOVERNANCE"
def get_manager():
    return get_domain_manager(DOMAIN_ID)
__all__ = ["DOMAIN_ID", "get_manager"]
