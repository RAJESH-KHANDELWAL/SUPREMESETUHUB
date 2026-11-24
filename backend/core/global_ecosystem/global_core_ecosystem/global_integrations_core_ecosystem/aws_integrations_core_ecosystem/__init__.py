"""Amazon Web Services Provider Integrations domain package."""
from .manager import AwsDomainManager, get_manager
DOMAIN_ID="AWS"
__all__=["DOMAIN_ID","AwsDomainManager","get_manager"]
