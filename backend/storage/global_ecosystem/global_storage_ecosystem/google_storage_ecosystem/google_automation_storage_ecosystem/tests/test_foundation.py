"""Offline foundation tests for GOOGLE_AUTOMATION_STORAGE_ECOSYSTEM."""
from ..service import GoogleAutomationStorageEcosystem
def test_category_identity_and_safe_defaults():
    status = GoogleAutomationStorageEcosystem().describe()
    assert status["ecosystem_id"] == "GOOGLE_AUTOMATION_STORAGE_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False
def test_health_does_not_claim_external_connection():
    assert GoogleAutomationStorageEcosystem().health()["external_connection_verified"] is False
