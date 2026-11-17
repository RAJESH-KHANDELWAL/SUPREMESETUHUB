"""Hive Social platform-family Core service facade."""
from ...module_service import SocialMediaPlatformCoreService

class PlatformCoreService(SocialMediaPlatformCoreService):
    PLATFORM_ID = "hive_social"

    def __init__(self) -> None:
        super().__init__(self.PLATFORM_ID)
