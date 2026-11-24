"""Canonical Python entry point for Global Social Media Core."""
from typing import Any
from .service import SocialMediaCoreService
from .domain_runtime import SocialMediaCoreDomainManager
from .product_catalog import list_social_media_platforms,get_social_media_platform
class SocialMediaCoreManager(SocialMediaCoreService):
    def list_platform_inventory(self)->list[dict[str,Any]]:return list_social_media_platforms()
    def get_platform_manager(self,platform_id:str):
        item=get_social_media_platform(platform_id)
        if item is None:raise LookupError(f"SOCIAL_MEDIA_PLATFORM_NOT_REGISTERED: {platform_id}")
        module=__import__(f"{__package__}.{item['platform_id']}_social_media_core_ecosystem",fromlist=["get_manager"]);return module.get_manager()
    def get_domain_manager(self,domain_id:str)->SocialMediaCoreDomainManager:return SocialMediaCoreDomainManager(domain_id)
def get_manager()->SocialMediaCoreManager:return SocialMediaCoreManager()
__all__=["SocialMediaCoreManager","get_manager"]
