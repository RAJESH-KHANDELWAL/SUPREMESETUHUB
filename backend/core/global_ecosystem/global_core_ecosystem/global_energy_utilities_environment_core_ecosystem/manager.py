"""Canonical manager with read-only 2468 master-catalog bridge."""
import json
from pathlib import Path
from .catalog import get_catalog
from .domain_catalog import list_domains,get_domain,search_domains
from .region_catalog import list_regional_frameworks,get_regional_framework
from .orchestrator import EnergyEnvironmentCoreOrchestrator
class GlobalEnergyUtilitiesEnvironmentCoreManager:
 NAME="GLOBAL ENERGY UTILITIES & ENVIRONMENT CORE ECOSYSTEM"
 MASTER_CATALOG_PATH=Path(__file__).resolve().parents[5]/"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
 MASTER_CATALOG_ID="GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"
 MASTER_CATALOG_TARGET=2468
 def __init__(self): self._orchestrator=EnergyEnvironmentCoreOrchestrator()
 def catalog(self): return get_catalog()
 def list_domains(self): return list_domains()
 def get_domain(self,domain_id): return get_domain(domain_id)
 def search(self,keyword): return search_domains(keyword)
 def regions(self): return list_regional_frameworks()
 def get_region(self,region_id): return get_regional_framework(region_id)
 def health(self): return self._orchestrator.health()
 def status(self): return {**self.health(),"name":self.NAME,"master_catalog":self.master_catalog_reference()}
 def master_catalog_reference(self): return {"catalogue_id":self.MASTER_CATALOG_ID,"source_path":"backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json","access_mode":"READ_ONLY_ON_DEMAND","target_unique_entries":2468}
 def master_catalog_inventory(self):
  if not self.MASTER_CATALOG_PATH.is_file(): raise FileNotFoundError("MASTER_CATALOG_NOT_FOUND")
  data=json.loads(self.MASTER_CATALOG_PATH.read_text(encoding="utf-8")); e=data.get("expansion",{}); c=data.get("counts",{})
  t,n=e.get("target_unique_entries"),e.get("current_unique_entries")
  if data.get("catalogue_id")!=self.MASTER_CATALOG_ID or t!=2468 or n!=c.get("unique_catalogue_entries") or e.get("remaining_unique_entries")!=t-n: raise ValueError("MASTER_CATALOG_INTEGRITY_ERROR")
  return {"success":True,"target_unique_entries":t,"current_unique_entries":n,"remaining_unique_entries":t-n,"access_mode":"READ_ONLY"}
def get_manager(): return GlobalEnergyUtilitiesEnvironmentCoreManager()
