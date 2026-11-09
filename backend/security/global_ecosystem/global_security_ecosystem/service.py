"""Independent GLOBAL SECURITY service; no API, CORE or ENGINE implementation imports."""
from .catalog import list_providers, list_capabilities
from .models import SecurityAsset, SecurityHealth
from .registry import SecurityAssetRegistry
from .provider_registry import SecurityProviderRegistry
from .operations import SecurityOperationService

class GlobalSecurityEcosystemService:
    domain = "SECURITY"
    ecosystem = "GLOBAL_SECURITY_ECOSYSTEM"

    def __init__(self, asset_registry=None, provider_registry=None, *, authorizer=None):
        self.assets = asset_registry or SecurityAssetRegistry()
        self.providers = provider_registry or SecurityProviderRegistry()
        self.operations = SecurityOperationService(self.providers, authorizer=authorizer)

    def register_asset(self, asset: SecurityAsset, *, replace=False):
        return self.assets.register(asset, replace=replace)
    def get_asset(self, security_id):
        return self.assets.get(security_id)
    def list_assets(self):
        return self.assets.list()
    def unregister_asset(self, security_id):
        return self.assets.unregister(security_id)
    def register_provider(self, provider_id, adapter, *, replace=False):
        return self.providers.register(provider_id, adapter, replace=replace)
    def provider_health(self, provider_id):
        adapter = self.providers.get(provider_id)
        if adapter is None:
            return {"provider_id": provider_id, "status": "NOT_CONFIGURED", "healthy": False, "external_connection": "NOT_ATTEMPTED"}
        return adapter.health()
    def execute(self, provider_id, capability, operation, payload=None, *, principal=None):
        return self.operations.execute(provider_id, capability, operation, payload, principal=principal)
    def health(self):
        configured = len(self.providers.list_registered())
        status = "CONFIGURED" if configured else "NOT_CONFIGURED"
        return {"domain": self.domain, "ecosystem": self.ecosystem, "status": status, "assets": self.assets.status(), "providers": self.providers.catalog(), "capabilities": self.operations.status(), "configured_provider_count": configured, "external_probes": "NOT_ATTEMPTED"}
    def status(self):
        report = self.health()
        return {"status": report["status"], "registered_assets": report["assets"]["registered_assets"], "configured_providers": report["configured_provider_count"], "external_probes": report["external_probes"]}
    def describe(self):
        return {"domain": self.domain, "ecosystem": self.ecosystem, "providers": list_providers(), "capabilities": [{"key": x.key, "description": x.description, "access": x.access} for x in list_capabilities()], "security_assets": self.assets.status()["registered_assets"], "credential_storage": "NOT_PROVIDED_BY_THIS_PACKAGE"}

EcosystemService = GlobalSecurityEcosystemService
__all__ = ["GlobalSecurityEcosystemService", "EcosystemService"]
