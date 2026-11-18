"""Offline foundation tests for GLOBAL_AI_PROMPT_AND_CONTEXT_STORAGE_ECOSYSTEM; no external provider calls."""
from ..service import GlobalAIPromptAndContextStorageEcosystem
def test_identity_and_safe_defaults():
 status=GlobalAIPromptAndContextStorageEcosystem().describe()
 assert status["ecosystem_id"]=="GLOBAL_AI_PROMPT_AND_CONTEXT_STORAGE_ECOSYSTEM"
 assert status["connection_state"]=="NOT_CONFIGURED"
 assert status["provider_product_verified"] is False
 assert status["storage_operations_enabled"] is False
def test_health_does_not_claim_connection():
 result=GlobalAIPromptAndContextStorageEcosystem().health()
 assert result["success"] is True and result["external_connection_verified"] is False
