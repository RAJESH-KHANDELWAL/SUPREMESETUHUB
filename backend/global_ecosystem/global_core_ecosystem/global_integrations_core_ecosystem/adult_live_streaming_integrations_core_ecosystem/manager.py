"""Manager for the ADULT_LIVE_STREAMING integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AdultLiveStreamingDomainManager(IntegrationDomainManager):
    DOMAIN_ID="ADULT_LIVE_STREAMING"
def get_manager(): return AdultLiveStreamingDomainManager()
__all__=["AdultLiveStreamingDomainManager","get_manager"]
