from .domain_catalog import list_domains,get_domain,search_domains
class IndependentWorkService:
 def list_domains(self): return list_domains()
 def get_domain(self,domain_id): return get_domain(domain_id)
 def search(self,keyword): return search_domains(keyword)
 def status(self): return {"status":"HEALTHY","domain_count":len(list_domains()),"mode":"READ_ONLY_DISCOVERY","integrations":"NOT_CONFIGURED"}
