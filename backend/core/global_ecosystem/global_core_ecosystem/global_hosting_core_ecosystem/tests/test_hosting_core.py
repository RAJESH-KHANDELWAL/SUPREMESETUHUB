"""Structural, registry, classification and package-contract tests."""
import importlib
from pathlib import Path
from .catalog import ROOT_ID,get_catalog,list_providers
from .hosting_categories import HOSTING_CATEGORIES,classify_provider
from .manager import get_manager
ROOT=Path(__file__).resolve().parents[1]
def test_catalog_registry_and_lookup():
 rows=get_catalog();ids=[x["ecosystem_id"] for x in rows]
 assert rows[0]["ecosystem_id"]==ROOT_ID and len(ids)==len(set(ids))
 providers=list_providers();provider_ids=[x["provider_id"] for x in providers]
 assert len(provider_ids)==len(set(provider_ids)) and len(providers)>=150
 m=get_manager();assert m.status()["provider_count"]==len(providers)
 for p in providers:assert m.get_provider(p["provider_id"])["ecosystem_id"]==p["ecosystem_id"]
def test_taxonomy_and_entity_separation():
 assert len(HOSTING_CATEGORIES)>=12
 assert classify_provider("CPANEL")["entity_type"]=="PLATFORM_OR_TECHNOLOGY"
 assert classify_provider("APP_PLATFORM")["entity_type"]=="SERVICE_CATEGORY"
 assert classify_provider("AWS")["hosting_category"]=="CLOUD_VPS_DEDICATED"
 assert classify_provider("KINSTA")["hosting_category"]=="MANAGED_WORDPRESS"
def test_all_provider_packages_have_contract_files_and_import():
 for folder in ROOT.iterdir():
  if folder.is_dir() and folder.name.endswith("_hosting_core_ecosystem"):
   for name in ("manager.py","manager.php","__init__.py","README.md"):assert (folder/name).is_file(),f"{folder.name}/{name}"
   module=importlib.import_module(f"{__package__.rsplit('.',1)[0]}.{folder.name}.manager")
   assert module.get_manager().status()["live_connection_verified"] is False
