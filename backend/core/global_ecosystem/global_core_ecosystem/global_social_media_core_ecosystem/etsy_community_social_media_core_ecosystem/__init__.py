"""Etsy Community platform Core metadata facade."""
from ..module_service import SocialMediaPlatformService
class PlatformManager(SocialMediaPlatformService):
    PLATFORM_ID="etsy_community"
def get_manager()->PlatformManager:return PlatformManager()
__all__=["PlatformManager","get_manager"]
