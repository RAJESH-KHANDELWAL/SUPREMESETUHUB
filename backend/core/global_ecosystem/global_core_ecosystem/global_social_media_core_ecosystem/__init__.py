"""Public interface for the Global Social Media Core control plane."""
from .catalog import SOCIAL_MEDIA_CORE_ECOSYSTEM, get_social_media_core_catalog
from .contracts import CoreResult, Readiness, SecretReference, TenantContext
from .domain_catalog import domain_summary, list_domain_inventory
from .module_service import SocialMediaPlatformCoreService
from .orchestrator import GlobalSocialMediaCoreOrchestrator
from .platform_catalog import get_platform, list_platforms, platform_summary
from .policy import SocialMediaCorePolicy, SocialMediaCorePolicyError
from .service import GlobalSocialMediaCoreService

__all__ = [
    "SOCIAL_MEDIA_CORE_ECOSYSTEM", "get_social_media_core_catalog",
    "CoreResult", "Readiness", "SecretReference", "TenantContext",
    "domain_summary", "list_domain_inventory",
    "SocialMediaPlatformCoreService", "GlobalSocialMediaCoreOrchestrator",
    "get_platform", "list_platforms", "platform_summary",
    "SocialMediaCorePolicy", "SocialMediaCorePolicyError",
    "GlobalSocialMediaCoreService",
]
