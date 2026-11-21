import json
from pathlib import Path

from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.manager import (
    get_domains, get_manager, get_catalog, get_service_tiers, get_protected_group_safety,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.provider_catalog import get_provider_catalog
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.policy import redact_sensitive_metadata


def _master_catalog():
    backend_root = Path(__file__).resolve().parents[5]
    source = backend_root / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    return json.loads(source.read_text(encoding="utf-8"))


def test_security_taxonomy_provider_inventory_and_master_catalog_refs():
    domains = get_domains()
    domain_ids = [item["id"] for item in domains]
    assert len(domains) == 33
    assert len(domain_ids) == len(set(domain_ids))
    assert len({item["folder"] for item in domains}) == len(domains)
    area_ids = [area["area_id"] for domain in domains for area in domain["coverage_areas"]]
    assert len(area_ids) == 330
    assert len(area_ids) == len(set(area_ids))
    assert all(len(domain["coverage_areas"]) == 10 for domain in domains)
    assert len(get_provider_catalog()) == 6

    master = _master_catalog()
    known_refs = {
        entry["entry_id"]
        for section in master["sections"]
        for entry in section["entries"]
    }
    known_sections = {section["section_id"] for section in master["sections"]}
    entry_sections = {
        entry["entry_id"]: section["section_id"]
        for section in master["sections"]
        for entry in section["entries"]
    }
    assert master["counts"]["unique_catalogue_entries"] == 246
    assert master["expansion"]["target_unique_entries"] == 2468
    module_index = master["ecosystem_module_index"]["modules"]
    security_module = [x for x in module_index if x["ecosystem_id"] == "GLOBAL-SECURITY-CORE-ECOSYSTEM"]
    assert len(security_module) == 1
    assert security_module[0]["control_area_count"] == 330
    assert master["implementation_registry"]["global_security_core_ecosystem"]["taxonomy_entries_counted_in_global_2468_target"] is False
    for domain in domains:
        refs = domain["master_catalog_refs"]
        assert refs and len(refs) == len(set(refs))
        assert set(refs) <= known_refs
        assert domain["scope"].strip()
        assert domain["master_catalog_section"] in known_sections
        assert domain["master_catalog_section"] in {entry_sections[ref] for ref in refs}

    safety = get_protected_group_safety()
    assert set(safety["groups"]) == {"MEN", "WOMEN", "GIRLS", "BOYS"}
    assert safety["groups"]["GIRLS"]["adult_content_access"] == "PROHIBITED"
    assert safety["groups"]["BOYS"]["adult_content_access"] == "PROHIBITED"
    assert safety["universal_baseline"]["production_enforcement_verified"] is False


def test_manager_google_core_style_discovery_contract():
    manager = get_manager()
    status = manager.status()
    assert status["success"] is True
    assert status["ecosystem_id"] == "GLOBAL-SECURITY-CORE-ECOSYSTEM"
    assert status["domain_count"] == 33
    assert status["coverage_area_count"] == 330
    assert status["provider_count"] == 6
    assert manager.health()["security_enforcement_verified"] is False
    assert len(manager.list_domain_inventory()) == 33
    assert manager.get_domain("identity_access") is not None
    assert manager.get_domain("not_a_domain") is None
    assert len(manager.list_modules()) == 6
    assert manager.catalog()["master_catalog_counts"]["target_unique_entries"] == 2468
    assert manager.catalog()["taxonomy"]["coverage_status"] == "DEFINED_CORE_TAXONOMY_NON_EXHAUSTIVE"
    assert manager.dependency_map()["success"] is True
    domain_manager = manager.get_domain_manager("IDENTITY_ACCESS")
    assert domain_manager.status()["coverage_area_count"] == 10
    assert domain_manager.list_coverage_areas()["count"] == 10
    assert domain_manager.master_catalog_alignment()["counts_as_new_master_entries"] is False


def test_catalog_tier_list_matches_master_capability_levels():
    tiers = get_service_tiers()
    assert [item["rank"] for item in tiers] == list(range(1, 14))
    assert [item["tier_id"] for item in tiers] == [
        "BASIC", "NORMAL", "STANDARD", "PROFESSIONAL", "ADVANCED", "EXPERT",
        "SPECIALIZED", "ENTERPRISE", "NATIONAL", "INTERNATIONAL", "GLOBAL",
        "UNIVERSAL", "SUPREME",
    ]


def test_sensitive_metadata_is_redacted():
    assert redact_sensitive_metadata({"token": "hidden", "label": "safe"}) == {"label": "safe"}
