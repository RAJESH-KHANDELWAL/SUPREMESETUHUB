"""Independent lifecycle manager for GLOBAL SERVER ENGINE."""
from .catalog import list_engines
from .provider_catalog import list_providers, get_provider
from .registry import EngineRegistry

class EcosystemEngineManager:
    def __init__(self):
        self.registry = EngineRegistry()
        self.catalog = list_engines()
        self.providers = list_providers()

    def register(self, key, value):
        return self.registry.register(key, value)

    def get(self, key):
        return self.registry.get(key)

    def unregister(self, key):
        return self.registry.unregister(key)

    def list(self):
        return {"success": True, "count": self.registry.count(),
                "engine_ids": list(self.registry.list_ids())}

    def provider(self, provider_id):
        try:
            return {"success": True, "provider": get_provider(provider_id)}
        except KeyError:
            return {"success": False, "error": "ENGINE_PROVIDER_NOT_FOUND"}

    def status(self):
        return {
            "success": True, "layer": "ENGINE",
            "ecosystem": "GLOBAL SERVER ENGINE",
            "catalog_count": len(self.catalog),
            "provider_count": len(self.providers),
            "registered_count": self.registry.count(),
            "status": "READY",
        }

__all__ = ["EcosystemEngineManager"]
