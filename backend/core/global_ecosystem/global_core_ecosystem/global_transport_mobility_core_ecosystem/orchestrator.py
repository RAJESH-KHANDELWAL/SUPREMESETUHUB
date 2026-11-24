"""Read-only discovery orchestration for transport and mobility taxonomy."""
from .manager import get_manager
class TransportMobilityCoreOrchestrator:
    def __init__(self): self.manager = get_manager()
    def status(self): return self.manager.status()
    def discover(self, query=None):
        items = self.manager.list_entries()["data"]["entries"]
        q = (query or "").strip().casefold()
        if q: items = [x for x in items if q in x["id"].casefold() or q in x["name"].casefold() or q in x["description"].casefold()]
        return {"success": True, "count": len(items), "entries": items, "execution_performed": False}
