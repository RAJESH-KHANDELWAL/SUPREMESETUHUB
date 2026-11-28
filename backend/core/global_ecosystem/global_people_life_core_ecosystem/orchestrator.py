"""People Life CORE discovery, routing and health metadata."""
from __future__ import annotations
from typing import Any
from .catalog import get_people_life_core_catalog
from .domain_catalog import (
    get_people_life_domain, get_people_life_module, list_people_life_domains,
    list_people_life_domain_inventory, list_people_life_modules,
    people_life_domain_summary,
)
from .policy import safe_domain_summary

class PeopleLifeCoreOrchestrator:
    def catalog(self) -> dict[str, Any]:
        return get_people_life_core_catalog()

    def list_modules(self, enabled_only: bool = False) -> dict[str, Any]:
        items = list_people_life_modules()
        return {"success": True, "count": len(items), "modules": items}

    def get_module(self, module_id: str) -> dict[str, Any] | None:
        return get_people_life_module(module_id)

    def list_domains(self, include_external: bool = True) -> dict[str, Any]:
        items = list_people_life_domains(include_external=include_external)
        return {"success": True, "count": len(items), "domains": [safe_domain_summary(x) for x in items]}

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return get_people_life_domain(domain_id)

    def domains(self) -> dict[str, Any]:
        return {"success": True, **people_life_domain_summary(), "domains": list_people_life_domains()}

    def domain_inventory(self) -> list[dict[str, Any]]:
        return list_people_life_domain_inventory()

    def health(self) -> dict[str, Any]:
        catalog = self.catalog()
        summary = people_life_domain_summary()
        return {
            "success": True, "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            **summary,
            "enabled_module_count": sum(bool(x.get("enabled", True)) for x in catalog["children"]),
            "live_service_connections_verified": 0,
            "application_workflows_executed": 0,
            "warning": "Taxonomy and policy metadata do not prove legal compliance, age verification, clinical suitability, user authorization or live service integration.",
        }

    def dependency_map(self) -> dict[str, Any]:
        edges = []
        for domain in list_people_life_domains():
            if domain["implementation_mode"] == "LOCAL_DOMAIN_PACKAGE":
                edges.append({"domain_id": domain["domain_id"], "core_module": domain["package_path"], "relationship": "LOCAL_DOMAIN_METADATA_MANAGER"})
            else:
                edges.append({
                    "domain_id": domain["domain_id"],
                    "canonical_ecosystem_ref": domain["canonical_ecosystem_ref"],
                    "canonical_domain_refs": domain["canonical_domain_refs"],
                    "relationship": "DELEGATES_TO_CANONICAL_SPECIALIST_ECOSYSTEM",
                })
        return {"success": True, "edge_count": len(edges), "edges": edges}
