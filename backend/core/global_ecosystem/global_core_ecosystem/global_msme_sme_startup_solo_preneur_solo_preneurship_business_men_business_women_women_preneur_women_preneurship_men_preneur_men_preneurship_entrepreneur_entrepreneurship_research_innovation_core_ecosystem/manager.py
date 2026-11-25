"""Canonical CORE manager and read-only 2468 master catalog bridge."""
import json
from pathlib import Path
from .catalog import get_catalog
from .domain_catalog import list_domains,get_domain,search_domains,validate_domains
from .policy import get_policy
class GlobalMSMESMEStartupEntrepreneurshipCoreManager:
 NAME="GLOBAL MSME SME STARTUP SOLO-PRENEUR BUSINESS MEN BUSINESS WOMEN WOMEN-PRENEUR MEN-PRENEUR ENTREPRENEUR ENTREPRENEURSHIP RESEARCH INNOVATION CORE ECOSYSTEM"
 MASTER_CATALOG_PATH=Path(__file__).resolve().parents[4]/"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
 MASTER_CATALOG_ID="GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"
 def catalog(self): return get_catalog()
 def list_domains(self): return list_domains()
 def get_domain(self,key): return get_domain(key)
 def search(self,q): return search_domains(q)
 def policy(self): return get_policy()
 def health(self): return {"healthy":validate_domains()["valid"],"domain_count":len(list_domains()),"mode":"taxonomy_only"}
 def master_catalog_reference(self): return {"catalogue_id":self.MASTER_CATALOG_ID,"source_path":"backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json","access_mode":"READ_ONLY_ON_DEMAND","target_unique_entries":2468}
 def master_catalog_inventory(self):
  data=json.loads(self.MASTER_CATALOG_PATH.read_text(encoding="utf-8")); e=data["expansion"]; c=data["counts"]; t=e["target_unique_entries"]; n=e["current_unique_entries"]
  if data["catalogue_id"]!=self.MASTER_CATALOG_ID or t!=2468 or n!=c["unique_catalogue_entries"] or e["remaining_unique_entries"]!=t-n: raise ValueError("MASTER_CATALOG_INTEGRITY_ERROR")
  return {"success":True,"target_unique_entries":t,"current_unique_entries":n,"remaining_unique_entries":t-n,"access_mode":"READ_ONLY"}
def get_manager(): return GlobalMSMESMEStartupEntrepreneurshipCoreManager()
