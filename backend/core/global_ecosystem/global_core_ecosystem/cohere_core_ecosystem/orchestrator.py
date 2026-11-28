"""Cohere CORE discovery and readiness orchestration; no provider execution."""
from __future__ import annotations

from typing import Any

from .catalog import get_cohere_core_catalog, list_capabilities
from .domain_catalog import domain_summary, list_domain_inventory


class CohereCoreOrchestrator:
    """Coordinate capability and domain metadata without invoking Cohere."""

    def catalog(self) -> dict[str, Any]:
        return get_cohere_core_catalog()

    def capabilities(self) -> dict[str, Any]:
        items = list_capabilities()
        return {"success": True, "count": len(items), "capabilities": items}

    def list_modules(self, *, enabled_only: bool = False) -> dict[str, Any]:
        children = self.catalog()["children"]
        if enabled_only:
            children = [item for item in children if item.get("enabled", True)]
        return {"success": True, "count": len(children), "modules": children}

    def get_module(self, ecosystem_id: str) -> dict[str, Any] | None:
        if not isinstance(ecosystem_id, str) or not ecosystem_id.strip():
            return None
        needle = ecosystem_id.strip().casefold()
        for item in self.catalog()["children"]:
            if item["ecosystem_id"].casefold() == needle or item["capability"].casefold() == needle:
                return item
        return None

    def domains(self) -> dict[str, Any]:
        return {"success": True, **domain_summary()}

    def domain_inventory(self) -> list[dict[str, Any]]:
        return list_domain_inventory()

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        children = catalog["children"]
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            "capability_count": len(children),
            "enabled_capability_count": sum(bool(item.get("enabled")) for item in children),
            "api_catalog_reference_count": sum(bool(item.get("api_catalog_ref")) for item in children),
            "engine_reference_count": sum(bool(item.get("engine_ref")) for item in children),
            "live_connections_verified": 0,
            "live_provider_calls_enabled": False,
            "api_calls_performed": 0,
            "warning": "Catalog registration is not evidence of API access, model availability, entitlement or live connectivity.",
        }

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True,
            "edges": [
                {
                    "core_module": item["core_module"],
                    "api_catalog_ref": item["api_catalog_ref"],
                    "engine_ref": item["engine_ref"],
                    "relationship": "DECLARED_LAYER_DEPENDENCY_NO_LIVE_DISPATCH",
                }
                for item in self.catalog()["children"]
            ],
        }
