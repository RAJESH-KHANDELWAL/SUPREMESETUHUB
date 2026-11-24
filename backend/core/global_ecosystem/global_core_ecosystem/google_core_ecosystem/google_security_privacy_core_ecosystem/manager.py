"""Manager for the SECURITY_PRIVACY_AND_COMPLIANCE Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class SecurityPrivacyDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "SECURITY_PRIVACY_AND_COMPLIANCE"


def get_manager() -> SecurityPrivacyDomainManager:
    return SecurityPrivacyDomainManager()


__all__ = ["SecurityPrivacyDomainManager", "get_manager"]
