"""Offline foundation tests for GLOBAL_APP_PUBLIC_INFORMATION_STORAGE_ECOSYSTEM; no external provider calls."""
from ..service import GlobalAppPublicInformationStorageEcosystem
def test_identity_and_safe_defaults():
 status=GlobalAppPublicInformationStorageEcosystem().describe()
 assert status["ecosystem_id"]=="GLOBAL_APP_PUBLIC_INFORMATION_STORAGE_ECOSYSTEM"
 assert status["connection_state"]=="NOT_CONFIGURED"
 assert status["provider_product_verified"] is False
 assert status["storage_operations_enabled"] is False
def test_health_does_not_claim_connection():
 result=GlobalAppPublicInformationStorageEcosystem().health()
 assert result["success"] is True and result["external_connection_verified"] is False
