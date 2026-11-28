from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="REGIONAL_AND_LOCAL_SOCIAL_COMMUNITIES"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
