"""Manager for the ANDROID_AND_MOBILE Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class AndroidMobileDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "ANDROID_AND_MOBILE"


def get_manager() -> AndroidMobileDomainManager:
    return AndroidMobileDomainManager()


__all__ = ["AndroidMobileDomainManager", "get_manager"]
