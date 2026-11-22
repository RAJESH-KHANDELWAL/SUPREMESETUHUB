"""PayPal product and domain discovery orchestration."""
from __future__ import annotations
from typing import Any
from .catalog import get_paypal_core_catalog
from .domain_catalog import list_paypal_domain_inventory, paypal_domain_summary
from .policy import PayPalCorePolicy
from .product_catalog import get_paypal_product, list_paypal_products

class PayPalCoreOrchestrator:
    def catalog(self) -> dict[str, Any]:
        return get_paypal_core_catalog()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        products = list_paypal_products()
        if enabled_only:
            products = [item for item in products if item.get("enabled", True)]
        safe = [PayPalCorePolicy.safe_product_summary(item) for item in products]
        return {"success": True, "count": len(safe), "products": safe}

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        item = get_paypal_product(ecosystem_id)
        return PayPalCorePolicy.safe_product_summary(item) if item else None

    def domains(self) -> dict[str, Any]:
        return {"success": True, **paypal_domain_summary()}

    def domain_inventory(self) -> list[dict[str, Any]]:
        return list_paypal_domain_inventory()

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            "product_count": len(catalog["children"]),
            "domain_count": paypal_domain_summary()["count"],
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "api_transport_in_core": False,
        }

    def dependency_map(self) -> dict[str, Any]:
        catalog = self.catalog()
        return {
            "success": True,
            "provider_core": catalog["ecosystem_id"],
            "api_layer": catalog["api_catalog_ref"],
            "dependencies": [
                {"product": item["ecosystem_id"], "domain": item["domain_id"], "api_catalog_ref": item["api_catalog_ref"]}
                for item in list_paypal_products()
            ],
            "live_connection_verified": False,
        }
