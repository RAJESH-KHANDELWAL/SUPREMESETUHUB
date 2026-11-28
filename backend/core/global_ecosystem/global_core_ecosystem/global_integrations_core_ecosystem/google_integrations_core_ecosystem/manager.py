"""Manager for the GOOGLE integration domain."""
from ..domain_runtime import IntegrationDomainManager
class GoogleDomainManager(IntegrationDomainManager):
    DOMAIN_ID="GOOGLE"
def get_manager(): return GoogleDomainManager()
__all__=["GoogleDomainManager","get_manager"]
