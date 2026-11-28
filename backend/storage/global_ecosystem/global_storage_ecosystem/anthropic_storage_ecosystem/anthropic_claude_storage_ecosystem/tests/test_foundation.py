"""Offline foundation tests for ANTHROPIC_CLAUDE_STORAGE_ECOSYSTEM."""
from anthropic_claude_storage_ecosystem.ecosystem_service import CategoryEcosystemService
def test_foundation_is_not_misreported_as_connected():
    service = CategoryEcosystemService()
    assert service.describe()["connection_state"] == "NOT_CONFIGURED"
    assert service.health()["external_connection_verified"] is False
