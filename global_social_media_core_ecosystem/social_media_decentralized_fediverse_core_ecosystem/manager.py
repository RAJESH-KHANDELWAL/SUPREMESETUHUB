from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="DECENTRALIZED_AND_FEDIVERSE_COMMUNITIES"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
