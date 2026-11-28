"""Manager for the SPECIALTY_AND_CROSS_PRODUCT Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class SpecialtyServicesDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "SPECIALTY_AND_CROSS_PRODUCT"


def get_manager() -> SpecialtyServicesDomainManager:
    return SpecialtyServicesDomainManager()


__all__ = ["SpecialtyServicesDomainManager", "get_manager"]
