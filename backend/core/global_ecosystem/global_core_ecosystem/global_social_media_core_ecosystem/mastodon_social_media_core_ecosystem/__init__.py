"""Mastodon Social Media Core package."""
from .service import PlatformCoreService

PLATFORM_ID = "mastodon"
ECOSYSTEM_ID = "SOCIAL-MASTODON-CORE-ECOSYSTEM"

__all__ = ["PLATFORM_ID", "ECOSYSTEM_ID", "PlatformCoreService"]
