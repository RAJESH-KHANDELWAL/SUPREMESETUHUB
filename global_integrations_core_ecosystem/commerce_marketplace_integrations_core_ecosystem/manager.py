"""Manager for the COMMERCE_MARKETPLACE integration domain."""
from ..domain_runtime import IntegrationDomainManager
class CommerceMarketplaceDomainManager(IntegrationDomainManager):
    DOMAIN_ID="COMMERCE_MARKETPLACE"
def get_manager(): return CommerceMarketplaceDomainManager()
__all__=["CommerceMarketplaceDomainManager","get_manager"]
