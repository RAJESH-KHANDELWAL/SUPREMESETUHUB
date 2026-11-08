"""Independent manager for GLOBAL SERVER ENGINE; no API/CORE delegation."""
from .catalog import list_engines
from .registry import EngineRegistry


class EcosystemEngineManager:
    def __init__(self):
        self.registry = EngineRegistry()
        self.catalog = list_engines()

    def register(self, key, value):
        return self.registry.register(key, value)

    def get(self, key):
        return self.registry.get(key)

    def unregister(self, key):
        return self.registry.unregister(key)

    def list(self):
        return {"success": True, "count": self.registry.count(),
                "engine_ids": list(self.registry.list_ids())}

    def status(self):
        return {
            "success": True,
            "layer": "ENGINE",
            "ecosystem": "GLOBAL SERVER",
            "catalog_count": len(self.catalog),
            "registered_count": self.registry.count(),
            "status": "READY",
        }


__all__ = ["EcosystemEngineManager"]
