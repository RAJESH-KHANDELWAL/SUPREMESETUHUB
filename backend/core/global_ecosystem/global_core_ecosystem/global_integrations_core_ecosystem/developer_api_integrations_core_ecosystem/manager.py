"""Manager for the DEVELOPER_API integration domain."""
from ..domain_runtime import IntegrationDomainManager
class DeveloperApiDomainManager(IntegrationDomainManager):
    DOMAIN_ID="DEVELOPER_API"
def get_manager(): return DeveloperApiDomainManager()
__all__=["DeveloperApiDomainManager","get_manager"]
