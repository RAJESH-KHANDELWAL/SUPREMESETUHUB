"""Structural and behavior tests for People Life CORE domain packages."""
from __future__ import annotations
import importlib
from backend.core.global_ecosystem.global_core_ecosystem.global_people_life_core_ecosystem.domain_catalog import (
    DOMAIN_DEFINITIONS, DOMAIN_PACKAGE_MAP, list_people_life_domain_inventory,
    list_people_life_modules, people_life_domain_summary,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_people_life_core_ecosystem.domain_runtime import PeopleLifeDomainManager

PACKAGE_ROOT = "backend.core.global_ecosystem.global_core_ecosystem.global_people_life_core_ecosystem"
def test_all_domains_are_registered_and_have_unique_ids():
    assert len(DOMAIN_DEFINITIONS) == 24
    assert len(DOMAIN_PACKAGE_MAP) == 19
    assert len(set(DOMAIN_DEFINITIONS)) == 24

def test_each_local_domain_package_exports_a_working_manager():
    for domain_id, package_name in DOMAIN_PACKAGE_MAP.items():
        package = importlib.import_module(f"{PACKAGE_ROOT}.{package_name}")
        manager = package.get_manager()
        assert manager.DOMAIN_ID == domain_id
        assert manager.status()["domain_id"] == domain_id
        assert manager.list_modules()["success"] is True

def test_domain_module_inventory_matches_canonical_map():
    inventory = list_people_life_domain_inventory()
    assert len(inventory) == 24
    for domain in inventory:
        manager = PeopleLifeDomainManager(domain["domain_id"])
        assert manager.list_modules()["count"] == domain["module_count"]

def test_all_existing_modules_are_routed_or_are_service_tiers():
    modules = list_people_life_modules()
    assert len(modules) == 28
    summary = people_life_domain_summary()
    assert summary["unmapped_module_count"] == 0
    assert summary["service_tier_count"] == 7

def test_adult_domains_are_explicitly_restricted_and_external():
    adult = [x for x in DOMAIN_DEFINITIONS.values() if x["age_restricted"]]
    assert len(adult) == 5
    assert all(x["implementation_mode"] == "CROSS_ECOSYSTEM_REFERENCE" for x in adult)
    assert all(x["canonical_ecosystem_ref"] for x in adult)
