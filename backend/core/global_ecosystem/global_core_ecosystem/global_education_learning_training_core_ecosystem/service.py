from .domain_catalog import list_domains,get_domain
from .catalog import get_catalog
class EducationDomainService:
 def list_domains(self): return list_domains()
 def get_domain(self,domain_id): return get_domain(domain_id)
 def search(self,keyword):
  term=keyword.strip().casefold()
  return [d for d in list_domains() if term and (term in d["name"].casefold() or term in d["description"].casefold() or term in d["domain_id"])]
 def catalog(self): return get_catalog()
 def status(self): return {"status":"HEALTHY","domain_count":len(list_domains()),"mode":"READ_ONLY"}
