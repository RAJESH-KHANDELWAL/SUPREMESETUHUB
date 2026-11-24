"""Safe ENGINE facade for infrastructure catalog and CORE validation."""
from __future__ import annotations

from typing import Any

from backend.engine.base import BaseEngine
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem import (
    GlobalInfrastructureEcosystemService,
)


class GlobalInfrastructureEngine(BaseEngine):
    """Lifecycle-managed engine with an injected CORE validation port."""

    def __init__(self, core: Any | None = None) -> None:
        super().__init__("global_infrastructure")
        self.core = core
        self.ecosystem = GlobalInfrastructureEcosystemService()

    def status(self) -> dict:
        core_status = (
            self.core.describe()["status"]
            if self.core is not None
            else "CORE_PORT_NOT_CONFIGURED"
        )
        overview = self.ecosystem.get_overview()
        return {
            **super().status(),
            "layer": "ENGINE",
            "ecosystem_id": "global-infrastructure-engine-ecosystem",
            "catalog_status": overview["status"],
            "module_count": overview["module_count"],
            "core_validation": core_status,
            "provider_operations_enabled": False,
        }

    def validate_resource(self, payload: dict) -> dict:
        if self.state != "RUNNING":
            return {"success": False, "error": "INFRASTRUCTURE_ENGINE_NOT_RUNNING"}
        if self.core is None:
            return {"success": False, "error": "INFRASTRUCTURE_CORE_PORT_NOT_CONFIGURED"}
        return self.core.validate_resource(payload)


_ENGINE: GlobalInfrastructureEngine | None = None


def get_infrastructure_engine(core: Any | None = None) -> GlobalInfrastructureEngine:
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = GlobalInfrastructureEngine(core=core)
    elif core is not None:
        _ENGINE.core = core
    return _ENGINE


__all__ = ["GlobalInfrastructureEngine", "get_infrastructure_engine"]
