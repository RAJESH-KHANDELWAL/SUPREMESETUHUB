"""Way2News platform Core metadata facade."""
from ..module_service import SocialMediaPlatformService
class PlatformManager(SocialMediaPlatformService):
    PLATFORM_ID="way2news"
def get_manager()->PlatformManager:return PlatformManager()
__all__=["PlatformManager","get_manager"]
