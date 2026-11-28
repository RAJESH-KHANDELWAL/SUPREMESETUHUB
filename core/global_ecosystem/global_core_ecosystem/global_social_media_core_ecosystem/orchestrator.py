"""Platform and domain discovery orchestration."""
from typing import Any
from .catalog import get_social_media_core_catalog
from .domain_catalog import social_media_domain_summary,list_social_media_domain_inventory
from .product_catalog import list_social_media_platforms,get_social_media_platform,social_media_platform_summary
from .policy import SocialMediaCorePolicy
class SocialMediaCoreOrchestrator:
    def catalog(self)->dict[str,Any]:return get_social_media_core_catalog()
    def list_platforms(self,*,domain_id:str|None=None,adult_only:bool|None=None)->dict[str,Any]:
        items=[SocialMediaCorePolicy.safe_platform_summary(x) for x in list_social_media_platforms(domain_id=domain_id,adult_only=adult_only)];return {"success":True,"count":len(items),"platforms":items}
    def get_platform(self,platform_id:str)->dict[str,Any]|None:
        item=get_social_media_platform(platform_id);return SocialMediaCorePolicy.safe_platform_summary(item) if item else None
    def domains(self)->dict[str,Any]:return social_media_domain_summary()
    def domain_inventory(self)->list[dict[str,Any]]:return list_social_media_domain_inventory()
    def health(self)->dict[str,Any]:
        s=social_media_platform_summary();return {"success":True,**s,"status":"CORE_CATALOG_AVAILABLE","api_transport_in_core":False,"credential_storage":"EXTERNAL_SECRET_STORE_ONLY"}
    def dependency_map(self)->dict[str,Any]:return {"success":True,"dependencies":{"platform_inventory":"product_ecosystem_index.json","domain_taxonomy":"domain_catalog.py","authentication_and_api_transport":"separate API layer","durable_records":"separate storage/database layer","moderation_enforcement":"dedicated safety services"}}
