"""Stripe Core discovery, domain mapping and dependency orchestration."""
from __future__ import annotations

from typing import Any

from .catalog import get_stripe_core_catalog, list_stripe_core_modules
from .domain_catalog import list_stripe_domain_inventory, stripe_domain_summary
from .master_catalog import get_master_catalog_status
from .policy import StripeCorePolicy


class StripeCoreOrchestrator:
    """Coordinate Stripe metadata only; never execute provider operations."""

    def catalog(self) -> dict[str, Any]:
        return get_stripe_core_catalog()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        modules = list_stripe_core_modules(include_disabled=not enabled_only)
        safe = [StripeCorePolicy.safe_metadata(item) for item in modules]
        return {"success": True, "count": len(safe), "products": safe}

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        needle = ecosystem_id.strip().casefold()
        if not needle:
            return None
        for item in list_stripe_core_modules(include_disabled=True):
            if needle in {
                item["ecosystem_id"].casefold(),
                item["name"].casefold(),
                item["module"].casefold(),
                item["api_family"].casefold(),
            }:
                return StripeCorePolicy.safe_metadata(item)
        return None

    def domains(self) -> dict[str, Any]:
        return stripe_domain_summary()

    def domain_inventory(self) -> list[dict[str, Any]]:
        return list_stripe_domain_inventory()

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        modules = catalog["children"]
        domains = stripe_domain_summary()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            "service_family_count": len(modules),
            "enabled_service_family_count": sum(bool(item.get("enabled", True)) for item in modules),
            "domain_count": domains["domain_count"],
            "api_adapter_references": sum(bool(item.get("api_catalog_ref")) for item in modules),
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "warning": "Catalog registration and domain mapping do not prove Stripe account eligibility, authorization or live connectivity.",
        }

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True,
            "edges": [
                {
                    "core_module": item["core_module"],
                    "api_catalog_ref": item["api_catalog_ref"],
                    "relationship": "CORE_METADATA_DELEGATES_TO_API_ADAPTER",
                    "transport_owned_by": "STRIPE_API_ECOSYSTEM",
                }
                for item in list_stripe_core_modules(include_disabled=True)
            ],
        }

    def master_catalog_reference(self) -> dict[str, Any]:
        return get_master_catalog_status()


__all__ = ["StripeCoreOrchestrator"]
