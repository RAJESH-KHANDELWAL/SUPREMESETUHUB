"""Cultural Core discovery, inventory and dependency orchestration."""
from __future__ import annotations

from typing import Any

from .catalog import get_cultural_core_catalog
from .domain_catalog import domain_summary, get_domain, list_domains
from .resource_catalog import resource_inventory_summary


class CulturalCoreOrchestrator:
    """Coordinate local cultural metadata; never performs external API calls."""

    def catalog(self) -> dict[str, Any]:
        return get_cultural_core_catalog()

    def list_domains(self, *, enabled_only: bool = False) -> dict[str, Any]:
        items = list_domains()
        if enabled_only:
            items = [item for item in items if item.get("enabled", True)]
        return {"success": True, "count": len(items), "domains": items}

    def domain_inventory(self) -> list[dict[str, Any]]:
        """Return canonical domain metadata with explicit implementation boundaries."""
        return [
            {
                **item,
                "registration_status": "REGISTERED",
                "domain_assignment": "CANONICAL_DOMAIN_REGISTRY",
                "live_connection_verified": False,
            }
            for item in list_domains()
        ]

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return get_domain(domain_id)

    def offerings(self) -> dict[str, Any]:
        items = self.domain_inventory()
        return {"success": True, "count": len(items), "offerings": items}

    def get_offering(self, product_id: str) -> dict[str, Any] | None:
        needle = str(product_id or "").strip().casefold()
        if not needle:
            return None
        for item in self.domain_inventory():
            candidates = (
                str(item.get("domain_id", "")),
                str(item.get("name", "")),
                str(item.get("package_name", "")),
            )
            if any(value.casefold() == needle for value in candidates):
                return item
        return None

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        domains = domain_summary()
        resources = resource_inventory_summary()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            "pillar_count": len(catalog["pillars"]),
            "domain_count": domains["domain_count"],
            "domain_package_count": domains["domain_count"],
            "resource_count": resources["resource_count"],
            "resource_count_verified": resources["resource_count_verified"],
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "warnings": [
                "Registered domains do not prove exhaustive coverage of every culture or tradition.",
                "Catalog availability does not imply live API connectivity or publication permission.",
            ],
        }

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True,
            "edges": [
                {
                    "core_module": item["package_path"],
                    "api_domain_ref": item["api_domain_ref"],
                    "relationship": "DELEGATES_TO_CULTURAL_API_DOMAIN",
                }
                for item in list_domains()
            ],
        }
