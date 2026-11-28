from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="PUBLISHING_BLOGGING_AND_NEWSLETTERS"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
