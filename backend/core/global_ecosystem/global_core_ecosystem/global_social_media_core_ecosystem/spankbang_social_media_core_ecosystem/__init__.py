"""Spankbang platform Core metadata facade."""
from ..module_service import SocialMediaPlatformService
class PlatformManager(SocialMediaPlatformService):
    PLATFORM_ID="spankbang"
def get_manager()->PlatformManager:return PlatformManager()
__all__=["PlatformManager","get_manager"]
