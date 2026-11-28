from .domain_catalog import list_business_domains,get_business_domain,validate_business_domains
from .catalog import get_catalog
class EducationBusinessService:
 def list_domains(self): return list_business_domains()
 def get_domain(self,domain_id): return get_business_domain(domain_id)
 def filter_by_capability(self,capability):
  key=capability.strip().upper()
  return [d for d in list_business_domains() if key in d["capabilities"]] if key in {"SERVICE","WORK","BUSINESS"} else []
 def search(self,keyword):
  term=keyword.strip().casefold()
  return [d for d in list_business_domains() if term and (term in d["name"].casefold() or term in d["description"].casefold() or term in d["domain_id"])]
 def validation(self): return validate_business_domains()
 def catalog(self): return get_catalog()
 def status(self): return {"status":"HEALTHY" if validate_business_domains()["valid"] else "DEGRADED","domain_count":len(list_business_domains()),"mode":"METADATA_ONLY"}
