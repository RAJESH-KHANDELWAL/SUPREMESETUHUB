"""Offline foundation tests for GOOGLE_GLOBAL_DIGITAL_KNOWLEDGE_STORAGE_ECOSYSTEM."""
from ..service import GoogleGlobalDigitalKnowledgeStorageEcosystem
def test_category_identity_and_safe_defaults():
    status = GoogleGlobalDigitalKnowledgeStorageEcosystem().describe()
    assert status["ecosystem_id"] == "GOOGLE_GLOBAL_DIGITAL_KNOWLEDGE_STORAGE_ECOSYSTEM"
    assert status["connection_state"] == "NOT_CONFIGURED"
    assert status["provider_product_verified"] is False
    assert status["storage_operations_enabled"] is False
def test_health_does_not_claim_external_connection():
    assert GoogleGlobalDigitalKnowledgeStorageEcosystem().health()["external_connection_verified"] is False
