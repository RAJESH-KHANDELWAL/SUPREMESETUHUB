"""Manager for the ADVERTISING_COMMERCE_AND_MONETIZATION Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class AdvertisingCommerceDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "ADVERTISING_COMMERCE_AND_MONETIZATION"


def get_manager() -> AdvertisingCommerceDomainManager:
    return AdvertisingCommerceDomainManager()


__all__ = ["AdvertisingCommerceDomainManager", "get_manager"]
