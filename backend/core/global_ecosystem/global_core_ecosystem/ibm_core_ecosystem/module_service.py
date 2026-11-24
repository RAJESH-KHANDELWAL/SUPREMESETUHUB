"""Shared read-only service for IBM product-family Core packages."""
from __future__ import annotations
from typing import Any
from .product_catalog import get_product
from .contracts import CoreResult, TenantContext
from .policy import IBMCorePolicy
class IBMProductCoreService:
    PRODUCT_ID=""
    def __init__(self, product_id: str | None = None) -> None:
        key=product_id or self.PRODUCT_ID
        self._product=get_product(key) if key else None
        if self._product is None: raise LookupError(f"IBM_CORE_PRODUCT_NOT_REGISTERED: {key}")
    def status(self) -> dict[str,Any]:
        return {**IBMCorePolicy.sanitize(self._product),"core_layer":"IBM_CORE","api_transport_in_core":False,"engine_execution_in_core":False,"live_connection_verified":False}
    def capabilities(self) -> dict[str,Any]:
        items=self._product["capabilities"]
        return {"success":True,"product_id":self._product["product_id"],"count":len(items),"capabilities":[{"name":x,"authorization_class":IBMCorePolicy.classify_capability(x)} for x in items]}
    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str,Any]:
        try:
            IBMCorePolicy.require_tenant_context(context)
            IBMCorePolicy.validate_capability(self._product,capability)
        except (ValueError,PermissionError) as exc:
            return CoreResult(False,self._product["product_id"],"POLICY_DENIED",errors=[str(exc)],request_id=getattr(context,"request_id",None)).to_dict()
        return CoreResult(True,self._product["product_id"],"CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED",data={"capability":capability,"tenant_id":context.tenant_id,"actor_id":context.actor_id,"api_call_performed":False},request_id=context.request_id).to_dict()
