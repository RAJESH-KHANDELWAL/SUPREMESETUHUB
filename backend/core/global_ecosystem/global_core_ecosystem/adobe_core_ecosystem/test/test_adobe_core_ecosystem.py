"""Smoke tests for the Adobe Core Ecosystem manager."""
from backend.core.global_ecosystem.global_core_ecosystem.adobe_core_ecosystem.manager import get_manager


def test_adobe_core_ecosystem_manager_contract():
    manager = get_manager()
    assert manager.status()["ecosystem_id"] == "ADOBE-CORE-ECOSYSTEM"
    assert isinstance(manager.list_products(), dict)
    assert isinstance(manager.list_domains(), dict)
