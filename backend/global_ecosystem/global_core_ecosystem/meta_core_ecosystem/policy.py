"""Meta Core authorization, OAuth and privacy policy guardrails."""
from __future__ import annotations
from typing import Any
SENSITIVE_MARKERS=("ADMIN","DELETE","WRITE","PUBLISH","SEND","MESSAGE","ADS","BILLING","IAM","PERMISSION","ASSET_ASSIGN","TOKEN","WEBHOOK","BUSINESS")
BLOCKED_SECRET_KEYS={"token","access_token","refresh_token","client_secret","app_secret","appsecret_proof","api_key","apikey","secret","secret_value","authorization","password","verification_token"}
class MetaCorePolicyError(PermissionError): pass
class MetaCorePolicy:
    @staticmethod
    def require_tenant_context(context:Any)->None:
        if context is None: raise MetaCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator=getattr(context,"validate",None)
        if not callable(validator): raise MetaCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()
    @staticmethod
    def validate_capability(product:dict[str,Any],capability:str)->None:
        if not product.get("enabled",True): raise MetaCorePolicyError("PRODUCT_DISABLED")
        if product.get("status")=="DISCOVERY_ONLY": raise MetaCorePolicyError("DISCOVERY_ONLY_PRODUCT_NO_API_CAPABILITY")
        if capability not in set(product.get("capabilities",[])): raise MetaCorePolicyError("CAPABILITY_NOT_REGISTERED")
    @staticmethod
    def classify_capability(capability:str)->str:
        upper=capability.upper()
        return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(x in upper for x in SENSITIVE_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
    @staticmethod
    def sanitize(value:Any)->Any:
        if isinstance(value,dict): return {k:MetaCorePolicy.sanitize(v) for k,v in value.items() if str(k).casefold() not in BLOCKED_SECRET_KEYS}
        if isinstance(value,list): return [MetaCorePolicy.sanitize(x) for x in value]
        if isinstance(value,tuple): return [MetaCorePolicy.sanitize(x) for x in value]
        return value
