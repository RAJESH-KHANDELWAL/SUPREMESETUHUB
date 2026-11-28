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
    assert isinstance(manager.catalog(), dict)


def test_manager_lists_domains_with_success_envelope():
    result = get_manager().list_domains()
    assert isinstance(result, dict)
    assert result["success"] is True
    assert isinstance(result["count"], int)
    assert isinstance(result["domains"], list)
    assert result["count"] == len(result["domains"])
