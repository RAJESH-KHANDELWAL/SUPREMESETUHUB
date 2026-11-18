"""Offline foundation tests for GLOBAL_CLOUD_STORAGE_ENCRYPTION_ECOSYSTEM."""
from ..service import GlobalCloudStorageEncryptionEcosystem

def test_category_identity_and_safe_defaults():
    status = GlobalCloudStorageEncryptionEcosystem().describe()
    assert status["ecosystem_id"] == "GLOBAL_CLOUD_STORAGE_ENCRYPTION_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False

def test_health_does_not_claim_external_connection():
    result = GlobalCloudStorageEncryptionEcosystem().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False
