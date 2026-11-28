"""Canonical CORE manager and read-only 2468 master catalog bridge."""
import json
from pathlib import Path

from .catalog import get_catalog
from .domain_catalog import (
    get_domain,
    get_geographic_registry,
    list_domains,
    search_domains,
    validate_domains,
)
from .policy import get_policy


class GlobalMSMESMEStartupEntrepreneurshipCoreManager:
    NAME = (
        "GLOBAL MSME SME STARTUP SOLO-PRENEUR BUSINESS MEN BUSINESS WOMEN "
        "WOMEN-PRENEUR MEN-PRENEUR ENTREPRENEUR ENTREPRENEURSHIP "
        "RESEARCH INNOVATION CORE ECOSYSTEM"
    )
    MASTER_CATALOG_PATH = (
        Path(__file__).resolve().parents[4] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    )
    MASTER_CATALOG_ID = "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"

    def catalog(self):
        return get_catalog()

    def list_domains(self):
        return list_domains()

    def get_domain(self, key):
        return get_domain(key)

    def search(self, query):
        return search_domains(query)

    def policy(self):
        return get_policy()

    def health(self):
        validation = validate_domains()
        return {
            "healthy": validation["valid"],
            "domain_count": len(list_domains()),
            "mode": "taxonomy_only",
        }

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

    def list_geographic_locations(self, parent_id):
        return get_geographic_registry().children(parent_id)


def get_manager():
    return GlobalMSMESMEStartupEntrepreneurshipCoreManager()
