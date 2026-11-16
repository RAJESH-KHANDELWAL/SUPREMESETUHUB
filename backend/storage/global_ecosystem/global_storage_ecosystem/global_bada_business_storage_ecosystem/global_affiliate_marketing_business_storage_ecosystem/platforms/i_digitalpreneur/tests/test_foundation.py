from ..ecosystem_service import PlatformService
def test_not_connected_by_default():
 state=PlatformService().describe();assert state["connection_state"]=="NOT_CONFIGURED" and state["external_connections_verified"] is False
