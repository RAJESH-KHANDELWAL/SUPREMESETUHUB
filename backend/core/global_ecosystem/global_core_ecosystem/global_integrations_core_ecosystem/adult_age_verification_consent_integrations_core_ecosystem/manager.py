"""Manager for the ADULT_AGE_VERIFICATION_CONSENT integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AdultAgeVerificationConsentDomainManager(IntegrationDomainManager):
    DOMAIN_ID="ADULT_AGE_VERIFICATION_CONSENT"
def get_manager(): return AdultAgeVerificationConsentDomainManager()
__all__=["AdultAgeVerificationConsentDomainManager","get_manager"]
