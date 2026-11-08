"""Structural tests for the Stripe Core catalog."""
from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.catalog import (
    STRIPE_CORE_ECOSYSTEM,
    get_stripe_core_catalog,
    list_stripe_core_modules,
)

def test_stripe_core_catalog_has_all_api_families():
    catalog = get_stripe_core_catalog()
    assert catalog["ecosystem_id"] == "STRIPE-CORE-ECOSYSTEM"
    assert len(catalog["children"]) == 22
    assert len({item["ecosystem_id"] for item in catalog["children"]}) == 22

def test_stripe_core_children_are_not_live_by_default():
    assert all(item["connected"] is False for item in list_stripe_core_modules())
    assert STRIPE_CORE_ECOSYSTEM["live_connection_verified"] is False

def test_every_child_has_api_and_core_boundaries():
    for child in list_stripe_core_modules():
        assert child["api_family"]
        assert child["module"]
        assert child["status"] == "CORE_CATALOG_ONLY"

def test_every_child_has_complete_parent_and_layer_references():
    for child in list_stripe_core_modules():
        assert child["ecosystem_type"] == "PROVIDER_CORE_SERVICE"
        assert child["parent_id"] == "STRIPE-CORE-ECOSYSTEM"
        assert child["api_catalog_ref"].startswith(
            "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/"
        )
        assert child["core_module"].startswith(
            "backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/"
        )
