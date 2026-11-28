"""Domain manager for Security and Privacy."""
from ..domain_runtime import SoftwareCoreDomainManager
class SecurityAndPrivacyManager(SoftwareCoreDomainManager):
    DOMAIN_ID="SECURITY_AND_PRIVACY"
def get_manager(): return SecurityAndPrivacyManager()
