"""Shared read-only Core service for Google product families."""
from __future__ import annotations

from typing import Any

from .catalog import get_google_core_catalog
from .contracts import CoreResult, Readiness, TenantContext
from .policy import GoogleCorePolicy


class GoogleProductCoreService:
    """Expose a product's Core identity and policy-aware capability metadata.

    This class never performs network I/O, OAuth, token storage or Google API
    calls. A product API adapter must be invoked by the application/API layer.
    """

    ECOSYSTEM_ID = ""

    def __init__(self) -> None:
        if not self.ECOSYSTEM_ID:
            raise NotImplementedError("Product service must define ECOSYSTEM_ID")
        self._module = self._find_module(self.ECOSYSTEM_ID)

    @staticmethod
    def _find_module(ecosystem_id: str) -> dict[str, Any]:
        for item in get_google_core_catalog()["children"]:
            if item["ecosystem_id"] == ecosystem_id:
                return item
        raise LookupError(f"GOOGLE_CORE_MODULE_NOT_REGISTERED: {ecosystem_id}")

    def status(self) -> dict[str, Any]:
        module = GoogleCorePolicy.safe_module_summary(self._module)
        return {
            "success": True,
            **module,
            "core_layer": "GOOGLE_CORE",
            "api_transport_in_core": False,
            "live_connection_verified": False,
            "readiness": self._readiness(),
        }

    def _readiness(self) -> str:
        if not self._module.get("enabled", True):
            return Readiness.DISABLED.value
        status = self._module.get("status", Readiness.CATALOG_ONLY.value)
        if status == Readiness.READY.value:
            return Readiness.READY.value
        if status == Readiness.ADAPTER_SCAFFOLD.value:
            return Readiness.ADAPTER_SCAFFOLD.value
        return Readiness.CATALOG_ONLY.value

    def capabilities(self) -> dict[str, Any]:
        capabilities = self._module.get("capabilities", [])
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "count": len(capabilities),
            "capabilities": [
                {
                    "name": item,
                    "authorization_class": GoogleCorePolicy.classify_capability(item),
                }
                for item in capabilities
            ],
        }

    def authorize_capability(
        self, capability: str, context: TenantContext | None
    ) -> CoreResult:
        try:
            GoogleCorePolicy.require_tenant_context(context)
            GoogleCorePolicy.validate_capability(self._module, capability)
        except (ValueError, PermissionError) as exc:
            return CoreResult(
                success=False,
                ecosystem_id=self.ECOSYSTEM_ID,
                status="POLICY_DENIED",
                errors=[str(exc)],
                request_id=getattr(context, "request_id", None),
            ).to_dict()
        return CoreResult(
            success=True,
            ecosystem_id=self.ECOSYSTEM_ID,
            status="CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED",
            data={
                "capability": capability,
                "tenant_id": context.tenant_id,
                "actor_id": context.actor_id,
                "authorization_class": GoogleCorePolicy.classify_capability(capability),
                "api_call_performed": False,
            },
            request_id=context.request_id,
        ).to_dict()
