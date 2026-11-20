"""Manager for the ADULT_PRIVACY_SECURITY integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AdultPrivacySecurityDomainManager(IntegrationDomainManager):
    DOMAIN_ID="ADULT_PRIVACY_SECURITY"
def get_manager(): return AdultPrivacySecurityDomainManager()
__all__=["AdultPrivacySecurityDomainManager","get_manager"]
