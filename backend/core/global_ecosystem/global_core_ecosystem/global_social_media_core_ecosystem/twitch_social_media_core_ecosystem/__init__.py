"""Twitch Social Media Core package."""
from .service import PlatformCoreService

PLATFORM_ID = "twitch"
ECOSYSTEM_ID = "SOCIAL-TWITCH-CORE-ECOSYSTEM"

__all__ = ["PLATFORM_ID", "ECOSYSTEM_ID", "PlatformCoreService"]
