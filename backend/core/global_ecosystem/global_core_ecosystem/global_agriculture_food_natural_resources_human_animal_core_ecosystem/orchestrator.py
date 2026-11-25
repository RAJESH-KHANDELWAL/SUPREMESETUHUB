"""Coordinates taxonomy and policy metadata without external API calls."""
from __future__ import annotations
from .catalog import get_catalog
from .domain_catalog import domain_summary, get_domain
from .policy import classify_capability, safe_metadata

class AgricultureCoreOrchestrator:
    def catalog(self):
        return get_catalog()

    def domains(self):
        return domain_summary()

    def get_domain(self, domain_id: str):
        return get_domain(domain_id)

    def classify(self, capability: str):
        return classify_capability(capability)

    def dependency_map(self):
        catalog = get_catalog()
        return {"success": True, "edges": [
            {"from": catalog["ecosystem_id"], "to": catalog["business_layer_id"], "relationship": "SHARED_CANONICAL_TAXONOMY"}
        ]}

    def health(self):
        catalog = get_catalog()
        return {"success": True, "status": "CORE_CATALOG_AVAILABLE", "domain_count": len(catalog["domains"]), "live_data_verified": False, "provider_connections_verified": False, "api_calls_performed": 0}
