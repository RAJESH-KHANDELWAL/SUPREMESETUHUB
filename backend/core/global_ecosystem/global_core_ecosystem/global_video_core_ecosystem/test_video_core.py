"""Structural and behavior tests for GLOBAL VIDEO CORE ECOSYSTEM."""
from backend.core.global_ecosystem.global_core_ecosystem.global_video_core_ecosystem.catalog import get_catalog
from backend.core.global_ecosystem.global_core_ecosystem.global_video_core_ecosystem.domain_catalog import DOMAIN_DEFINITIONS, domain_summary
from backend.core.global_ecosystem.global_core_ecosystem.global_video_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.global_video_core_ecosystem.master_catalog import master_catalog_status

def test_core_catalog_and_manager_are_consistent():
    catalog = get_catalog(); manager = get_manager()
    assert catalog["ecosystem_id"] == manager.ECOSYSTEM_ID
    assert catalog["provider_count"] == len(catalog["providers"])
    assert manager.status()["success"] is True
    assert manager.status()["live_connections_verified"] == 0

def test_domain_inventory_is_valid():
    assert DOMAIN_DEFINITIONS
    summary = domain_summary()
    assert summary["domain_count"] == len(DOMAIN_DEFINITIONS)
    assert sum(item["provider_count"] for item in summary["domains"]) == summary["provider_count"]

def test_every_provider_has_a_registered_domain_and_no_live_claim():
    for provider in get_catalog()["providers"]:
        assert provider["domain_id"] in DOMAIN_DEFINITIONS
        assert provider["connected"] is False
        assert provider["live_connection_verified"] is False

def test_global_core_hierarchy_registers_video_core():
    from backend.core.global_ecosystem.global_core_ecosystem.manager import get_catalog as get_global_catalog
    records = get_global_catalog()
    record = next(item for item in records if item["ecosystem_id"] == "GLOBAL-VIDEO-CORE-ECOSYSTEM")
    assert record["parent_id"] == "GLOBAL-CORE-ECOSYSTEM"
    assert record["metadata"]["core_catalog"].endswith("/global_video_core_ecosystem")

def test_master_catalog_is_read_only_reference():
    result = master_catalog_status()
    assert result["available"] is True
    assert result["access_mode"] == "READ_ONLY"
    assert result["target_unique_entries"] == 2468
