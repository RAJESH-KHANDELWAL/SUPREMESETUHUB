"""Independent SERVER domain application service."""
from .config import ServerConfig
from .exceptions import ServerValidationError, ServerNotFoundError
from .health import ServerHealthService
from .lifecycle import ServerLifecycleService
from .models import ServerRecord
from .registry import ServerRegistry
from .global_ecosystem.global_server_ecosystem import ServerProviderRegistry

SERVER_TYPES = {"WEB", "VPS", "CLOUD", "VPN", "DATABASE", "APPLICATION", "DEDICATED", "CONTAINER"}

class ServerService:
    domain = "SERVER"
    version = "1.0.0"
    def __init__(self, registry=None, provider_registry=None, config=None):
        self.config = config or ServerConfig()
        self.registry = registry or ServerRegistry()
        self.providers = provider_registry or ServerProviderRegistry()
        self.lifecycle = ServerLifecycleService(self.registry)
        self.health_service = ServerHealthService(self.registry, self.providers)
    def register(self, name, server_type, provider="local", region="global", metadata=None):
        clean_name = str(name or "").strip()
        kind = str(server_type or "").strip().upper()
        if not clean_name: raise ServerValidationError("SERVER_NAME_REQUIRED")
        if kind not in SERVER_TYPES: raise ServerValidationError(f"UNSUPPORTED_SERVER_TYPE: {kind}")
        record = ServerRecord(clean_name, kind, str(provider or "local").strip().lower(),
                              str(region or "global").strip(), metadata=dict(metadata or {}))
        return self.registry.create(record).to_dict()
    def get(self, server_id):
        record = self.registry.get(server_id)
        if record is None: raise ServerNotFoundError(f"Unknown server: {server_id}")
        return record.to_dict()
    def list(self): return [record.to_dict() for record in self.registry.list()]
    def start(self, server_id): return self.lifecycle.start(server_id)
    def stop(self, server_id): return self.lifecycle.stop(server_id)
    def health(self): return self.health_service.health()
    def describe(self):
        return {"domain": self.domain, "version": self.version, "config": self.config.describe(),
                "server_types": sorted(SERVER_TYPES), "inventory": self.registry.status(),
                "provider_connections": "NOT_ATTEMPTED"}
