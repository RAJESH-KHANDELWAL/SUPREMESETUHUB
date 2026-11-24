from .catalog import get_catalog,get_modules,get_module
from .domain_catalog import domain_inventory,domain_summary
from .master_catalog import get_master_summary
class GlobalIndividualCoreOrchestrator:
    def modules(self): return {"items":get_modules(),"count":len(get_modules())}
    def get_module(self,module_id): return get_module(module_id)
    def domains(self): return domain_inventory()
    def domain_summary(self): return domain_summary()
    def master_catalog(self): return get_master_summary()
    def health(self): return {"status":"HEALTHY_METADATA_ONLY","catalog_loaded":True,"api_calls":0,"connected":False,"persistence_enabled":False}
