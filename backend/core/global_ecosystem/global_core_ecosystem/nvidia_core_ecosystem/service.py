from .orchestrator import NvidiaCoreOrchestrator
class NvidiaCoreService:
 def __init__(self):self.o=NvidiaCoreOrchestrator()
 def status(self):
  c=self.o.catalog();h=self.o.health();return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":c["name"],"provider":c["provider"],"status":c["status"],"product_count":h["product_count"],"domain_count":h["domain_count"],"live_connection_verified":False,"api_calls_performed":0,"master_catalog":c["master_catalog"]}
 def health(self):return self.o.health()
 def products(self,enabled_only=False):return self.o.products(enabled_only)
 def product(self,k):return self.o.product(k)
 def domains(self):return self.o.domains()
 def dependency_map(self):return self.o.dependency_map()
