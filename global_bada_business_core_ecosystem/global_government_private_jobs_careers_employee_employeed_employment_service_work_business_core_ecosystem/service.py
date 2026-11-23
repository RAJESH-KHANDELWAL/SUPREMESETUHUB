"""Employment-services taxonomy discovery and validation."""
from .catalog import get_catalog
from .domain_catalog import DOMAINS
from .policy import validate_provider_record
class EmploymentServicesBusinessService:
 def status(self): return {"success":True,"status":"CORE_CATALOG_READY","live_services_verified":False,"external_integrations":"NOT_CONFIGURED","domain_count":len(DOMAINS)}
 def catalog(self): return get_catalog()
 def search(self,query="",domain_id=None):
  q=query.casefold().strip(); selected=domain_id.upper() if domain_id else None; rows=[]
  for key,value in DOMAINS.items():
   if selected and key!=selected: continue
   for topic in value["topics"]:
    if not q or q in topic.replace("_"," ").casefold() or q in value["name"].casefold(): rows.append({"domain_id":key,"domain_name":value["name"],"service":topic})
  return rows
 def validate_provider(self,payload):
  errors=validate_provider_record(payload); return {"success":not errors,"status":"VALID" if not errors else "REJECTED","errors":errors}
