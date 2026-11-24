"""Lemon8 platform Core metadata facade."""
from ..module_service import SocialMediaPlatformService
class PlatformManager(SocialMediaPlatformService):
    PLATFORM_ID="lemon8"
def get_manager()->PlatformManager:return PlatformManager()
__all__=["PlatformManager","get_manager"]
