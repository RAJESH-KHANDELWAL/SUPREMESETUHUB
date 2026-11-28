"""Manager for the INTEGRATION_TIERS_NORMAL_TO_SUPREME integration domain."""
from ..domain_runtime import IntegrationDomainManager
class IntegrationTiersNormalToSupremeDomainManager(IntegrationDomainManager):
    DOMAIN_ID="INTEGRATION_TIERS_NORMAL_TO_SUPREME"
def get_manager(): return IntegrationTiersNormalToSupremeDomainManager()
__all__=["IntegrationTiersNormalToSupremeDomainManager","get_manager"]
