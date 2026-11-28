"""Microsoft Provider Integrations domain package."""
from .manager import MicrosoftDomainManager, get_manager
DOMAIN_ID="MICROSOFT"
__all__=["DOMAIN_ID","MicrosoftDomainManager","get_manager"]
