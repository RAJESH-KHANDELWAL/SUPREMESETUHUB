"""Read-only manager, orchestration and policy for transport taxonomy."""
from .catalog import ECOSYSTEM_ID, PARENT_ID, STATUS, list_catalog

CORE_POLICY = {"catalogue_only_by_default": True, "provider_api_calls_in_core": False, "route_execution_in_core": False, "booking_dispatch_in_core": False, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY", "live_connection_requires_smoke_test": True}

class TransportMobilityCoreManager:
    def status(self):
        return {"success": True, "ecosystem_id": ECOSYSTEM_ID, "parent_id": PARENT_ID, "status": STATUS, "entry_count": len(list_catalog()), "policy": dict(CORE_POLICY), "live_connection_verified": False}
    def list_entries(self):
        items = list_catalog()
        return {"success": True, "count": len(items), "entries": items}
    def get_entry(self, entry_id):
        key = str(entry_id).strip().upper()
        if not key: raise ValueError("IDENTIFIER_REQUIRED")
        return next((item for item in list_catalog() if item["id"] == key), None)

class TransportMobilityCoreOrchestrator:
    def __init__(self): self.manager = TransportMobilityCoreManager()
    def discover(self, query=None):
        items = self.manager.list_entries()["entries"]
        q = (query or "").strip().casefold()
        if q: items = [x for x in items if q in x["id"].casefold() or q in x["name"].casefold() or q in x["description"].casefold()]
        return {"success": True, "count": len(items), "entries": items, "execution_performed": False}

class TransportMobilityCoreService:
    def __init__(self): self.orchestrator = TransportMobilityCoreOrchestrator()
    def status(self): return self.orchestrator.manager.status()
    def discover(self, query=None): return self.orchestrator.discover(query)

def get_manager(): return TransportMobilityCoreManager()
