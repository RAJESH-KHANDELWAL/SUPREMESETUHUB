"""Shared read-only service used by every PayPal product Core package."""
from __future__ import annotations
from typing import Any
from .contracts import CoreResult, Readiness, TenantContext
from .policy import PayPalCorePolicy
from .product_catalog import get_paypal_product
class PayPalProductCoreService:
    def __init__(self, ecosystem_id: str) -> None:
        product = get_paypal_product(ecosystem_id)
        if product is None: raise LookupError(f"PAYPAL_CORE_MODULE_NOT_REGISTERED: {ecosystem_id}")
        self._product = product
    def status(self) -> dict[str, Any]:
        return {"success": True, **PayPalCorePolicy.safe_product_summary(self._product), "core_layer": "PAYPAL_CORE", "api_transport_in_core": False, "readiness": Readiness.CATALOG_ONLY.value}
    def capabilities(self) -> dict[str, Any]:
        items = self._product["capabilities"]
        return {"success": True, "ecosystem_id": self._product["ecosystem_id"], "count": len(items), "capabilities": [{"name": item, "authorization_class": PayPalCorePolicy.classify_capability(item)} for item in items]}
    def evaluate_capability(self, capability: str, context: TenantContext | None) -> dict[str, Any]:
        try:
            PayPalCorePolicy.require_tenant_context(context)
            PayPalCorePolicy.validate_capability(self._product, capability)
        except (ValueError, PermissionError) as exc:
            return CoreResult(False, self._product["ecosystem_id"], "POLICY_DENIED", errors=[str(exc)], request_id=getattr(context,"request_id",None)).to_dict()
        return CoreResult(True, self._product["ecosystem_id"], "CORE_POLICY_PASSED_PROVIDER_AUTH_STILL_REQUIRED", data={"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,"authorization_class":PayPalCorePolicy.classify_capability(capability),"provider_api_call_performed":False}, request_id=context.request_id).to_dict()
