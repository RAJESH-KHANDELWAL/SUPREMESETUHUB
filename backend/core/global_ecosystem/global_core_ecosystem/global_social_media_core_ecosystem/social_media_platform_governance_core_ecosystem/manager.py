from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="PLATFORM_GOVERNANCE_AND_CROSS_PLATFORM_DISCOVERY"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
