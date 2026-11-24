from ..ecosystem_service import AppService
def test_app_is_separate_and_disconnected():
 data=AppService().describe();assert data["app_id"]=="YOUTAG_RECHARGES_APP"
 assert data["business_parent"]=="GLOBAL_YOUTAG_BUSINESS_STORAGE_ECOSYSTEM"
 assert data["connection_state"]=="NOT_CONFIGURED" and data["storage_operations_enabled"] is False
