"""Smoke tests for the Adobe Core Ecosystem manager."""
from .manager import get_manager


def test_adobe_core_ecosystem_manager_contract():
    manager = get_manager()
    assert manager.status()["ecosystem_id"] == "ADOBE-CORE-ECOSYSTEM"
    assert manager.health()["live_connections_verified"] == 0
    assert manager.list_products()["count"] >= 0
    assert manager.list_domains()["domain_count"] >= 0
