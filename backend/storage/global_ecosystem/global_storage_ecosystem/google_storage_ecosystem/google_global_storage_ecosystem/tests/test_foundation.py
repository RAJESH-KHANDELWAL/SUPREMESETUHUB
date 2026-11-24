"""Offline foundation tests for GOOGLE_GLOBAL_STORAGE_ECOSYSTEM."""
from ..service import GoogleGlobalStorageEcosystem
def test_category_identity_and_safe_defaults():
    status = GoogleGlobalStorageEcosystem().describe()
    assert status["ecosystem_id"] == "GOOGLE_GLOBAL_STORAGE_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False
def test_health_does_not_claim_external_connection():
    assert GoogleGlobalStorageEcosystem().health()["external_connection_verified"] is False
