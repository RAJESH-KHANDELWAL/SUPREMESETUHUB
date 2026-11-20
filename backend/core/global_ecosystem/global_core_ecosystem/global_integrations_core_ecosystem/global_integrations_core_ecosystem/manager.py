"""Manager for the GLOBAL_INTEGRATIONS integration domain."""
from ..domain_runtime import IntegrationDomainManager
class GlobalIntegrationsDomainManager(IntegrationDomainManager):
    DOMAIN_ID="GLOBAL_INTEGRATIONS"
def get_manager(): return GlobalIntegrationsDomainManager()
__all__=["GlobalIntegrationsDomainManager","get_manager"]
