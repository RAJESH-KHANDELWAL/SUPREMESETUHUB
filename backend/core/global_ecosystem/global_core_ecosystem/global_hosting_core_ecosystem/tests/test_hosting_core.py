"""Hosting Core architecture, inventory and master-catalog tests."""
import importlib,json
from pathlib import Path
from .catalog import ROOT_ID,get_catalog,list_providers
from .hosting_categories import HOSTING_CATEGORIES,classify_provider
from .manager import get_manager
ROOT=Path(__file__).resolve().parents[1]
def test_inventory_and_unique_ids():
 rows=get_catalog();ids=[x["ecosystem_id"] for x in rows];providers=list_providers();pids=[x["provider_id"] for x in providers]
 assert rows[0]["ecosystem_id"]==ROOT_ID and len(ids)==len(set(ids))
 assert len(providers)==206 and len(pids)==len(set(pids))
 assert get_manager().status()["provider_count"]==len(providers)
 for p in providers:assert get_manager().get_provider(p["provider_id"])["ecosystem_id"]==p["ecosystem_id"]
def test_taxonomy_and_classification():
 assert len(HOSTING_CATEGORIES)==16
 assert classify_provider("CPANEL")["entity_type"]=="PLATFORM_OR_TECHNOLOGY"
 assert classify_provider("APP_PLATFORM")["entity_type"]=="SERVICE_CATEGORY"
 assert classify_provider("AWS")["hosting_category"]=="CLOUD_VPS_DEDICATED"
 assert classify_provider("KINSTA")["hosting_category"]=="MANAGED_WORDPRESS"
def test_master_catalog_read_only_reference():
 data=json.loads((ROOT.parents[3]/"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json").read_text(encoding="utf-8"))
 assert data["expansion"]["target_unique_entries"]==2468 and data["expansion"]["current_unique_entries"]==246
 rows=[x for x in data["ecosystem_module_index"]["modules"] if x["ecosystem_id"]==ROOT_ID]
 assert len(rows)==1 and rows[0]["provider_directory_count"]==206
def test_all_provider_and_domain_packages_have_contract_files():
 for folder in ROOT.iterdir():
  if folder.is_dir() and folder.name.endswith("_hosting_core_ecosystem"):
   for name in ("manager.py","manager.php","__init__.py","README.md"):assert (folder/name).is_file(),f"{folder.name}/{name}"
   module=importlib.import_module(f"{__package__.rsplit('.',1)[0]}.{folder.name}.manager")
   assert module.get_manager().status()["live_connection_verified"] is False
def test_policy_requires_tenant_context():
 from .contracts import TenantContext
 from .policy import HostingCorePolicy,HostingCorePolicyError
 try:HostingCorePolicy.require_tenant_context(None)
 except HostingCorePolicyError as exc:assert str(exc)=="TENANT_CONTEXT_REQUIRED"
 else:raise AssertionError("tenant context should be required")
 assert TenantContext("tenant","actor").validate() is None
