"""PeerTube Social Media Core package."""
from .service import PlatformCoreService

PLATFORM_ID = "peertube"
ECOSYSTEM_ID = "SOCIAL-PEERTUBE-CORE-ECOSYSTEM"

__all__ = ["PLATFORM_ID", "ECOSYSTEM_ID", "PlatformCoreService"]
