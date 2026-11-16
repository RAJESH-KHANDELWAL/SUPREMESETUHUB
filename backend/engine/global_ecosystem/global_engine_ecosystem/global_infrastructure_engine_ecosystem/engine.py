"""Safe ENGINE facade for infrastructure catalog and CORE validation."""
from __future__ import annotations

from backend.engine.base import BaseEngine
from backend.core.global_ecosystem.global_core_ecosystem.global_infrastructure_core_ecosystem import (
    GlobalInfrastructureCoreService,
)
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem import (
    GlobalInfrastructureEcosystemService,
)


class GlobalInfrastructureEngine(BaseEngine):
    """Lifecycle-managed metadata engine; no external provider side effects."""

    def __init__(self) -> None:
        super().__init__("global_infrastructure")
        self.core = GlobalInfrastructureCoreService()
        self.ecosystem = GlobalInfrastructureEcosystemService()

    def status(self) -> dict:
        return {
            **super().status(),
            "layer": "ENGINE",
            "ecosystem_id": "global-infrastructure-engine-ecosystem",
            "catalog_status": self.ecosystem.get_overview()["status"],
            "module_count": self.ecosystem.get_overview()["module_count"],
            "core_validation": self.core.describe()["status"],
            "provider_operations_enabled": False,
        }

    def validate_resource(self, payload: dict) -> dict:
        """Delegate resource contract validation to CORE."""
        if self.state != "RUNNING":
            return {
                "success": False,
                "error": "INFRASTRUCTURE_ENGINE_NOT_RUNNING",
            }
        return self.core.validate_resource(payload)


_ENGINE: GlobalInfrastructureEngine | None = None


def get_infrastructure_engine() -> GlobalInfrastructureEngine:
    """Return the singleton registered by the application bootstrap."""
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = GlobalInfrastructureEngine()
    return _ENGINE
