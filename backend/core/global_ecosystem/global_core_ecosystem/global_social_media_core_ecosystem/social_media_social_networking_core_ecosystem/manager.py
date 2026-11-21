from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="SOCIAL_NETWORKING_AND_MICROBLOGGING"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
