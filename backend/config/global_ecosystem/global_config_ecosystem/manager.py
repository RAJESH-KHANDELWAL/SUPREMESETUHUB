"""Lifecycle manager for the global configuration service."""

from .service import GlobalConfigService
from .catalog import get_global_config_catalog


class GlobalConfigManager:
    def __init__(self, service=None):
        self.service = service or GlobalConfigService(
            defaults={"app_name": "SUPREMESETUHUB", "version": "1.0", "environment": "development"},
            env_prefix="APP_",
            namespace="global",
        )

    def initialize(self):
        return self.service.snapshot().as_dict()

    def get(self, key, default=None):
        return self.service.get(key, default)

    def reload(self):
        return self.service.reload().as_dict()

    def diagnostics(self):
        return self.service.diagnostics()

    def catalog(self):
        return get_global_config_catalog()
