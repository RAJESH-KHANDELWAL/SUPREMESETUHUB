"""Global Integration Governance domain package."""
from .manager import GlobalIntegrationsDomainManager, get_manager
DOMAIN_ID="GLOBAL_INTEGRATIONS"
__all__=["DOMAIN_ID","GlobalIntegrationsDomainManager","get_manager"]
