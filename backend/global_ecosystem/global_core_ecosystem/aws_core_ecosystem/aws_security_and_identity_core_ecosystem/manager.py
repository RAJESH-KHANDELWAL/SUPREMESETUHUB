"""Manager for the Security and Identity AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class SecurityAndIdentityDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="SECURITY_AND_IDENTITY"
def get_manager()->SecurityAndIdentityDomainManager:return SecurityAndIdentityDomainManager()
__all__=["SecurityAndIdentityDomainManager","get_manager"]
