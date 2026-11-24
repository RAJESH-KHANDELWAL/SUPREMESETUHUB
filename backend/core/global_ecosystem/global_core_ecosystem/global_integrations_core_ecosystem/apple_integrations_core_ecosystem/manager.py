"""Manager for the APPLE integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AppleDomainManager(IntegrationDomainManager):
    DOMAIN_ID="APPLE"
def get_manager(): return AppleDomainManager()
__all__=["AppleDomainManager","get_manager"]
