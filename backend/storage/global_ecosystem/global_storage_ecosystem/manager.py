"""Independent GLOBAL STORAGE ECOSYSTEM hierarchy manager."""
from datetime import datetime, timezone
from .catalog import ROOT_ID,get_catalog,get_provider_catalog,get_category_catalog
from .ecosystem_registry import StorageEcosystemRegistry
from .models import StorageEcosystemIdentity
class GlobalStorageEcosystemManager:
    ROOT_ID=ROOT_ID; ROOT_NAME="GLOBAL STORAGE ECOSYSTEM"; VERSION="2.0.0"
    def __init__(self):
        self.registry=StorageEcosystemRegistry(); self._initialize()
    def _initialize(self):
        seen=set()
        for record in get_catalog():
            item=StorageEcosystemIdentity(**record)
            if item.ecosystem_id in seen: raise RuntimeError("Duplicate STORAGE ecosystem ID: "+item.ecosystem_id)
            if item.parent_id and item.parent_id not in seen: raise RuntimeError("Parent must precede child: "+item.ecosystem_id)
            self.registry.register(item); seen.add(item.ecosystem_id)
        if self.ROOT_ID not in seen: raise RuntimeError("STORAGE root missing")
    def status(self):
        ready=self.registry.exists(self.ROOT_ID)
        return {"success":ready,"ecosystem_id":self.ROOT_ID,"name":self.ROOT_NAME,"version":self.VERSION,"status":"FOUNDATION_READY" if ready else "NOT_INITIALIZED","count":self.registry.count(),"timestamp":datetime.now(timezone.utc).isoformat(),"layer":"STORAGE","independent":True}
    def health(self):
        ready=self.registry.exists(self.ROOT_ID)
        return {"success":ready,"service":self.ROOT_NAME,"status":"FOUNDATION_HEALTHY" if ready else "DEGRADED","registry_available":True,"registry_count":self.registry.count(),"provider_connections_verified":False,"note":"Catalog and hierarchy only; live adapters are not configured."}
    def list(self):
        values=self.registry.list(); return {"success":True,"count":len(values),"ecosystems":values}
    def names(self):
        values=self.registry.names(); return {"success":True,"count":len(values),"names":values}
    def get(self,ecosystem_id): return self.registry.get(ecosystem_id)
    def exists(self,ecosystem_id): return self.registry.exists(ecosystem_id)
    def register(self,identity):
        try:
            item=identity if isinstance(identity,StorageEcosystemIdentity) else StorageEcosystemIdentity(**identity)
            return {"success":True,"ecosystem":self.registry.register(item)}
        except (TypeError,ValueError,KeyError) as exc: return {"success":False,"error":"REGISTRATION_FAILED","message":str(exc)}
    def providers(self):
        values=get_provider_catalog(); return {"success":True,"count":len(values),"providers":values}
    def runtime_status(self):
        """Return physical provider health separately from catalog readiness."""
        from .provider_runtime import StorageProviderRuntime
        return StorageProviderRuntime().status()
    def categories(self):
        values=get_category_catalog(); return {"success":True,"count":len(values),"categories":values}
    def get_provider(self,provider_id):
        from .registry import get_provider
        return get_provider(provider_id)
    def tree(self):
        values=self.registry.list(); nodes={x["ecosystem_id"]:{**x,"children":[]} for x in values}
        for x in values:
            if x.get("parent_id") in nodes: nodes[x["parent_id"]]["children"].append(nodes[x["ecosystem_id"]])
        root=nodes.get(self.ROOT_ID); return {"success":root is not None,"tree":root}
    def connection_map(self):
        values=self.registry.list(); edges=[{"source":x["parent_id"],"target":x["ecosystem_id"],"relationship":"CONTAINS"} for x in values if x.get("parent_id")]
        return {"success":True,"node_count":len(values),"edge_count":len(edges),"edges":edges}
StorageEcosystemManager=GlobalStorageEcosystemManager
