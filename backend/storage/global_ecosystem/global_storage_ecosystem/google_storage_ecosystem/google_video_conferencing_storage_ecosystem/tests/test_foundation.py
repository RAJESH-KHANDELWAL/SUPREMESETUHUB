"""Offline foundation tests for GOOGLE_VIDEO_CONFERENCING_STORAGE_ECOSYSTEM."""
from ..service import GoogleVideoConferencingStorageEcosystem

def test_category_identity_and_safe_defaults():
    service = GoogleVideoConferencingStorageEcosystem()
    status = service.describe()
    assert status["ecosystem_id"] == "GOOGLE_VIDEO_CONFERENCING_STORAGE_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False

def test_health_does_not_claim_external_connection():
    result = GoogleVideoConferencingStorageEcosystem().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False
