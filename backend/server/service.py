"""Independent SERVER domain application service.

This is the SERVER control plane. Inventory changes are local metadata
operations; remote infrastructure actions require explicitly injected
provider/operation adapters and are never simulated.
"""
from .config import ServerConfig
from .exceptions import ServerValidationError, ServerNotFoundError
from .health import ServerHealthService
from .lifecycle import ServerLifecycleService
from .models import ServerRecord, utc_now
from .registry import ServerRegistry
from .global_ecosystem.global_server_ecosystem import (
    ServerProviderRegistry, ServerProviderGateway, ServerOperationService,
)


SERVER_TYPES = {
    "WEB", "VPS", "CLOUD", "VPN", "DATABASE", "APPLICATION",
    "DEDICATED", "CONTAINER", "EDGE", "CLOUD_WEB",
}


class ServerService:
    domain = "SERVER"
    version = "1.1.0"

    def __init__(self, registry=None, provider_registry=None, config=None,
                 operation_service=None):
        self.config = config or ServerConfig()
        self.registry = registry or ServerRegistry()
        self.providers = provider_registry or ServerProviderRegistry()
        self.provider_gateway = ServerProviderGateway(self.providers)
        self.operations = operation_service or ServerOperationService()
        self.lifecycle = ServerLifecycleService(self.registry)
        self.health_service = ServerHealthService(self.registry, self.providers)

    @staticmethod
    def _clean_required(value, field):
        clean = str(value or "").strip()
        if not clean:
            raise ServerValidationError(f"{field}_REQUIRED")
        return clean

    @staticmethod
    def _clean_metadata(metadata):
        if metadata is None:
            return {}
        if not isinstance(metadata, dict):
            raise ServerValidationError("METADATA_MUST_BE_A_DICTIONARY")
        return dict(metadata)

    def register(self, name, server_type, provider="local", region="global", metadata=None):
        clean_name = self._clean_required(name, "SERVER_NAME")
        kind = str(server_type or "").strip().upper().replace("-", "_").replace(" ", "_")
        if kind not in SERVER_TYPES:
            raise ServerValidationError(f"UNSUPPORTED_SERVER_TYPE: {kind}")
        provider_id = str(provider or "local").strip().lower()
        clean_region = self._clean_required(region or "global", "SERVER_REGION")
        if provider_id != "local":
            try:
                from .global_ecosystem.global_server_ecosystem.catalog import get_provider
                get_provider(provider_id)
            except KeyError as exc:
                raise ServerValidationError(f"UNKNOWN_SERVER_PROVIDER: {provider_id}") from exc
        record = ServerRecord(
            clean_name, kind, provider_id, clean_region,
            metadata=self._clean_metadata(metadata),
        )
        return self.registry.create(record).to_dict()

    def get(self, server_id):
        record = self.registry.get(server_id)
        if record is None:
            raise ServerNotFoundError(f"Unknown server: {server_id}")
        return record.to_dict()

    def list(self):
        return [record.to_dict() for record in self.registry.list()]

    def update(self, server_id, **changes):
        record = self.registry.get(server_id)
        if record is None:
            raise ServerNotFoundError(f"Unknown server: {server_id}")
        allowed = {"name", "server_type", "provider", "region", "metadata"}
        unknown = set(changes) - allowed
        if unknown:
            raise ServerValidationError("UNSUPPORTED_SERVER_FIELDS: " + ", ".join(sorted(unknown)))
        if "name" in changes:
            record.name = self._clean_required(changes["name"], "SERVER_NAME")
        if "server_type" in changes:
            kind = str(changes["server_type"] or "").strip().upper().replace("-", "_").replace(" ", "_")
            if kind not in SERVER_TYPES:
                raise ServerValidationError(f"UNSUPPORTED_SERVER_TYPE: {kind}")
            record.server_type = kind
        if "provider" in changes:
            provider_id = str(changes["provider"] or "").strip().lower()
            if not provider_id:
                raise ServerValidationError("SERVER_PROVIDER_REQUIRED")
            if provider_id != "local":
                from .global_ecosystem.global_server_ecosystem.catalog import get_provider
                try:
                    get_provider(provider_id)
                except KeyError as exc:
                    raise ServerValidationError(f"UNKNOWN_SERVER_PROVIDER: {provider_id}") from exc
            record.provider = provider_id
        if "region" in changes:
            record.region = self._clean_required(changes["region"], "SERVER_REGION")
        if "metadata" in changes:
            record.metadata = self._clean_metadata(changes["metadata"])
        record.updated_at = utc_now()
        self.registry.update(record)
        return record.to_dict()

    def delete(self, server_id):
        """Delete only the local inventory record; never delete remote resources."""
        if self.registry.get(server_id) is None:
            raise ServerNotFoundError(f"Unknown server: {server_id}")
        return {"server_id": str(server_id), "deleted": self.registry.delete(server_id),
                "scope": "LOCAL_INVENTORY_ONLY"}

    def start(self, server_id):
        return self.lifecycle.start(server_id)

    def stop(self, server_id):
        return self.lifecycle.stop(server_id)

    def restart(self, server_id):
        return self.lifecycle.restart(server_id)

    def register_provider(self, provider_id, adapter, *, replace=False):
        return self.providers.register(provider_id, adapter, replace=replace)

    def describe_provider(self, provider_id):
        return self.provider_gateway.describe(provider_id)

    def provider_health(self, provider_id):
        return self.provider_gateway.health(provider_id)

    def execute_provider_operation(self, provider_id, operation, payload=None):
        return self.provider_gateway.execute(provider_id, operation, payload)

    def register_operation_adapter(self, capability, adapter, *, replace=False):
        return self.operations.register_adapter(capability, adapter, replace=replace)

    def execute_operation(self, capability, operation, payload=None):
        return self.operations.execute(capability, operation, payload)

    def health(self):
        result = self.health_service.health()
        result["operations"] = self.operations.status()
        return result

    def describe(self):
        return {
            "domain": self.domain,
            "version": self.version,
            "config": self.config.describe(),
            "server_types": sorted(SERVER_TYPES),
            "inventory": self.registry.status(),
            "provider_catalog": list(self.providers.catalog()),
            "operations": self.operations.status(),
            "provider_connections": "NOT_ATTEMPTED",
            "remote_lifecycle_execution": "NOT_CONFIGURED_BY_DEFAULT",
        }


__all__ = ["ServerService", "SERVER_TYPES"]
