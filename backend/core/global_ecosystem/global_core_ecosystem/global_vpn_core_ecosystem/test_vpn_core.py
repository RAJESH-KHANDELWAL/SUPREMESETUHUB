"""Offline structural and behavior tests for Global VPN Core."""
import importlib
from pathlib import Path
import pytest
from .catalog import PROVIDERS,get_catalog
from .contracts import validate_request
from .domain_catalog import DOMAIN_DEFINITIONS,domain_summary
from .domain_runtime import VPNCoreDomainManager
from .master_catalog import get_master_catalog_mapping
from .manager import get_manager
ROOT=Path(__file__).resolve().parent
REPO_ROOT=Path(__file__).resolve().parents[5]
EXPECTED={"wireguard","openvpn","tailscale","protonvpn"}
def test_provider_inventory_matches_existing_vpn_registry():
 assert {p["provider_id"] for p in PROVIDERS}==EXPECTED and len(PROVIDERS)==4
 for p in PROVIDERS:
  assert (ROOT/p["directory"]).is_dir()
  assert (REPO_ROOT/p["source_service_ref"]).is_file()
def test_each_provider_package_has_exact_four_purposeful_files():
 expected={"README.md","__init__.py","provider.py","contracts.py"}
 for p in PROVIDERS:
  folder=ROOT/p["directory"]
  assert {x.name for x in folder.iterdir() if x.is_file()}==expected
  provider=importlib.import_module(f"{__package__}.{p['directory']}.provider")
  contract=importlib.import_module(f"{__package__}.{p['directory']}.contracts")
  assert provider.get_provider()["provider_id"]==p["provider_id"]
  assert contract.validate_request({"operation":"describe"})["validated_only"] is True
def test_domains_and_read_only_runtime():
 assert len(DOMAIN_DEFINITIONS)==18 and domain_summary()["domain_count"]==18
 for key in DOMAIN_DEFINITIONS:assert VPNCoreDomainManager(key).list_offerings()["provider_count"]==4
def test_manager_does_not_claim_live_vpn_connections():
 m=get_manager();assert m.status()["provider_count"]==4
 assert m.health()["connected_provider_count"]==0 and get_catalog()["live_connection_verified"] is False
def test_contract_rejects_private_keys_and_unknown_providers():
 with pytest.raises(ValueError,match="SECRET_MATERIAL"):validate_request({"provider_id":"wireguard","private_key":"never-accept"})
 with pytest.raises(ValueError,match="UNKNOWN_VPN_PROVIDER"):validate_request({"provider_id":"not-real"})
def test_master_mapping_uses_existing_taxonomy_only():
 result=get_master_catalog_mapping();assert result["success"] is True
 assert result["target_unique_entries"]==2468 and result["taxonomy_entries_added"]==0
 assert len(result["entries"])==6
