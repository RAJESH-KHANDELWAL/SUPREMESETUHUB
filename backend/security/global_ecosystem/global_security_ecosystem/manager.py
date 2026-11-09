"""Manager facade for the independent GLOBAL SECURITY ecosystem."""
from .service import GlobalSecurityEcosystemService

class GlobalSecurityEcosystemManager:
    def __init__(self, *, authorizer=None):
        self.service = GlobalSecurityEcosystemService(authorizer=authorizer)
    def register_asset(self, asset, *, replace=False): return self.service.register_asset(asset, replace=replace)
    def get_asset(self, security_id): return self.service.get_asset(security_id)
    def list_assets(self): return self.service.list_assets()
    def unregister_asset(self, security_id): return self.service.unregister_asset(security_id)
    def register_provider(self, provider_id, adapter, *, replace=False): return self.service.register_provider(provider_id, adapter, replace=replace)
    def provider_health(self, provider_id): return self.service.provider_health(provider_id)
    def execute(self, provider_id, capability, operation, payload=None, *, principal=None): return self.service.execute(provider_id, capability, operation, payload, principal=principal)
    def health(self): return self.service.health()
    def status(self): return self.service.status()
    def describe(self): return self.service.describe()

__all__ = ["GlobalSecurityEcosystemManager"]
