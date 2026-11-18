"""Offline foundation tests for GOOGLE_COMPUTE_STORAGE_ECOSYSTEM."""
from ..service import GoogleComputeStorageEcosystem

def test_category_identity_and_safe_defaults():
    service = GoogleComputeStorageEcosystem()
    status = service.describe()
    assert status["ecosystem_id"] == "GOOGLE_COMPUTE_STORAGE_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False

def test_health_does_not_claim_external_connection():
    result = GoogleComputeStorageEcosystem().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False
