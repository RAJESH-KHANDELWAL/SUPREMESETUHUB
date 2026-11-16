"""Offline category foundation tests."""
from ..service import GlobalAffiliateMarketingBusinessStorageEcosystemStorageEcosystem
def test_safe_disconnected_defaults():
 status=GlobalAffiliateMarketingBusinessStorageEcosystemStorageEcosystem().describe()
 assert status["connection_state"]=="NOT_CONFIGURED"
 assert status["external_connections_verified"] is False
 assert status["storage_operations_enabled"] is False
