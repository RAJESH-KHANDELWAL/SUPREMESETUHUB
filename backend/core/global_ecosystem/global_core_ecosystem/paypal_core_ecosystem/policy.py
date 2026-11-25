"""PayPal Core metadata guardrails; never authorizes provider API operations."""
from __future__ import annotations
from typing import Any
SENSITIVE_MARKERS = ("CAPTURE","REFUND","PAYOUT","DISPUTE","VAULT","DELETE","WRITE","BILLING","MERCHANT","ONBOARD","WEBHOOK")
class PayPalCorePolicyError(PermissionError): pass
class PayPalCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None: raise PayPalCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator = getattr(context, "validate", None)
        if not callable(validator): raise PayPalCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()
    @staticmethod
    def validate_capability(product: dict[str, Any], capability: str) -> None:
        if not product.get("enabled", True): raise PayPalCorePolicyError("MODULE_DISABLED")
        if capability not in set(product.get("capabilities", [])): raise PayPalCorePolicyError("CAPABILITY_NOT_REGISTERED")
    @staticmethod
    def classify_capability(capability: str) -> str:
        upper = capability.upper()
        return "SENSITIVE_REQUIRES_EXTERNAL_AUTHORIZATION_AND_AUDIT" if any(x in upper for x in SENSITIVE_MARKERS) else "METADATA_DISCOVERY_ONLY"
    @staticmethod
    def safe_product_summary(product: dict[str, Any]) -> dict[str, Any]:
        allowed = ("ecosystem_id","name","package","description","domain_id","capabilities","status","enabled","connected","core_module","api_catalog_ref")
        return {key: product[key] for key in allowed if key in product} | {"live_connection_verified": False}
