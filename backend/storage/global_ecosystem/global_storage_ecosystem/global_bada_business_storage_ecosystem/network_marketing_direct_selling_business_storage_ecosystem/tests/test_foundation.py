"""Offline category foundation tests."""
from ..service import GlobalNetworkMarketingDirectSellingBusinessStorageEcosystemStorageEcosystem
def test_safe_disconnected_defaults():
 status=GlobalNetworkMarketingDirectSellingBusinessStorageEcosystemStorageEcosystem().describe()
 assert status["connection_state"]=="NOT_CONFIGURED"
 assert status["external_connections_verified"] is False
 assert status["storage_operations_enabled"] is False
