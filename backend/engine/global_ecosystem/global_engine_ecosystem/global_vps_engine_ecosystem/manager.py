"""Independent manager for GLOBAL VPS; no API/CORE delegation."""
from .catalog import list_engines
from .registry import EngineRegistry
class EcosystemEngineManager:
    def __init__(self): self.registry=EngineRegistry(); self.catalog=list_engines()
    def register(self,key,value): return self.registry.register(key,value)
    def get(self,key): return self.registry.get(key)
    def status(self): return {"layer":"ENGINE","ecosystem":"GLOBAL VPS","catalog_count":len(self.catalog),"registered_count":self.registry.count(),"status":"READY"}
