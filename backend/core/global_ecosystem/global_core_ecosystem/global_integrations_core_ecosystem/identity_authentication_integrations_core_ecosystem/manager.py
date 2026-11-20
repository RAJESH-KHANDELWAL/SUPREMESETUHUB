"""Manager for the IDENTITY_AUTHENTICATION integration domain."""
from ..domain_runtime import IntegrationDomainManager
class IdentityAuthenticationDomainManager(IntegrationDomainManager):
    DOMAIN_ID="IDENTITY_AUTHENTICATION"
def get_manager(): return IdentityAuthenticationDomainManager()
__all__=["IdentityAuthenticationDomainManager","get_manager"]
