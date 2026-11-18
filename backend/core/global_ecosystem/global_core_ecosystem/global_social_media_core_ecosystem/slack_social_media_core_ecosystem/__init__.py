"""Slack Social Media Core package."""
from .service import PlatformCoreService

PLATFORM_ID = "slack"
ECOSYSTEM_ID = "SOCIAL-SLACK-CORE-ECOSYSTEM"

__all__ = ["PLATFORM_ID", "ECOSYSTEM_ID", "PlatformCoreService"]
