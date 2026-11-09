"""Lifecycle manager for Bada Business configuration."""

from .service import BadaBusinessConfigService
from .catalog import get_bada_business_config_catalog


class BadaBusinessConfigManager:
    def __init__(self, service=None):
        self.service = service or BadaBusinessConfigService()

    def initialize(self):
        return self.service.snapshot()

    def get(self, key, default=None):
        return self.service.get(key, default)

    def diagnostics(self):
        return self.service.diagnostics()

    def catalog(self):
        return get_bada_business_config_catalog()
