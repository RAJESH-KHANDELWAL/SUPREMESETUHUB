"""Manager for the ADULT_CONTENT_PRODUCTION_STUDIO integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AdultContentProductionStudioDomainManager(IntegrationDomainManager):
    DOMAIN_ID="ADULT_CONTENT_PRODUCTION_STUDIO"
def get_manager(): return AdultContentProductionStudioDomainManager()
__all__=["AdultContentProductionStudioDomainManager","get_manager"]
