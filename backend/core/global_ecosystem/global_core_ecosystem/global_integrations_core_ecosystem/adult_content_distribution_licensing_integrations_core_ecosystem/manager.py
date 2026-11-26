"""Manager for the ADULT_CONTENT_DISTRIBUTION_LICENSING integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AdultContentDistributionLicensingDomainManager(IntegrationDomainManager):
    DOMAIN_ID="ADULT_CONTENT_DISTRIBUTION_LICENSING"
def get_manager(): return AdultContentDistributionLicensingDomainManager()
__all__=["AdultContentDistributionLicensingDomainManager","get_manager"]
