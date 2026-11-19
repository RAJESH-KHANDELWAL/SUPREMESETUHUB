"""Offline foundation tests for COHERE_SEMANTIC_SEARCH_STORAGE_ECOSYSTEM."""
from ..service import CohereSemanticSearchStorageEcosystem

def test_category_identity_and_safe_defaults():
    service = CohereSemanticSearchStorageEcosystem()
    status = service.describe()
    assert status["ecosystem_id"] == "COHERE_SEMANTIC_SEARCH_STORAGE_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False

def test_health_does_not_claim_external_connection():
    result = CohereSemanticSearchStorageEcosystem().health()
    assert result["success"] is True
    assert result["external_connection_verified"] is False
