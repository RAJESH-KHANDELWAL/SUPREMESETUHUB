"""Public cultural Core service; preserves the original GlobalCulturalCore API."""
from __future__ import annotations

from typing import Any

from .catalog import get_cultural_core_catalog
from .domain_catalog import list_domains
from .orchestrator import CulturalCoreOrchestrator
from .resource_catalog import get_foundational_knowledge, search_knowledge
from .governance import validate_cultural_record, assess_evidence
from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem import assess_publication as assess_domain_publication


class GlobalCulturalCore:
    NAME = "GLOBAL VASUDHAIVA KUTUMBAKAM | SANATAN DHARMA | BHARAT SANSKRITI | WORLD CULTURE CORE ECOSYSTEM"
    ecosystem_id = "GLOBAL-VASUDHAIVA-KUTUMBAKAM-SANATAN-DHARMA-BHARAT-WORLD-CULTURE-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self.orchestrator = CulturalCoreOrchestrator()

    def describe(self) -> dict[str, Any]:
        catalog = get_cultural_core_catalog()
        return {
            "id": catalog["ecosystem_id"],
            "name": catalog["name"],
            "pillars": list(catalog["pillars"]),
            "domain_ids": [item["domain_id"] for item in list_domains()],
            "purpose": "Preserve, research, teach and connect living cultural knowledge with evidence, consent and community context.",
        }

    def domains(self) -> list[dict[str, Any]]:
        return list_domains()

    def knowledge(self) -> dict[str, Any]:
        return get_foundational_knowledge()

    def search_foundation(self, query: str) -> list[dict[str, Any]]:
        return search_knowledge(query)

    def publication_review(self, resource: Any) -> Any:
        if not isinstance(resource, dict):
            return assess_domain_publication(resource)
        errors = validate_cultural_record(resource)
        approved = not errors and str(resource.get("publication_status", "DRAFT")).upper() == "APPROVED"
        return {
            "approved": approved,
            "status": "APPROVED" if approved else "REVIEW_REQUIRED",
            "errors": errors,
        }

    def status(self) -> dict[str, Any]:
        catalog = get_cultural_core_catalog()
        health = self.orchestrator.health()
        registry = self.manager_status()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "name": self.NAME,
            "status": catalog["status"],
            "registry_status": registry["registered"],
            "pillar_count": len(catalog["pillars"]),
            "domain_count": health["domain_count"],
            "domain_package_count": health["domain_package_count"],
            "resource_count": health["resource_count"],
            "resource_count_verified": health["resource_count_verified"],
            "live_connections_verified": False,
            "api_calls_performed": 0,
            "health": health,
            "api_catalog_ref": catalog["api_catalog_ref"],
            "source_of_record": catalog["domain_source_ref"],
        }

    def list_domains(self) -> dict[str, Any]:
        return self.orchestrator.list_domains()

    def list_offerings(self) -> dict[str, Any]:
        return self.orchestrator.offerings()

    def get_domain_manager(self, domain_id: str):
        from .domain_runtime import CulturalCoreDomainManager
        return CulturalCoreDomainManager(domain_id)

    def dependency_map(self) -> dict[str, Any]:
        return self.orchestrator.dependency_map()

    def manager_status(self) -> dict[str, Any]:
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            record = GlobalEcosystemManager().get(self.ecosystem_id)
            return {"success": record is not None, "registered": record is not None, "ecosystem": record}
        except Exception as exc:
            return {"success": False, "registered": False, "ecosystem": None, "error": type(exc).__name__}


def get_manager():
    """Backward-compatible manager factory retained at the service boundary."""
    from .manager import CulturalCoreManager
    return CulturalCoreManager()


__all__ = ["GlobalCulturalCore", "get_manager", "validate_cultural_record", "assess_evidence"]
