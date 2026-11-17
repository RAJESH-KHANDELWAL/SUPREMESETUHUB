"""Other lawful age-restricted creator and adult communities platform-family Core service facade."""
from ...module_service import SocialMediaPlatformCoreService

class PlatformCoreService(SocialMediaPlatformCoreService):
    PLATFORM_ID = "adult_community_platforms"

    def __init__(self) -> None:
        super().__init__(self.PLATFORM_ID)
