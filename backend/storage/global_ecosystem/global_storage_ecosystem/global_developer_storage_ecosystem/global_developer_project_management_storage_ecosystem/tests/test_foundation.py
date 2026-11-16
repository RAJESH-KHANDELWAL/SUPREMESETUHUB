"""Offline readiness safety checks."""
from ..ecosystem_service import EcosystemService

def test_starts_unconfigured_and_disabled():
    state = EcosystemService().describe()
    assert state["connection_state"] == "NOT_CONFIGURED"
    assert state["external_connections_verified"] is False
    assert state["storage_operations_enabled"] is False
