"""ShareChat platform-family Core service facade."""
from ...module_service import SocialMediaPlatformCoreService

class PlatformCoreService(SocialMediaPlatformCoreService):
    PLATFORM_ID = "sharechat"

    def __init__(self) -> None:
        super().__init__(self.PLATFORM_ID)
