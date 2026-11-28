from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="VIDEO_LIVE_STREAMING_AND_CREATOR_MEDIA"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
