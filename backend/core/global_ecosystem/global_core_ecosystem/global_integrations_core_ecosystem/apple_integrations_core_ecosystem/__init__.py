"""Apple Provider Integrations domain package."""
from .manager import AppleDomainManager, get_manager
DOMAIN_ID="APPLE"
__all__=["DOMAIN_ID","AppleDomainManager","get_manager"]
