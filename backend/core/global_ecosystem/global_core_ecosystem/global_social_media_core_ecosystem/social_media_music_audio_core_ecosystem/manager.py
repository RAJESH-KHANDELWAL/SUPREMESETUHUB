from ..domain_runtime import SocialMediaCoreDomainManager
class DomainManager(SocialMediaCoreDomainManager):
    DOMAIN_ID="MUSIC_AUDIO_AND_PODCAST_COMMUNITIES"
def get_manager()->DomainManager:return DomainManager()
__all__=["DomainManager","get_manager"]
