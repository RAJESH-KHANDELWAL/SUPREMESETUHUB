"""Smoke tests for the Anthropic Core Ecosystem manager."""
from backend.core.global_ecosystem.global_core_ecosystem.anthropic_core_ecosystem.manager import get_manager


def test_anthropic_core_ecosystem_manager_contract():
    manager = get_manager()
    assert manager.status()["ecosystem_id"] == "ANTHROPIC-CORE-ECOSYSTEM"
    assert isinstance(manager.list_products(), dict)
    assert isinstance(manager.list_domains(), dict)
