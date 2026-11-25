"""Reusable read-only manager for a registered social platform package."""
from typing import Any
from .catalog import SOCIAL_MEDIA_CORE_ECOSYSTEM
from .contracts import CoreResult,TenantContext
from .policy import SocialMediaCorePolicy
from .product_catalog import get_social_media_platform
class SocialMediaPlatformService:
    PLATFORM_ID=""
    def __init__(self)->None:
        if not self.PLATFORM_ID:raise NotImplementedError("Platform manager must define PLATFORM_ID")
        self.platform=get_social_media_platform(self.PLATFORM_ID)
        if self.platform is None:raise LookupError(f"SOCIAL_MEDIA_PLATFORM_NOT_REGISTERED: {self.PLATFORM_ID}")
    def status(self)->dict[str,Any]:
        return {"success":True,**SocialMediaCorePolicy.safe_platform_summary(self.platform),"core_layer":"SOCIAL_MEDIA_CORE","age_policy":SocialMediaCorePolicy.age_gate(self.platform),"api_transport_in_core":False,"live_connection_verified":False}
    def capabilities(self)->dict[str,Any]:return {"success":True,"platform_id":self.PLATFORM_ID,"capabilities":list(self.platform["capabilities"])}
    def authorize_capability(self,capability:str,context:TenantContext|None)->dict[str,Any]:
        try:SocialMediaCorePolicy.require_tenant_context(context);SocialMediaCorePolicy.validate_capability(self.platform,capability)
        except (ValueError,PermissionError) as exc:return CoreResult(False,SOCIAL_MEDIA_CORE_ECOSYSTEM["ecosystem_id"],"POLICY_DENIED",errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
        return CoreResult(True,SOCIAL_MEDIA_CORE_ECOSYSTEM["ecosystem_id"],"CORE_POLICY_PASSED_PROVIDER_AUTH_STILL_REQUIRED",data={"platform_id":self.PLATFORM_ID,"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,"api_call_performed":False},request_id=context.request_id).to_dict()
