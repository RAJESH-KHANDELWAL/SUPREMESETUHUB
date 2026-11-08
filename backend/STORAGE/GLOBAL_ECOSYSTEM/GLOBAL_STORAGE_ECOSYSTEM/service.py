"""GLOBAL STORAGE ECOSYSTEM service facade; storage remains STORAGE-owned."""
from .registry import list_providers, get_provider


class EcosystemService:
    domain = "STORAGE"
    ecosystem = "GLOBAL_STORAGE_ECOSYSTEM"

    def describe(self):
        providers = list_providers()
        return {
            "domain": self.domain,
            "ecosystem": self.ecosystem,
            "providers": providers,
            "provider_count": len(providers),
            "live_connections_enabled": False,
            "file_operations_enabled": False,
        }

    def list_providers(self):
        items = list_providers()
        return {"success": True, "count": len(items), "providers": items}

    def get_provider(self, provider_id):
        try:
            return {"success": True, "provider": get_provider(provider_id)}
        except KeyError:
            return {"success": False, "error": "STORAGE_PROVIDER_NOT_FOUND"}
