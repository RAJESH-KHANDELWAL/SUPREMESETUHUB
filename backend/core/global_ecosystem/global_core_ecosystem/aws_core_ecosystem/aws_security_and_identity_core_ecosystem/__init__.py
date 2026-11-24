"""Security and Identity AWS Core domain package."""
from .manager import SecurityAndIdentityDomainManager,get_manager
DOMAIN_ID="SECURITY_AND_IDENTITY"
__all__=["DOMAIN_ID","SecurityAndIdentityDomainManager","get_manager"]
