"""GLOBAL DATABASE ECOSYSTEM service facade; persistence stays DATABASE-owned."""
from .registry import list_providers, get_provider


class GlobalDatabaseEcosystemService:
    domain = "DATABASE"
    ecosystem = "GLOBAL_DATABASE_ECOSYSTEM"

    def describe(self):
        providers = list_providers()
        return {
            "domain": self.domain,
            "ecosystem": self.ecosystem,
            "providers": providers,
            "provider_count": len(providers),
            "live_connections_enabled": False,
            "persistence_enabled": False,
        }

    def list_providers(self):
        return {"success": True, "count": len(list_providers()), "providers": list_providers()}

    def get_provider(self, provider_id):
        try:
            return {"success": True, "provider": get_provider(provider_id)}
        except KeyError:
            return {"success": False, "error": "DATABASE_PROVIDER_NOT_FOUND"}
