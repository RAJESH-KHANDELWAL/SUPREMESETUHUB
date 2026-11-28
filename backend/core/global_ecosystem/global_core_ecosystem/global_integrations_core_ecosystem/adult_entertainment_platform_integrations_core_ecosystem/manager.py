"""Manager for the ADULT_ENTERTAINMENT_PLATFORM integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AdultEntertainmentPlatformDomainManager(IntegrationDomainManager):
    DOMAIN_ID="ADULT_ENTERTAINMENT_PLATFORM"
def get_manager(): return AdultEntertainmentPlatformDomainManager()
__all__=["AdultEntertainmentPlatformDomainManager","get_manager"]
