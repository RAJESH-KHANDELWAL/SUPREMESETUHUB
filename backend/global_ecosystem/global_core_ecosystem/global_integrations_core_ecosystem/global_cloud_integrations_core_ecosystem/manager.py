"""Manager for the GLOBAL_CLOUD integration domain."""
from ..domain_runtime import IntegrationDomainManager
class GlobalCloudDomainManager(IntegrationDomainManager):
    DOMAIN_ID="GLOBAL_CLOUD"
def get_manager(): return GlobalCloudDomainManager()
__all__=["GlobalCloudDomainManager","get_manager"]
