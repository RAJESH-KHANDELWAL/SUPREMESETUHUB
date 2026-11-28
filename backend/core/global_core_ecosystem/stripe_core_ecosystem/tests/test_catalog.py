"""Structural and behavior tests for the Stripe Core control plane."""
from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.catalog import (
    STRIPE_CORE_ECOSYSTEM,
    get_stripe_core_catalog,
    list_stripe_core_modules,
)
from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.contracts import (
    SecretReference,
    TenantContext,
)
from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.domain_catalog import (
    list_stripe_domain_inventory,
    stripe_domain_summary,
)
from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.master_catalog import (
    get_master_catalog_status,
)
from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.policy import (
    StripeCorePolicy,
    StripeCorePolicyError,
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


def test_all_families_are_assigned_to_a_stripe_domain():
    inventory = list_stripe_domain_inventory()
    summary = stripe_domain_summary()
    assert len(inventory) == 22
    assert summary["domain_count"] == 7
    assert all(item["core_domain_id"] for item in inventory)


def test_manager_is_the_canonical_entry_point():
    manager = get_manager()
    assert manager.ECOSYSTEM_ID == "STRIPE-CORE-ECOSYSTEM"
    assert manager.list_products()["count"] == 22
    assert manager.list_domains()["domain_count"] == 7
    assert manager.health()["live_connections_verified"] == 0


def test_contracts_reject_empty_tenant_and_secret_reference():
    TenantContext(tenant_id="tenant-1", actor_id="actor-1").validate()
    SecretReference(provider="vault", reference="stripe/tenant-1")
    try:
        TenantContext(tenant_id="", actor_id="actor-1").validate()
    except ValueError as exc:
        assert str(exc) == "TENANT_ID_REQUIRED"
    else:
        raise AssertionError("Empty tenant context must be rejected")


def test_sensitive_payment_capabilities_are_classified():
    assert StripeCorePolicy.classify_capability("REFUND_LIFECYCLE").startswith("SENSITIVE")
    try:
        StripeCorePolicy.require_idempotency_key(None)
    except StripeCorePolicyError as exc:
        assert "IDEMPOTENCY_KEY_REQUIRED" in str(exc)
    else:
        raise AssertionError("Payment write without idempotency key must be rejected")


def test_safe_metadata_removes_credentials_and_card_data():
    result = StripeCorePolicy.safe_metadata({
        "account": "acct_test",
        "api_key": "must-not-leak",
        "nested": {"webhook_secret": "must-not-leak", "status": "ok"},
    })
    assert result == {"account": "acct_test", "nested": {"status": "ok"}}


def test_master_catalog_bridge_is_read_only_and_preserves_target():
    result = get_master_catalog_status()
    assert result["path"] == "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    assert result["target_unique_entries"] == 2468
    assert result["access_mode"] == "READ_ONLY_ON_DEMAND"
    assert result["source_modified"] is False
