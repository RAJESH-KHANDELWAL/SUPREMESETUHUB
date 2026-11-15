"""Offline tests for GOOGLE_PERSONAL_CLOUD_STORAGE_ECOSYSTEM."""
from ..ecosystem_service import CategoryEcosystemService
from ..service import GooglePersonalCloudStorageEcosystem


def test_category_identity_and_safe_defaults():
    result = GooglePersonalCloudStorageEcosystem().describe()
    assert result["ecosystem_id"] == "GOOGLE_PERSONAL_CLOUD_STORAGE_ECOSYSTEM"
    assert result["category"] == "PERSONAL_CLOUD"
    assert result["connection_state"] == "NOT_CONFIGURED"
    assert result["storage_operations_enabled"] is False


def test_health_does_not_claim_external_connection():
    result = CategoryEcosystemService().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False
