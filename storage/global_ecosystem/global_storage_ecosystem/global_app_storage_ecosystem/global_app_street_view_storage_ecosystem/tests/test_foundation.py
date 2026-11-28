"""Offline tests for GLOBAL_APP_STREET_VIEW_STORAGE_ECOSYSTEM; no external calls."""
from ..service import GlobalAppStreetViewStorageEcosystem
def test_identity_and_safe_defaults():
 status=GlobalAppStreetViewStorageEcosystem().describe()
 assert status["ecosystem_id"]=="GLOBAL_APP_STREET_VIEW_STORAGE_ECOSYSTEM"
 assert status["connection_state"]=="NOT_CONFIGURED"
 assert status["provider_product_verified"] is False
 assert status["storage_operations_enabled"] is False
def test_health_does_not_claim_connection():
 result=GlobalAppStreetViewStorageEcosystem().health()
 assert result["success"] is True and result["external_connection_verified"] is False
