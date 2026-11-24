from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="VISUAL_ART_DESIGN_AND_IMAGE_COMMUNITIES"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
