"""OpenAI Core product and domain discovery orchestration."""
from __future__ import annotations

from typing import Any

from .catalog import get_openai_core_catalog, get_openai_core_module, list_openai_core_modules
from .domain_catalog import openai_domain_summary, list_openai_domain_inventory
from .policy import OpenAICorePolicy
from .product_catalog import openai_offerings_summary


class OpenAICoreOrchestrator:
    """Coordinate catalog metadata only; no provider requests are made."""

    def catalog(self) -> dict[str, Any]:
        return get_openai_core_catalog()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        products = list_openai_core_modules()
        if enabled_only:
            products = tuple(item for item in products if item.get("enabled", True))
        safe = [OpenAICorePolicy.safe_summary(item) for item in products]
        return {"success": True, "count": len(safe), "products": safe}

    def get_product(self, product_id: str) -> dict[str, Any] | None:
        item = get_openai_core_module(product_id)
        return OpenAICorePolicy.safe_summary(item) if item else None

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        domains = openai_domain_summary()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            "product_family_count": len(catalog["children"]),
            "domain_count": domains["domain_count"],
            "domain_product_memberships": domains["domain_product_memberships"],
            "api_capability_count": catalog["api_capability_count"],
            "enabled_product_family_count": sum(bool(item.get("enabled", True)) for item in catalog["children"]),
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "warning": "Catalog readiness does not prove API entitlement, account access or live OpenAI connectivity.",
        }

    def offerings(self) -> dict[str, Any]:
        return openai_offerings_summary()

    def get_offering(self, product_id: str) -> dict[str, Any] | None:
        return next(
            (item for item in list_openai_domain_inventory() if item["id"].casefold() == str(product_id).strip().casefold()),
            None,
        )

    def domains(self) -> dict[str, Any]:
        return openai_domain_summary()

    def domain_inventory(self) -> list[dict[str, Any]]:
        return list_openai_domain_inventory()

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True,
            "edges": [
                {
                    "core_module": item["core_module"],
                    "api_catalog_ref": item["api_catalog_ref"],
                    "relationship": "DELEGATES_TO_API_LAYER",
                    "api_transport_in_core": False,
                }
                for item in list_openai_core_modules()
            ],
        }


__all__ = ["OpenAICoreOrchestrator"]
