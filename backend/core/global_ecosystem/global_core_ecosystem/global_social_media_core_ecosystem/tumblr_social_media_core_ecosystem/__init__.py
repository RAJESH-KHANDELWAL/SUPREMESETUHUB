"""Tumblr platform Core metadata facade."""
from ..module_service import SocialMediaPlatformService
class PlatformManager(SocialMediaPlatformService):
    PLATFORM_ID="tumblr"
def get_manager()->PlatformManager:return PlatformManager()
__all__=["PlatformManager","get_manager"]
