"""Manager for the BUSINESS_EDUCATION_AND_LOCAL Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class BusinessEducationDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "BUSINESS_EDUCATION_AND_LOCAL"


def get_manager() -> BusinessEducationDomainManager:
    return BusinessEducationDomainManager()


__all__ = ["BusinessEducationDomainManager", "get_manager"]
