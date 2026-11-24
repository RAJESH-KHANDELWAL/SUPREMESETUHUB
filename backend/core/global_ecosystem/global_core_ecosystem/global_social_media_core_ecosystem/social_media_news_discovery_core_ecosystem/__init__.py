from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="NEWS_AND_CONTENT_DISCOVERY"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
