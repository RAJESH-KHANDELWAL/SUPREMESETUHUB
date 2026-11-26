from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="CREATOR_ECONOMY_AND_MONETIZATION"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
