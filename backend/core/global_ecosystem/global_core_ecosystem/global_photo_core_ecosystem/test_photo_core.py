"""Structural and behavior tests for Global Photo Core."""
from backend.core.global_ecosystem.global_core_ecosystem.global_photo_core_ecosystem.catalog import get_catalog
from backend.core.global_ecosystem.global_core_ecosystem.global_photo_core_ecosystem.domain_catalog import DOMAIN_DEFINITIONS,domain_summary
from backend.core.global_ecosystem.global_core_ecosystem.global_photo_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.global_photo_core_ecosystem.master_catalog import master_catalog_status
def test_core_catalog_and_manager_are_consistent():
    c=get_catalog(); m=get_manager()
    assert c["ecosystem_id"]==m.ECOSYSTEM_ID
    assert c["provider_count"]==len(c["providers"])
    assert m.status()["success"] is True
    assert m.status()["live_connections_verified"]==0
def test_domain_inventory_is_valid():
    assert DOMAIN_DEFINITIONS
    s=domain_summary()
    assert s["domain_count"]==len(DOMAIN_DEFINITIONS)
    assert sum(x["provider_count"] for x in s["domains"])==s["provider_count"]
def test_no_unverified_provider_is_claimed():
    for p in get_catalog()["providers"]:
        assert p["connected"] is False and p["live_connection_verified"] is False
def test_global_core_hierarchy_registers_photo_core():
    from backend.core.global_ecosystem.global_core_ecosystem.manager import get_catalog as get_global_catalog
    records = get_global_catalog()
    record = next(item for item in records if item["ecosystem_id"] == "GLOBAL-PHOTO-CORE-ECOSYSTEM")
    assert record["parent_id"] == "GLOBAL-CORE-ECOSYSTEM"
    assert record["metadata"]["core_catalog"].endswith("/global_photo_core_ecosystem")

def test_master_catalog_is_read_only_reference():
    assert master_catalog_status()["access_mode"]=="READ_ONLY"
