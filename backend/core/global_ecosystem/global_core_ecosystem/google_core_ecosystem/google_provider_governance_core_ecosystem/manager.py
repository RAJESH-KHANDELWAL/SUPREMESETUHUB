"""Manager for the PROVIDER_GOVERNANCE Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class ProviderGovernanceDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "PROVIDER_GOVERNANCE"


def get_manager() -> ProviderGovernanceDomainManager:
    return ProviderGovernanceDomainManager()


__all__ = ["ProviderGovernanceDomainManager", "get_manager"]
