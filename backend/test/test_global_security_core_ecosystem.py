"""Focused regression tests for the Global Security CORE ecosystem."""
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.manager import (
    get_manager,
    get_domains,
    get_protected_group_safety,
)


def test_global_security_core_manager_and_inventory():
    manager = get_manager()
    status = manager.health()
    assert status["success"] is True
    assert status["ecosystem_id"] == "GLOBAL-SECURITY-CORE-ECOSYSTEM"
    assert status["domain_count"] == 33
    assert status["coverage_area_count"] == 330
    assert status["provider_count"] == 6
    assert status["jurisdiction_profile_count"] == 2
    assert status["security_enforcement_verified"] is False


def test_global_security_core_domain_registry_is_complete_and_unique():
    domains = get_domains()
    assert len(domains) == 33
    assert len({item["id"] for item in domains}) == 33
    assert len({item["folder"] for item in domains}) == 33
    assert all(len(item["coverage_areas"]) == 10 for item in domains)


def test_global_security_core_protected_group_safety_metadata():
    result = get_protected_group_safety()
    assert set(result["groups"]) == {"MEN", "WOMEN", "GIRLS", "BOYS"}
    assert result["groups"]["GIRLS"]["adult_content_access"] == "PROHIBITED"
    assert result["groups"]["BOYS"]["adult_content_access"] == "PROHIBITED"
    assert result["production_enforcement_verified"] is False
    assert result["universal_baseline"]["production_enforcement_verified"] is False
