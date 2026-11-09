"""Backward-compatible facade over the Global Config Ecosystem."""

from .settings import APP_NAME, VERSION, STATUS, ENVIRONMENT
from .global_ecosystem.global_config_ecosystem.service import GlobalConfigService


class ConfigService:
    """Preserve the original ConfigService API while using centralized settings."""

    def __init__(self, service=None):
        self.service = service or GlobalConfigService(
            defaults={
                "app_name": APP_NAME,
                "version": VERSION,
                "status": STATUS,
                "environment": ENVIRONMENT,
            },
            env_prefix="APP_",
            namespace="backend",
        )

    def get_app_name(self):
        return self.service.get("app_name", APP_NAME)

    def get_version(self):
        return self.service.get("version", VERSION)

    def get_status(self):
        return self.service.get("status", STATUS)

    def initialize(self):
        return {
            "app_name": self.get_app_name(),
            "version": self.get_version(),
            "status": self.get_status(),
            "environment": self.service.get("environment", ENVIRONMENT),
        }

    def diagnostics(self):
        return self.service.diagnostics()
