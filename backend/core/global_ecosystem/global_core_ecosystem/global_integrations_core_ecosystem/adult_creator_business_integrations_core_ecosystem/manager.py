"""Manager for the ADULT_CREATOR_BUSINESS integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AdultCreatorBusinessDomainManager(IntegrationDomainManager):
    DOMAIN_ID="ADULT_CREATOR_BUSINESS"
def get_manager(): return AdultCreatorBusinessDomainManager()
__all__=["AdultCreatorBusinessDomainManager","get_manager"]
