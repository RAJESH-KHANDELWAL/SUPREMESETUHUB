"""Offline foundation tests for GOOGLE_FITNESS_STORAGE_ECOSYSTEM."""
from ..service import GoogleFitnessStorageEcosystem

def test_category_identity_and_safe_defaults():
    service = GoogleFitnessStorageEcosystem()
    status = service.describe()
    assert status["ecosystem_id"] == "GOOGLE_FITNESS_STORAGE_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False

def test_health_does_not_claim_external_connection():
    result = GoogleFitnessStorageEcosystem().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False
