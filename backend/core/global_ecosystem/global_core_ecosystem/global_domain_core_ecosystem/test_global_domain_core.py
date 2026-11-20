"""Expanded Domain Core inventory tests."""
from .catalog import PROVIDER_DIRECTORIES, DOMAIN_DEFINITIONS
from .manager import get_manager
from .sector_catalog import SECTORS, list_sectors
from .provider_registry import list_expanded_provider_registry

def test_legacy_provider_inventory_nonempty_unique():
    assert len(PROVIDER_DIRECTORIES)>50
    assert len(set(PROVIDER_DIRECTORIES))==len(PROVIDER_DIRECTORIES)

def test_expanded_sectors_are_meaningful_and_unique():
    sectors=list_sectors()
    assert len(sectors)>=35
    assert len({s["sector_id"] for s in sectors})==len(sectors)
    assert all(s["description"].strip() for s in sectors)
    assert all(s["ecosystem_name"].startswith("GLOBAL ") for s in sectors)
    assert all(s["ecosystem_name"].endswith(" CORE ECOSYSTEM") for s in sectors)
    assert all(s["ecosystem_id"].startswith("GLOBAL-") and s["ecosystem_id"].endswith("-CORE-ECOSYSTEM") for s in sectors)

def test_provider_registry_scales_and_is_explicitly_catalog_only():
    rows=list_expanded_provider_registry()
    assert len(rows)>=100
    assert len({r["provider_id"] for r in rows})==len(rows)
    assert all(r["catalog_status"]=="CATALOG_ONLY" and not r["connected"] for r in rows)
    assert all(r["adapter_status"]=="NOT_IMPLEMENTED" for r in rows)

def test_domain_catalog_has_expected_definitions():
    assert len(DOMAIN_DEFINITIONS)>=15
    assert all(v.get("purpose") for v in DOMAIN_DEFINITIONS.values())

def test_manager_status_is_catalog_only():
    status=get_manager().status()
    assert status["success"] is True
    assert status["live_connection_verified"] is False

def test_unknown_domain_is_safe():
    result=get_manager().get_domain_manager("NOT_A_DOMAIN").status()
    assert result["success"] is False
