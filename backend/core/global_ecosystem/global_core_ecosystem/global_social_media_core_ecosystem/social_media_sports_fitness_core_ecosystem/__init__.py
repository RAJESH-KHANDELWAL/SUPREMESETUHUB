from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="SPORTS_FITNESS_AND_ACTIVITY_COMMUNITIES"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
