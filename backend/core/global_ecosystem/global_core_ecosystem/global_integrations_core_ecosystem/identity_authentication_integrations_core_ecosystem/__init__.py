"""Identity & Authentication domain package."""
from .manager import IdentityAuthenticationDomainManager, get_manager
DOMAIN_ID="IDENTITY_AUTHENTICATION"
__all__=["DOMAIN_ID","IdentityAuthenticationDomainManager","get_manager"]
