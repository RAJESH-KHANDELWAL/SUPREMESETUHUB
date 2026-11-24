"""Dribbble platform Core metadata facade."""
from ..module_service import SocialMediaPlatformService
class PlatformManager(SocialMediaPlatformService):
    PLATFORM_ID="dribbble"
def get_manager()->PlatformManager:return PlatformManager()
__all__=["PlatformManager","get_manager"]
