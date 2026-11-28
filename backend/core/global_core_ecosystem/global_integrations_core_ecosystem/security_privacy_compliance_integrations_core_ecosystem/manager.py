"""Manager for the SECURITY_PRIVACY_COMPLIANCE integration domain."""
from ..domain_runtime import IntegrationDomainManager
class SecurityPrivacyComplianceDomainManager(IntegrationDomainManager):
    DOMAIN_ID="SECURITY_PRIVACY_COMPLIANCE"
def get_manager(): return SecurityPrivacyComplianceDomainManager()
__all__=["SecurityPrivacyComplianceDomainManager","get_manager"]
