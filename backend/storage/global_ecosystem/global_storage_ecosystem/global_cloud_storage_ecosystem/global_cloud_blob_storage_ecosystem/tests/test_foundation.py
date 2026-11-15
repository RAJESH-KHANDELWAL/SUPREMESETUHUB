"""Offline foundation tests for GLOBAL_CLOUD_BLOB_STORAGE_ECOSYSTEM."""
from ..service import GlobalCloudBlobStorageEcosystem

def test_category_identity_and_safe_defaults():
    status = GlobalCloudBlobStorageEcosystem().describe()
    assert status["ecosystem_id"] == "GLOBAL_CLOUD_BLOB_STORAGE_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False

def test_health_does_not_claim_external_connection():
    result = GlobalCloudBlobStorageEcosystem().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False
