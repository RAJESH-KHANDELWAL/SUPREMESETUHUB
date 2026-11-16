"""Models for Bada Business configuration snapshots."""

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class BadaBusinessConfig:
    enabled: bool = False
    environment: str = "development"
    require_approval: bool = True
    request_timeout_seconds: int = 15
    default_locale: str = "en-IN"
    resource_catalog_module: str = "backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog"

    def as_dict(self) -> Mapping[str, Any]:
        return {
            "enabled": self.enabled,
            "environment": self.environment,
            "require_approval": self.require_approval,
            "request_timeout_seconds": self.request_timeout_seconds,
            "default_locale": self.default_locale,
            "resource_catalog_module": self.resource_catalog_module,
        }
