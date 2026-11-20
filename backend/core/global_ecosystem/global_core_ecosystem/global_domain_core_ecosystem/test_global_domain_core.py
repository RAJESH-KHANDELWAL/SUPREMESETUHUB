"""Tests for GLOBAL DOMAIN CORE ECOSYSTEM naming, catalog and inventory."""
from .catalog import PROVIDER_DIRECTORIES, DOMAIN_DEFINITIONS, SECTOR_ECOSYSTEMS, ECOSYSTEM_ID, ECOSYSTEM_NAME
from .manager import get_manager
from .sector_catalog import SECTORS, list_sectors
from .provider_registry import list_expanded_provider_registry

def test_global_domain_root_name_and_id_standard():
    assert ECOSYSTEM_NAME == "GLOBAL DOMAIN CORE ECOSYSTEM"
    assert ECOSYSTEM_ID == "GLOBAL-DOMAIN-CORE-ECOSYSTEM"

def test_legacy_provider_inventory_nonempty_unique():
    assert len(PROVIDER_DIRECTORIES)>50
    assert len(set(PROVIDER_DIRECTORIES))==len(PROVIDER_DIRECTORIES)

def test_sector_names_ids_and_registry_unique():
    sectors=list_sectors()
    assert len(sectors)>=35
    assert len({s["sector_id"] for s in sectors})==len(sectors)
    assert len({s["ecosystem_id"] for s in sectors})==len(sectors)
    assert all(s["description"].strip() for s in sectors)
    assert all(s["ecosystem_name"].startswith("GLOBAL ") for s in sectors)
    assert all(s["ecosystem_name"].endswith(" CORE ECOSYSTEM") for s in sectors)
    assert all(s["ecosystem_id"].startswith("GLOBAL-") and s["ecosystem_id"].endswith("-CORE-ECOSYSTEM") for s in sectors)
    assert all(s["naming_standard"]=="GLOBAL + SUBJECT + CORE ECOSYSTEM" for s in sectors)

def test_catalog_registers_all_sector_ecosystems():
    assert len(SECTOR_ECOSYSTEMS)==len(SECTORS)
    assert all(row["parent_id"]==ECOSYSTEM_ID for row in SECTOR_ECOSYSTEMS)
    assert all(row["name"].startswith("GLOBAL ") and row["name"].endswith(" CORE ECOSYSTEM") for row in SECTOR_ECOSYSTEMS)

def test_provider_registry_catalog_only_and_unique():
    rows=list_expanded_provider_registry()
    assert len(rows)>=100
    assert len({r["provider_id"] for r in rows})==len(rows)
    assert all(r["catalog_status"]=="CATALOG_ONLY" and not r["connected"] for r in rows)
    assert all(r["adapter_status"]=="NOT_IMPLEMENTED" for r in rows)

def test_domain_catalog_has_expected_definitions():
    assert len(DOMAIN_DEFINITIONS)>=15
    assert all(v.get("purpose") for v in DOMAIN_DEFINITIONS.values())

def test_manager_exposes_sector_catalog_and_status():
    manager=get_manager()
    status=manager.status()
    assert status["success"] is True
    assert status["live_connection_verified"] is False
    assert status["naming_standard"]=="GLOBAL + SUBJECT + CORE ECOSYSTEM"
    assert status["sector_ecosystem_count"]==len(SECTORS)
    assert len(manager.list_sector_ecosystems())==len(SECTORS)
    assert manager.get_sector_ecosystem("GLOBAL-DNSSEC-CORE-ECOSYSTEM") is not None

def test_unknown_domain_is_safe():
    result=get_manager().get_domain_manager("NOT_A_DOMAIN").status()
    assert result["success"] is False
