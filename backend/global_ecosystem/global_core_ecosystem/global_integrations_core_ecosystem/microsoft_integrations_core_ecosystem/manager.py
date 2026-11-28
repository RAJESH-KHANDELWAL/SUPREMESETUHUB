"""Manager for the MICROSOFT integration domain."""
from ..domain_runtime import IntegrationDomainManager
class MicrosoftDomainManager(IntegrationDomainManager):
    DOMAIN_ID="MICROSOFT"
def get_manager(): return MicrosoftDomainManager()
__all__=["MicrosoftDomainManager","get_manager"]
