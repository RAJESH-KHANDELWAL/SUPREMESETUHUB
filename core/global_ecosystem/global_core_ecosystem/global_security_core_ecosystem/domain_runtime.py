"""Shared read-only runtime for all registered Global Security CORE domains."""
from __future__ import annotations

from typing import Any

from .manager import get_domain


class SecurityCoreDomainManager:
    """Domain-scoped discovery over the canonical security catalog."""

    def __init__(self, domain_id: str) -> None:
        domain = get_domain(domain_id)
        if domain is None:
            raise ValueError(f"UNKNOWN_SECURITY_CORE_DOMAIN: {domain_id}")
        self._domain = domain

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            "domain_id": self._domain["id"],
            "name": self._domain["name"],
            "status": self._domain["status"],
            "coverage_area_count": len(self._domain["coverage_areas"]),
            "master_catalog_refs": list(self._domain["master_catalog_refs"]),
            "live_controls_verified": False,
            "runtime_enforcement_verified": False,
        }

    def list_coverage_areas(self) -> dict[str, Any]:
        areas = self._domain["coverage_areas"]
        return {
            "success": True,
            "domain_id": self._domain["id"],
            "count": len(areas),
            "coverage_areas": areas,
        }

    def get_coverage_area(self, area_id: str) -> dict[str, Any] | None:
        needle = area_id.strip().casefold()
        if not needle:
            return None
        return next(
            (dict(area) for area in self._domain["coverage_areas"]
             if area["area_id"].casefold() == needle),
            None,
        )

    def master_catalog_alignment(self) -> dict[str, Any]:
        return {
            "success": True,
            "source": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
            "references": list(self._domain["master_catalog_refs"]),
            "section_id": self._domain["master_catalog_section"],
            "counts_as_new_master_entries": False,
        }


__all__ = ["SecurityCoreDomainManager"]
