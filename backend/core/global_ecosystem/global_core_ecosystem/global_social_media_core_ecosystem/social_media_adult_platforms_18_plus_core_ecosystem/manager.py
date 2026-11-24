from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="ADULT_COMMUNITIES_AND_CREATOR_PLATFORMS_18_PLUS"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
