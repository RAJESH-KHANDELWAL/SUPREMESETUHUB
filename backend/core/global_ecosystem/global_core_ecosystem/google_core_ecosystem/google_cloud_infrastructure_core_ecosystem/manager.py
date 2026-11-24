"""Manager for the CLOUD_INFRASTRUCTURE_AND_NETWORK Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class CloudInfrastructureDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "CLOUD_INFRASTRUCTURE_AND_NETWORK"


def get_manager() -> CloudInfrastructureDomainManager:
    return CloudInfrastructureDomainManager()


__all__ = ["CloudInfrastructureDomainManager", "get_manager"]
