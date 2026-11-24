"""Offline tests for GLOBAL_DEDICATED_SERVER_HOSTING_HOSTING_STORAGE_ECOSYSTEM."""
from ..service import GlobalDedicatedServerHostingHostingStorageEcosystem
def test_safe_defaults():
 d=GlobalDedicatedServerHostingHostingStorageEcosystem().describe(); assert d["ecosystem_id"]=="GLOBAL_DEDICATED_SERVER_HOSTING_HOSTING_STORAGE_ECOSYSTEM"; assert d["connection_state"]=="NOT_CONFIGURED"; assert d["provider_product_verified"] is False; assert d["storage_operations_enabled"] is False
def test_health_is_not_external_connection(): assert GlobalDedicatedServerHostingHostingStorageEcosystem().health()["external_connection_verified"] is False
