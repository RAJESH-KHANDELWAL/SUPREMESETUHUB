"""Focused tests for the Bada Business Agriculture CORE manager."""
from .manager import AgricultureFoodNaturalResourcesBusinessManager, get_manager


def test_manager_factory_returns_canonical_manager():
    manager = get_manager()
    assert isinstance(manager, AgricultureFoodNaturalResourcesBusinessManager)


def test_manager_identity_is_stable():
    manager = get_manager()
    assert manager.ECOSYSTEM_ID == "GLOBAL-BADA-BUSINESS-AGRICULTURE-FOOD-NATURAL-RESOURCES-HUMAN-ANIMAL-CORE-ECOSYSTEM"


def test_manager_exposes_business_interfaces():
    manager = get_manager()
    assert isinstance(manager.status(), dict)
    assert isinstance(manager.health(), dict)
    assert isinstance(manager.list_domains(), list)
    assert isinstance(manager.catalog(), dict)
