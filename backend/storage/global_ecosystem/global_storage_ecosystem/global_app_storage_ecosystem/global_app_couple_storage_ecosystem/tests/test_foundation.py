"""Offline tests for GLOBAL_APP_COUPLE_STORAGE_ECOSYSTEM; no external calls."""
from ..service import GlobalAppCoupleStorageEcosystem
def test_identity_and_safe_defaults():
 status=GlobalAppCoupleStorageEcosystem().describe()
 assert status["ecosystem_id"]=="GLOBAL_APP_COUPLE_STORAGE_ECOSYSTEM"
 assert status["connection_state"]=="NOT_CONFIGURED"
 assert status["provider_product_verified"] is False
 assert status["storage_operations_enabled"] is False
def test_health_does_not_claim_connection():
 result=GlobalAppCoupleStorageEcosystem().health()
 assert result["success"] is True and result["external_connection_verified"] is False
