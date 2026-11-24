"""PROVIDER GOVERNANCE Google Core domain package."""
from .manager import ProviderGovernanceDomainManager, get_manager

DOMAIN_ID = "PROVIDER_GOVERNANCE"
__all__ = ["DOMAIN_ID", "ProviderGovernanceDomainManager", "get_manager"]
