from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="MESSAGING_AND_COMMUNITY_COMMUNICATION"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
