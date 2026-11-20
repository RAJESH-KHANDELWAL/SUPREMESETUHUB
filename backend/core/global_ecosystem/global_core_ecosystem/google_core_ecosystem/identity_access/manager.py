"""Manager for the IDENTITY_ACCESS_AND_ADMIN Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class IdentityAccessDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "IDENTITY_ACCESS_AND_ADMIN"


def get_manager() -> IdentityAccessDomainManager:
    return IdentityAccessDomainManager()


__all__ = ["IdentityAccessDomainManager", "get_manager"]
