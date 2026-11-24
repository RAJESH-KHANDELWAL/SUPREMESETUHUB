"""Business service manager and read-only 2468 master catalog bridge."""
import json
from pathlib import Path

from .business_classification import classify_service
from .policy import get_policy
from .service_catalog import (
    get_service,
    list_services,
    search_services,
    validate_mappings,
)
from ..global_msme_sme_startup_solo_preneur_solo_preneurship_business_men_business_women_women_preneur_women_preneurship_men_preneur_men_preneurship_entrepreneur_entrepreneurship_research_innovation_core_ecosystem.domain_catalog import (
    DOMAINS,
    get_geographic_registry,
)


class GlobalMSMESMEStartupEntrepreneurshipBusinessCoreManager:
    NAME = (
        "GLOBAL MSME SME STARTUP SOLO-PRENEUR BUSINESS MEN BUSINESS WOMEN "
        "WOMEN-PRENEUR MEN-PRENEUR ENTREPRENEUR ENTREPRENEURSHIP "
        "RESEARCH INNOVATION SERVICE WORK BUSINESS CORE ECOSYSTEM"
    )
    MASTER_CATALOG_PATH = (
        Path(__file__).resolve().parents[5] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    )
    MASTER_CATALOG_ID = "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"

    def list_services(self):
        return list_services()

    def get_service(self, key):
        return get_service(key)

    def search(self, query):
        return search_services(query)

    def classify_service(self, key):
        return classify_service(key)

    def policy(self):
        return get_policy()

    def validate_mappings(self):
        return validate_mappings({domain["domain_id"] for domain in DOMAINS})

    def health(self):
        return self.validate_mappings()

    def master_catalog_reference(self):
        return {
            "catalogue_id": self.MASTER_CATALOG_ID,
            "source_path": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
            "access_mode": "READ_ONLY_ON_DEMAND",
            "target_unique_entries": 2468,
        }

    def master_catalog_inventory(self):
        data = json.loads(self.MASTER_CATALOG_PATH.read_text(encoding="utf-8"))
        expansion = data["expansion"]
        counts = data["counts"]
        target = expansion["target_unique_entries"]
        current = expansion["current_unique_entries"]
        if (
            data["catalogue_id"] != self.MASTER_CATALOG_ID
            or target != 2468
            or current != counts["unique_catalogue_entries"]
            or expansion["remaining_unique_entries"] != target - current
        ):
            raise ValueError("MASTER_CATALOG_INTEGRITY_ERROR")
        return {
            "success": True,
            "target_unique_entries": target,
            "current_unique_entries": current,
            "remaining_unique_entries": target - current,
            "access_mode": "READ_ONLY",
        }

    def geography(self):
        registry = get_geographic_registry()
        return {"coverage": registry.coverage(), "validation": registry.validate()}


def get_manager():
    return GlobalMSMESMEStartupEntrepreneurshipBusinessCoreManager()
