"""Focused tests for the Global Agriculture/Food/Natural Resources CORE manager."""
from .manager import AgricultureFoodNaturalResourcesHumanAnimalCoreManager, get_manager


def test_manager_factory_returns_canonical_manager():
    manager = get_manager()
    assert isinstance(manager, AgricultureFoodNaturalResourcesHumanAnimalCoreManager)


def test_manager_identity_is_stable():
    manager = get_manager()
    assert manager.ECOSYSTEM_ID == "GLOBAL-AGRICULTURE-FOOD-NATURAL-RESOURCES-HUMAN-ANIMAL-CORE-ECOSYSTEM"


def test_manager_exposes_core_interfaces():
    manager = get_manager()
    assert isinstance(manager.status(), dict)
    assert isinstance(manager.health(), dict)
    assert isinstance(manager.list_domains(), list)
    assert isinstance(manager.catalog(), dict)
