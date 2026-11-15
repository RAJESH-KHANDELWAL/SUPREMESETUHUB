"""Offline provider-level foundation tests; no Adobe endpoints are contacted."""
from ..service import AdobeStorageEcosystem

def test_identity_and_safe_defaults():
    result = AdobeStorageEcosystem().describe()
    assert result["ecosystem_id"] == "ADOBE_STORAGE_ECOSYSTEM"
    assert result["category_count"] == 9
    assert result["external_connection_verified"] is False
    assert result["storage_operations_enabled"] is False

def test_health_does_not_claim_live_connection():
    result = AdobeStorageEcosystem().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False
