from backend.core.global_ecosystem.global_core_ecosystem.global_communication_core_ecosystem.catalog import get_provider, list_providers, list_categories, validate_catalog
from backend.core.global_ecosystem.global_core_ecosystem.global_communication_core_ecosystem.service import ecosystem_status
def test_provider_and_category_inventory():
    assert len(list_providers()) == 15
    assert len(list_categories()) == 15
    assert validate_catalog()["valid"]
    assert get_provider(" TWILIO ")["provider_id"] == "twilio"
    assert get_provider(None) is None
def test_no_live_provider_is_claimed():
    status = ecosystem_status()
    assert status["connected_provider_count"] == 0
    assert status["live_messaging_enabled"] is False
    assert all(not p["live_connection_verified"] for p in status["providers"])
