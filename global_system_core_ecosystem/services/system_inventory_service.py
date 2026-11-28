"""Read-only inventory service for operating-system families."""
from __future__ import annotations
from typing import Any
from ..catalog import list_system_providers
from ..product_catalog import list_system_products


class SystemInventoryService:
    def providers(self) -> dict[str, Any]:
        records = list_system_providers()
        return {"success": True, "count": len(records), "providers": records}

    def products(self, provider_id: str | None = None) -> dict[str, Any]:
        records = list_system_products(provider_id=provider_id)
        return {"success": True, "count": len(records), "products": records}

    def summary(self) -> dict[str, Any]:
        return {
            "success": True,
            "provider_count": len(list_system_providers()),
            "product_count": len(list_system_products()),
            "mutations_performed": 0,
        }
