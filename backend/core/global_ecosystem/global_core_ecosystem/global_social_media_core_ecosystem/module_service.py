"""Reusable read-only Core service for a social platform family."""
from __future__ import annotations
from typing import Any
from .contracts import CoreResult, Readiness, TenantContext
from .platform_catalog import get_platform
from .policy import SocialMediaCorePolicy

class SocialMediaPlatformCoreService:
    """Expose platform identity and capability metadata; never call provider APIs."""
    CAPABILITIES = (
        "PLATFORM_IDENTITY_METADATA", "ACCOUNT_CONNECTION_METADATA",
        "PROFILE_METADATA_BOUNDARY", "CONTENT_CAPABILITY_METADATA",
        "PUBLISHING_WORKFLOW_BOUNDARY", "COMMUNITY_INTERACTION_BOUNDARY",
    )

    def __init__(self, platform_id: str) -> None:
        self.platform = get_platform(platform_id)
        self.platform_id = self.platform["id"]

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            "ecosystem_id": f"SOCIAL-{self.platform_id.upper().replace('_','-')}-CORE-ECOSYSTEM",
            "platform": self.platform["name"],
            "category": self.platform["category"],
            "api_access_hint": self.platform["api_access"],
            "core_layer": "GLOBAL_SOCIAL_MEDIA_CORE",
            "readiness": Readiness.CATALOG_ONLY.value,
            "connected": False,
            "live_connection_verified": False,
            "api_call_performed": False,
        }

    def capabilities(self) -> dict[str, Any]:
        return {
            "success": True,
            "platform_id": self.platform_id,
            "count": len(self.CAPABILITIES),
            "capabilities": [{"name": item, "authorization_class": SocialMediaCorePolicy.classify_capability(item)} for item in self.CAPABILITIES],
        }

    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str, Any]:
        try:
            caller = SocialMediaCorePolicy.require_tenant_context(context)
            SocialMediaCorePolicy.validate_platform(self.platform_id)
            SocialMediaCorePolicy.validate_capability(capability, self.CAPABILITIES)
        except (ValueError, PermissionError, LookupError) as exc:
            return CoreResult(False, f"SOCIAL-{self.platform_id.upper()}-CORE-ECOSYSTEM", "POLICY_DENIED", errors=[str(exc)], request_id=getattr(context, "request_id", None)).to_dict()
        return CoreResult(
            True, f"SOCIAL-{self.platform_id.upper()}-CORE-ECOSYSTEM",
            "CORE_POLICY_PASSED_PROVIDER_AUTH_STILL_REQUIRED",
            data={"capability": capability, "tenant_id": caller.tenant_id, "actor_id": caller.actor_id, "authorization_class": SocialMediaCorePolicy.classify_capability(capability), "provider_api_call_performed": False},
            request_id=caller.request_id,
        ).to_dict()
