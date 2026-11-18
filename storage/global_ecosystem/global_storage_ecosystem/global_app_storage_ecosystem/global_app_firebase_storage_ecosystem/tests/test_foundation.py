"""Offline foundation tests for GLOBAL_APP_FIREBASE_STORAGE_ECOSYSTEM; no external provider calls."""
from ..service import GlobalAppFirebaseStorageEcosystem
def test_identity_and_safe_defaults():
 status=GlobalAppFirebaseStorageEcosystem().describe()
 assert status["ecosystem_id"]=="GLOBAL_APP_FIREBASE_STORAGE_ECOSYSTEM"
 assert status["connection_state"]=="NOT_CONFIGURED"
 assert status["provider_product_verified"] is False
 assert status["storage_operations_enabled"] is False
def test_health_does_not_claim_connection():
 result=GlobalAppFirebaseStorageEcosystem().health()
 assert result["success"] is True and result["external_connection_verified"] is False
