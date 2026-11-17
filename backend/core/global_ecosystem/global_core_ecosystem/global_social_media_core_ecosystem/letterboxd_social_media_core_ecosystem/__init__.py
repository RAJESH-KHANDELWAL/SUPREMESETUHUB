"""Letterboxd Social Media Core package."""
from .service import PlatformCoreService

PLATFORM_ID = "letterboxd"
ECOSYSTEM_ID = "SOCIAL-LETTERBOXD-CORE-ECOSYSTEM"

__all__ = ["PLATFORM_ID", "ECOSYSTEM_ID", "PlatformCoreService"]
