"""Social platform metadata policy; does not authenticate or execute provider actions."""
from typing import Any
from .contracts import TenantContext
_SECRET=("access_token","refresh_token","client_secret","password","authorization","cookie","private_key","api_key")
class SocialMediaCorePolicy:
    @staticmethod
    def safe_platform_summary(item:dict[str,Any])->dict[str,Any]:
        keys=("platform_id","platform_name","domain_id","category","core_path","status","age_classification","adult_only_18_plus","availability","live_connection_verified","api_transport_in_core","capabilities")
        return {k:item[k] for k in keys if k in item}
    @staticmethod
    def require_tenant_context(context:TenantContext|None)->None:
        if context is None:raise ValueError("TENANT_CONTEXT_REQUIRED")
        context.validate()
    @staticmethod
    def validate_capability(item:dict[str,Any],capability:str)->None:
        if capability not in item.get("capabilities",[]):raise PermissionError("CAPABILITY_NOT_REGISTERED")
    @staticmethod
    def redact(value:Any)->Any:
        if isinstance(value,dict):return {k:("[REDACTED]" if any(s in k.casefold() for s in _SECRET) else SocialMediaCorePolicy.redact(v)) for k,v in value.items()}
        if isinstance(value,list):return [SocialMediaCorePolicy.redact(v) for v in value]
        return value
    @staticmethod
    def age_gate(item:dict[str,Any])->str:
        return "AGE_VERIFICATION_AND_LOCAL_LAW_REVIEW_REQUIRED" if item.get("adult_only_18_plus") else "PROVIDER_AND_JURISDICTION_RULES_APPLY"
