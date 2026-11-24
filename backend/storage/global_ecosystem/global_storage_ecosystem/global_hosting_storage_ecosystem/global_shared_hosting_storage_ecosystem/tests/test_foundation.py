"""Offline foundation tests for GLOBAL_SHARED_HOSTING_HOSTING_STORAGE_ECOSYSTEM."""
from ..service import GlobalSharedHostingHostingStorageEcosystem

def test_category_identity_and_safe_defaults():
    service = GlobalSharedHostingHostingStorageEcosystem()
    status = service.describe()
    assert status["ecosystem_id"] == "GLOBAL_SHARED_HOSTING_HOSTING_STORAGE_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False

def test_health_does_not_claim_external_connection():
    result = GlobalSharedHostingHostingStorageEcosystem().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False
