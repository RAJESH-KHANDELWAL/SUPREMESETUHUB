"""System provider, product and domain discovery orchestration."""
from __future__ import annotations
from typing import Any
from .catalog import get_system_core_catalog, list_system_providers
from .domain_catalog import system_domain_summary, list_system_domain_inventory
from .product_catalog import list_system_products, system_products_summary
from .policy import SystemCorePolicy


class SystemCoreOrchestrator:
    def catalog(self) -> dict[str, Any]:
        return get_system_core_catalog()

    def list_providers(self) -> dict[str, Any]:
        providers = [SystemCorePolicy.safe_summary(p) for p in list_system_providers()]
        return {"success": True, "count": len(providers), "providers": providers}

    def get_provider(self, provider_id: str) -> dict[str, Any] | None:
        needle = provider_id.strip().casefold()
        return next((p for p in list_system_providers() if p["provider_id"].casefold() == needle), None) if needle else None

    def list_products(self, *, provider_id: str | None = None, enabled_only: bool = False) -> dict[str, Any]:
        products = list_system_products(provider_id=provider_id, enabled_only=enabled_only)
        return {"success": True, "count": len(products), "products": products}

    def get_product(self, product_id: str) -> dict[str, Any] | None:
        from .product_catalog import get_system_product
        return get_system_product(product_id)

    def domains(self) -> dict[str, Any]:
        return system_domain_summary()

    def domain_inventory(self) -> list[dict[str, Any]]:
        return list_system_domain_inventory()

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        summary = system_domain_summary()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            "provider_count": len(catalog["providers"]),
            "product_count": summary["product_count"],
            "domain_count": summary["domain_count"],
            "unassigned_product_count": summary["unassigned_product_count"],
            "live_connections_verified": 0,
            "host_operations_performed": 0,
            "warning": "Inventory and readiness metadata do not prove installation, support entitlement, API availability or a live host connection.",
        }

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True,
            "dependencies": [
                {"from": "GLOBAL_SYSTEM_CORE_ECOSYSTEM", "to": "GLOBAL_API_ECOSYSTEM", "relationship": "OPTIONAL_PROVIDER_CONTROL_APIS"},
                {"from": "GLOBAL_SYSTEM_CORE_ECOSYSTEM", "to": "GLOBAL_SECURITY_CORE_ECOSYSTEM", "relationship": "SECURITY_POLICY_REFERENCE"},
                {"from": "GLOBAL_SYSTEM_CORE_ECOSYSTEM", "to": "GLOBAL_SERVER_CORE_ECOSYSTEM", "relationship": "HOST_PLATFORM_REFERENCE"},
                {"from": "GLOBAL_SYSTEM_CORE_ECOSYSTEM", "to": "GLOBAL_SOFTWARE_CORE_ECOSYSTEM", "relationship": "SOFTWARE_COMPATIBILITY_REFERENCE"},
            ],
            "api_calls_performed": 0,
        }
