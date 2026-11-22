"""Shared read-only service for OpenAI product Core packages."""
from __future__ import annotations

from typing import Any

from .catalog import get_openai_core_module
from .contracts import CoreResult, Readiness, TenantContext
from .policy import OpenAICorePolicy


class OpenAIProductCoreService:
    """Expose product identity and policy-aware metadata; never call OpenAI APIs."""

    ECOSYSTEM_ID = ""

    def __init__(self) -> None:
        if not self.ECOSYSTEM_ID:
            raise NotImplementedError("Product service must define ECOSYSTEM_ID")
        self._product = get_openai_core_module(self.ECOSYSTEM_ID)
        if self._product is None:
            raise LookupError(f"OPENAI_CORE_PRODUCT_NOT_REGISTERED: {self.ECOSYSTEM_ID}")

    def status(self) -> dict[str, Any]:
        product = OpenAICorePolicy.safe_summary(self._product)
        status = product["status"]
        readiness = {
            "active_catalog": Readiness.CATALOG_ONLY.value,
            "availability_dependent_catalog": Readiness.AVAILABILITY_DEPENDENT.value,
            "public_beta_catalog": Readiness.PUBLIC_BETA.value,
            "retired_reference_only": Readiness.RETIRED.value,
        }.get(status, Readiness.CATALOG_ONLY.value)
        return {
            "success": True,
            **product,
            "core_layer": "OPENAI_CORE",
            "readiness": readiness,
            "api_transport_in_core": False,
            "live_connection_verified": False,
            "api_calls_performed": 0,
        }

    def capabilities(self) -> dict[str, Any]:
        capabilities = self._product.get("capabilities", [])
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "count": len(capabilities),
            "capabilities": [
                {
                    "name": item,
                    "authorization_class": OpenAICorePolicy.classify_capability(item),
                }
                for item in capabilities
            ],
        }

    def authorize_capability(
        self, capability: str, context: TenantContext | None
    ) -> dict[str, Any]:
        try:
            OpenAICorePolicy.require_tenant_context(context)
            OpenAICorePolicy.validate_capability(self._product, capability)
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
                "authorization_class": OpenAICorePolicy.classify_capability(capability),
                "api_call_performed": False,
            },
            request_id=context.request_id,
        ).to_dict()


__all__ = ["OpenAIProductCoreService"]
