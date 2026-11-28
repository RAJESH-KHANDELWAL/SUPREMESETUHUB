"""Hosting domain inventory derived from the canonical provider catalog."""
from .catalog import list_providers
from .hosting_categories import HOSTING_CATEGORIES
DOMAIN_DEFINITIONS={k:{"domain_id":k,"name":v["name"],"purpose":v["description"],"module":f"global_{k.lower()}_hosting_core_ecosystem"} for k,v in HOSTING_CATEGORIES.items()}
def list_hosting_domain_inventory():
 rows=list_providers();out=[]
 for key,value in DOMAIN_DEFINITIONS.items():
  ids=sorted(x["provider_id"] for x in rows if x.get("hosting_category")==key);out.append({"domain_id":key,**value,"provider_count":len(ids),"provider_ids":ids})
 return out
def hosting_domain_summary():
 rows=list_hosting_domain_inventory();return {"success":True,"domain_count":len(rows),"provider_count":sum(x["provider_count"] for x in rows),"domains":rows}
def get_hosting_domain(domain_id):
 needle=domain_id.strip().casefold();return next((x for x in list_hosting_domain_inventory() if x["domain_id"].casefold()==needle or x["name"].casefold()==needle),None)
