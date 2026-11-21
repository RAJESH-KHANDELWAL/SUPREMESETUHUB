"""Structural and behavior tests for Global VPS Core."""
import importlib
from pathlib import Path
import pytest
from .catalog import PROVIDERS,get_catalog
from .contracts import validate_request
from .domain_catalog import DOMAIN_DEFINITIONS,domain_summary
from .domain_runtime import VPSCoreDomainManager
from .master_catalog import get_master_catalog_mapping
from .manager import get_manager
ROOT=Path(__file__).resolve().parent
def test_provider_inventory_and_packages():
 assert len(PROVIDERS)==20 and len({p["provider_id"] for p in PROVIDERS})==20
 for p in PROVIDERS:
  folder=ROOT/p["directory"];assert folder.is_dir() and (folder/"provider.py").is_file()
  mod=importlib.import_module(f"{__package__}.{p['directory']}.provider");assert mod.get_provider()["provider_id"]==p["provider_id"]
def test_domains_and_runtime():
 assert len(DOMAIN_DEFINITIONS)==16 and domain_summary()["domain_count"]==16
 for key in DOMAIN_DEFINITIONS:assert VPSCoreDomainManager(key).list_offerings()["count"]==20
def test_manager_status_is_not_live():
 m=get_manager();assert m.status()["provider_count"]==20;assert m.health()["connected_provider_count"]==0;assert get_catalog()["live_connection_verified"] is False
def test_contract_blocks_secrets_and_unknown_provider():
 with pytest.raises(ValueError,match="SECRET_MATERIAL"):validate_request({"provider_id":"aws","api_key":"x"})
 with pytest.raises(ValueError,match="UNKNOWN_VPS_PROVIDER"):validate_request({"provider_id":"nope"})
def test_master_mapping_does_not_expand_taxonomy():
 x=get_master_catalog_mapping();assert x["success"] and x["target_unique_entries"]==2468 and x["taxonomy_entries_added"]==0
 assert {e["entry_id"] for e in x["entries"]}=={"S09_cloud_computing","S10_global_server"}
