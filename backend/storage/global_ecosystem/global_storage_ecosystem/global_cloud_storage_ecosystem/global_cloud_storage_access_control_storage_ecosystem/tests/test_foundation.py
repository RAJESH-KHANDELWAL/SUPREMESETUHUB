"""Offline foundation tests for GLOBAL_CLOUD_STORAGE_ACCESS_CONTROL_ECOSYSTEM."""
from ..service import GlobalCloudStorageAccessControlEcosystem

def test_category_identity_and_safe_defaults():
    status = GlobalCloudStorageAccessControlEcosystem().describe()
    assert status["ecosystem_id"] == "GLOBAL_CLOUD_STORAGE_ACCESS_CONTROL_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False

def test_health_does_not_claim_external_connection():
    result = GlobalCloudStorageAccessControlEcosystem().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False
