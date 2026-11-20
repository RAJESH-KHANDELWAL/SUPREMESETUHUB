"""Manager for GLOBAL ENTITY RELATIONSHIPS CORE ECOSYSTEM."""
from __future__ import annotations
from .catalog import ROOT_ID,get_catalog,list_categories,get_category,RELATIONSHIP_TYPES
from .registry import EntityRelationshipRegistry
NAME="GLOBAL ENTITY RELATIONSHIPS CORE ECOSYSTEM"
MASTER_CATALOG_PATH="backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
MASTER_CATALOG_ID="GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"
MASTER_CATALOG_TARGET_UNIQUE_ENTRIES=2468
class GlobalEntityRelationshipsCoreManager:
    def __init__(self): self.registry=EntityRelationshipRegistry(get_catalog())
    def status(self): return {"success":True,"ecosystem_id":ROOT_ID,"name":NAME,"status":"CORE_CATALOG_ONLY","category_count":self.registry.count()-1,"relationship_type_count":len(RELATIONSHIP_TYPES),"live_connection_verified":False,"api_transport_in_core":False,"master_catalog_target_unique_entries":2468}
    def list_categories(self): return {"success":True,"count":len(list_categories()),"categories":list_categories()}
    def get_category(self,ecosystem_id): return self.registry.get(ecosystem_id)
    def relationship_types(self): return {"success":True,"count":len(RELATIONSHIP_TYPES),"types":list(RELATIONSHIP_TYPES)}
    def tree(self):
        nodes={r["ecosystem_id"]:{**r,"children":[]} for r in self.registry.list()}
        for r in self.registry.list():
            parent=r.get("parent_id")
            if parent in nodes: nodes[parent]["children"].append(nodes[r["ecosystem_id"]])
        return {"success":ROOT_ID in nodes,"tree":nodes.get(ROOT_ID)}
    def master_catalog_reference(self): return {"catalog_id":MASTER_CATALOG_ID,"target_unique_entries":2468,"source_path":MASTER_CATALOG_PATH,"owner_layer":"GLOBAL_ENGINE_ECOSYSTEM","access_mode":"READ_ONLY_ON_DEMAND","catalog_loaded":False,"note":"Reference only; this CORE manager does not copy or mutate numbered master catalog entries."}
_manager=None
def get_manager():
    global _manager
    if _manager is None: _manager=GlobalEntityRelationshipsCoreManager()
    return _manager
