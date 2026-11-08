"""Tests for the independent GLOBAL DATABASE manager."""
from .manager import GlobalDatabaseEcosystemManager

def test_database_manager_reports_independent_catalog():
    status = GlobalDatabaseEcosystemManager().status()
    assert status["layer"] == "DATABASE"
    assert status["ecosystem_id"] == "GLOBAL-DATABASE-ECOSYSTEM"
    assert status["mirrored_directory_count"] > 0
    assert status["live_connections_verified"] is False

def test_database_manager_lists_existing_provider_adapters():
    providers = GlobalDatabaseEcosystemManager().list_providers()
    assert {item["provider_id"] for item in providers} == {
        "aws", "google", "mega", "microsoft", "proton"
    }
    assert all(item["connection_status"] == "not_configured" for item in providers)
