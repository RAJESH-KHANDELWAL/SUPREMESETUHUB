"""Read-only provider and product Core facades."""
from __future__ import annotations
from typing import Any
from .catalog import get_system_core_catalog
from .contracts import SystemCoreResult, SystemReadiness, SystemTenantContext
from .policy import SystemCorePolicy
from .product_catalog import get_system_product, list_system_products


class SystemProviderCoreService:
    PROVIDER_ID = ""

    def __init__(self, provider_id: str | None = None) -> None:
        self.provider_id = (provider_id or self.PROVIDER_ID).strip().casefold()
        if not self.provider_id:
            raise ValueError("SYSTEM_PROVIDER_ID_REQUIRED")
        providers = get_system_core_catalog()["providers"]
        self._provider = next((p for p in providers if p["provider_id"] == self.provider_id), None)
        if self._provider is None:
            raise LookupError(f"SYSTEM_PROVIDER_NOT_REGISTERED: {self.provider_id}")

    def status(self) -> dict[str, Any]:
        return {
            **SystemCorePolicy.safe_summary(self._provider),
            "success": True,
            "readiness": SystemReadiness.CATALOG_ONLY.value,
            "product_count": len(list_system_products(provider_id=self.provider_id)),
            "api_transport_in_core": False,
            "live_connection_verified": False,
        }

    def list_products(self) -> dict[str, Any]:
        products = list_system_products(provider_id=self.provider_id)
        return {"success": True, "provider_id": self.provider_id, "count": len(products), "products": products}


class SystemProductCoreService:
    PRODUCT_ID = ""

    def __init__(self, product_id: str | None = None) -> None:
        self.product_id = (product_id or self.PRODUCT_ID).strip()
        self._product = get_system_product(self.product_id)
        if self._product is None:
            raise LookupError(f"SYSTEM_PRODUCT_NOT_REGISTERED: {self.product_id}")

    def status(self) -> dict[str, Any]:
        return {
            **SystemCorePolicy.safe_summary(self._product),
            "success": True,
            "readiness": SystemReadiness.CATALOG_ONLY.value,
            "live_connection_verified": False,
            "system_changes_performed": False,
        }

    def authorize_metadata_access(self, context: SystemTenantContext | None) -> dict[str, Any]:
        try:
            SystemCorePolicy.require_tenant_context(context)
        except (ValueError, PermissionError) as exc:
            return SystemCoreResult(False, "GLOBAL-SYSTEM-CORE-ECOSYSTEM", "POLICY_DENIED", errors=[str(exc)]).to_dict()
        return SystemCoreResult(
            True, "GLOBAL-SYSTEM-CORE-ECOSYSTEM", "CORE_POLICY_PASSED_NO_HOST_ACTION",
            data={"product_id": self.product_id, "tenant_id": context.tenant_id, "actor_id": context.actor_id, "host_action_performed": False},
            request_id=context.request_id,
        ).to_dict()
