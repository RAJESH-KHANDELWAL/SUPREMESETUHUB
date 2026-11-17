"""Public service facade for the Global Social Media Core Ecosystem."""
from __future__ import annotations
from typing import Any
from .catalog import get_social_media_core_catalog
from .domain_catalog import domain_summary
from .module_service import SocialMediaPlatformCoreService
from .orchestrator import GlobalSocialMediaCoreOrchestrator
from .platform_catalog import get_platform, list_platforms, platform_summary

class GlobalSocialMediaCoreService:
    def __init__(self) -> None:
        self.orchestrator = GlobalSocialMediaCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            "ecosystem_id": "GLOBAL-SOCIAL-MEDIA-CORE-ECOSYSTEM",
            "name": "GLOBAL SOCIAL MEDIA CORE ECOSYSTEM",
            "status": "REGISTERED",
            "readiness": "CORE_CATALOG_ONLY",
            "platforms": platform_summary(),
            "domains": domain_summary(),
            "live_connections_verified": 0,
            "api_transport_in_core": False,
        }

    def list_platforms(self) -> list[dict[str, Any]]:
        return list_platforms()

    def get_platform(self, platform_id: str) -> dict[str, Any]:
        return get_platform(platform_id)

    def platform_service(self, platform_id: str) -> SocialMediaPlatformCoreService:
        return SocialMediaPlatformCoreService(platform_id)

    def catalog(self) -> dict[str, Any]:
        return get_social_media_core_catalog()
