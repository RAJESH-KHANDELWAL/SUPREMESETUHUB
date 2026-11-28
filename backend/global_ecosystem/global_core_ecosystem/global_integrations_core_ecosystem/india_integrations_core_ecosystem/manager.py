"""Manager for the INDIA integration domain."""
from ..domain_runtime import IntegrationDomainManager
class IndiaDomainManager(IntegrationDomainManager):
    DOMAIN_ID="INDIA"
def get_manager(): return IndiaDomainManager()
__all__=["IndiaDomainManager","get_manager"]
