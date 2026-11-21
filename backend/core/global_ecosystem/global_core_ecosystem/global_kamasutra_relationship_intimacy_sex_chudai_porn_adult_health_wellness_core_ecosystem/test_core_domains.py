"""Structural tests for the Core taxonomy."""
from .manager import get_manager
def test_inventory_is_catalog_only() -> None:
    manager = get_manager()
    assert manager.status()["status"] == "CATALOG_ONLY"
    assert manager.status()["connected"] is False
def test_domains_and_packages_are_registered() -> None:
    manager = get_manager()
    assert len(manager.list_domains()) == 12
    assert len(manager.list_products()) == 62
    assert all(item["connected"] is False for item in manager.list_products())
def test_adult_safety_policy_is_explicit() -> None:
    from .policy import get_policy
    policy = get_policy()
    assert policy["adult_only"] is True and policy["minimum_age"] == 18
    assert policy["non_consensual_intimate_content_prohibited"] is True
    assert policy["minors_and_child_sexual_abuse_material_prohibited"] is True
