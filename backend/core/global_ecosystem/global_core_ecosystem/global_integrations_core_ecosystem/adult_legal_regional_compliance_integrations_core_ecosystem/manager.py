"""Manager for the ADULT_LEGAL_REGIONAL_COMPLIANCE integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AdultLegalRegionalComplianceDomainManager(IntegrationDomainManager):
    DOMAIN_ID="ADULT_LEGAL_REGIONAL_COMPLIANCE"
def get_manager(): return AdultLegalRegionalComplianceDomainManager()
__all__=["AdultLegalRegionalComplianceDomainManager","get_manager"]
