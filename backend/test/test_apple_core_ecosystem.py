"""Smoke tests for the Apple Core Ecosystem manager."""
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.manager import get_manager


def test_apple_core_ecosystem_manager_contract():
    manager = get_manager()
    assert manager.status()["ecosystem_id"] == "APPLE-CORE-ECOSYSTEM"
    assert isinstance(manager.list_products(), dict)
    assert isinstance(manager.list_domains(), dict)
