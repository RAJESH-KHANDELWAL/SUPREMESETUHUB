"""DATABASE ecosystem service for provider catalog and server inventory."""
from .registry import list_providers, get_provider
from .server_inventory_repository import ServerInventoryRepository
from .models import ServerInventoryRecord

class GlobalDatabaseEcosystemService:
    domain = "DATABASE"
    ecosystem = "GLOBAL_DATABASE_ECOSYSTEM"

    def __init__(self, repository=None):
        self.server_inventory = repository or ServerInventoryRepository()

    def describe(self):
        providers = list_providers()
        return {
            "domain": self.domain, "ecosystem": self.ecosystem,
            "providers": providers, "provider_count": len(providers),
            "server_inventory_count": self.server_inventory.count(),
            "live_provider_connections_enabled": False,
            "persistence_backend": "IN_MEMORY_REFERENCE_ADAPTER",
            "durable_persistence_enabled": False,
        }

    def list_providers(self):
        items = list_providers()
        return {"success": True, "count": len(items), "providers": items}

    def get_provider(self, provider_id):
        try:
            return {"success": True, "provider": get_provider(provider_id)}
        except KeyError:
            return {"success": False, "error": "DATABASE_PROVIDER_NOT_FOUND"}

    def create_server_inventory(self, record):
        try:
            model = record if isinstance(record, ServerInventoryRecord) else ServerInventoryRecord(**dict(record))
            return {"success": True, "record": self.server_inventory.create(model)}
        except (TypeError, ValueError) as exc:
            return {"success": False, "error": "DATABASE_SERVER_INVENTORY_CREATE_FAILED", "message": str(exc)}

    def get_server_inventory(self, server_id):
        item = self.server_inventory.get(server_id)
        return {"success": True, "record": item} if item is not None else None

    def list_server_inventory(self):
        items = self.server_inventory.list()
        return {"success": True, "count": len(items), "records": items}

    def update_server_inventory(self, server_id, **changes):
        try:
            item = self.server_inventory.update(server_id, **changes)
            return {"success": True, "record": item} if item is not None else None
        except ValueError as exc:
            return {"success": False, "error": "DATABASE_SERVER_INVENTORY_UPDATE_FAILED", "message": str(exc)}
