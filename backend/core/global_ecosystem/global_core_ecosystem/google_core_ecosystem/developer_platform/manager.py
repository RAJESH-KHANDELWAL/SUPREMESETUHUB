"""Manager for the DEVELOPER_AND_APPLICATION_PLATFORM Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class DeveloperPlatformDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "DEVELOPER_AND_APPLICATION_PLATFORM"


def get_manager() -> DeveloperPlatformDomainManager:
    return DeveloperPlatformDomainManager()


__all__ = ["DeveloperPlatformDomainManager", "get_manager"]
