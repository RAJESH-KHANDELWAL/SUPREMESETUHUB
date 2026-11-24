"""Domain-specific read-only manager backed by the shared runtime."""
from ..domain_runtime import get_domain_manager
DOMAIN_ID = "SEXUAL_EDUCATION_AND_TRADITIONAL_KNOWLEDGE"
def get_manager():
    return get_domain_manager(DOMAIN_ID)
__all__ = ["DOMAIN_ID", "get_manager"]
