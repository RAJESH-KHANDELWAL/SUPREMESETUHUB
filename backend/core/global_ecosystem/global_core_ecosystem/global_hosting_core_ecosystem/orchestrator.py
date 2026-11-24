"""Hosting provider/domain discovery, health and dependency metadata."""
from .catalog import ROOT_ID,get_catalog,list_providers,get_provider
from .domain_catalog import hosting_domain_summary,list_hosting_domain_inventory
from .policy import HostingCorePolicy
class GlobalHostingCoreOrchestrator:
 def catalog(self):return get_catalog()
 def list_providers(self,*,provider_records_only=False,category=None):
  rows=list_providers()
  if provider_records_only:rows=[x for x in rows if x.get("is_provider_record")]
  if category:rows=[x for x in rows if x.get("hosting_category","").casefold()==category.casefold()]
  return {"success":True,"count":len(rows),"providers":[HostingCorePolicy.safe_summary(x) for x in rows]}
 def get_provider(self,key):
  row=get_provider(key);return HostingCorePolicy.safe_summary(row) if row else None
 def domains(self):return hosting_domain_summary()
 def domain_inventory(self):return list_hosting_domain_inventory()
 def health(self):
  rows=list_providers();domains=hosting_domain_summary();return {"success":True,"ecosystem_id":ROOT_ID,"status":"CORE_CATALOG_AVAILABLE","provider_record_count":len(rows),"classified_provider_count":sum(bool(x.get("classification_verified")) for x in rows),"domain_count":domains["domain_count"],"live_connections_verified":0,"api_calls_performed":0,"master_catalog_target_unique_entries":2468,"warning":"Catalog registration does not prove current availability, entitlement or live connectivity."}
 def dependency_map(self):
  rows=list_providers();return {"success":True,"nodes":[{"id":ROOT_ID,"type":"ecosystem"}]+[{"id":x["ecosystem_id"],"type":"provider_or_platform","parent_id":ROOT_ID} for x in rows],"edges":[{"from":ROOT_ID,"to":x["ecosystem_id"],"relationship":"REGISTERS_METADATA_FOR"} for x in rows]}
