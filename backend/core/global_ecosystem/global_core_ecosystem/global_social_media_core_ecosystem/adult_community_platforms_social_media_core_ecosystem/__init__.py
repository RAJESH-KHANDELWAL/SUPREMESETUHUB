"""Adult Community Platforms platform Core metadata facade."""
from ..module_service import SocialMediaPlatformService
class PlatformManager(SocialMediaPlatformService):
    PLATFORM_ID="adult_community_platforms"
def get_manager()->PlatformManager:return PlatformManager()
__all__=["PlatformManager","get_manager"]
