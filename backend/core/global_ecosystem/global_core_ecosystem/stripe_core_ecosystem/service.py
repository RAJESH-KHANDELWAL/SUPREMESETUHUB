"""Read-only Stripe Core registry service."""
from __future__ import annotations

from typing import Any

from .catalog import get_stripe_core_catalog, list_stripe_core_modules


class StripeCoreEcosystemService:
    NAME = "STRIPE CORE ECOSYSTEM"

    def status(self) -> dict[str, Any]:
        catalog = get_stripe_core_catalog()
        modules = catalog["children"]
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "name": self.NAME,
            "provider": "stripe",
            "status": catalog["status"],
            "module_count": len(modules),
            "connected_modules": sum(1 for module in modules if module.get("connected") is True),
            "live_connection_verified": catalog["live_connection_verified"],
            "api_catalog_ref": catalog["api_catalog_ref"],
        }

    def list_modules(self, include_disabled: bool = False) -> dict[str, Any]:
        modules = list_stripe_core_modules(include_disabled=include_disabled)
        return {"success": True, "count": len(modules), "modules": modules}

    def get_module(self, module_id: str) -> dict[str, Any] | None:
        key = module_id.strip().casefold()
        for module in list_stripe_core_modules(include_disabled=True):
            if module["ecosystem_id"].casefold() == key or module["module"].casefold() == key or module["api_family"].casefold() == key:
                return module
        return None

    def health(self) -> dict[str, Any]:
        catalog = get_stripe_core_catalog()
        return {
            "success": True,
            "registered": catalog["status"] == "REGISTERED",
            "enabled": bool(catalog["enabled"]),
            "api_catalog_available": bool(catalog["api_catalog_ref"]),
            "live_connection_verified": False,
            "status": "CORE_CATALOG_READY_NOT_LIVE_CONNECTED",
        }


__all__ = ["StripeCoreEcosystemService"]
