"""Lemmy Social Media Core package."""
from .service import PlatformCoreService

PLATFORM_ID = "lemmy"
ECOSYSTEM_ID = "SOCIAL-LEMMY-CORE-ECOSYSTEM"

__all__ = ["PLATFORM_ID", "ECOSYSTEM_ID", "PlatformCoreService"]
