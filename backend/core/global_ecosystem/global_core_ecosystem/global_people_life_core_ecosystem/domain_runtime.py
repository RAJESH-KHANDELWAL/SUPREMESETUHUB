"""Shared read-only runtime for People Life domain packages."""
from __future__ import annotations
from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS, list_people_life_domain_inventory
from .policy import safe_domain_summary

class PeopleLifeDomainManager:
    DOMAIN_ID = ""

    def __init__(self, domain_id: str | None = None) -> None:
        selected = domain_id or self.DOMAIN_ID
        if selected not in DOMAIN_DEFINITIONS:
            raise ValueError(f"UNKNOWN_PEOPLE_LIFE_DOMAIN: {selected}")
        self.DOMAIN_ID = selected
        self._definition = DOMAIN_DEFINITIONS[selected]

    def status(self) -> dict[str, Any]:
        item = next(x for x in list_people_life_domain_inventory() if x["domain_id"] == self.DOMAIN_ID)
        return {
            "success": True, "domain_id": self.DOMAIN_ID,
            "name": self._definition["name"], "purpose": self._definition["purpose"],
            "status": "CORE_DOMAIN_AVAILABLE",
            "implementation_mode": self._definition["implementation_mode"],
            "module_count": item["module_count"],
            "age_restricted": self._definition["age_restricted"],
            "live_service_connections_verified": 0, "workflows_executed": 0,
        }

    def describe(self) -> dict[str, Any]:
        return {"success": True, **safe_domain_summary(self._definition), "live_service_verified": False}

    def list_modules(self) -> dict[str, Any]:
        item = next(x for x in list_people_life_domain_inventory() if x["domain_id"] == self.DOMAIN_ID)
        return {"success": True, "domain_id": self.DOMAIN_ID, "count": item["module_count"], "modules": item["modules"]}

    def get_module(self, module_id: str) -> dict[str, Any] | None:
        needle = module_id.strip().casefold()
        for module in self.list_modules()["modules"]:
            if module["folder"].casefold() == needle or module["id"].casefold() == needle:
                return module
        return None

__all__ = ["PeopleLifeDomainManager"]
