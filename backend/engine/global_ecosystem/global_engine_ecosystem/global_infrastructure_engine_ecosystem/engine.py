"""Independent ENGINE facade for infrastructure execution metadata.

CORE validation is owned by the API composition layer. ENGINE does not import
or instantiate CORE, API, or infrastructure service implementations.
"""
from __future__ import annotations

from pathlib import Path

from backend.engine.base import BaseEngine


class GlobalInfrastructureEngine(BaseEngine):
    """Lifecycle-managed infrastructure engine metadata."""

    def __init__(self) -> None:
        super().__init__("global_infrastructure")

    def status(self) -> dict:
        module_count = sum(1 for _ in Path(__file__).resolve().parent.rglob("engine.py"))
        return {
            **super().status(),
            "layer": "ENGINE",
            "ecosystem_id": "global-infrastructure-engine-ecosystem",
            "catalog_status": "ENGINE_METADATA_READY",
            "module_count": module_count,
            "provider_operations_enabled": False,
        }


_ENGINE: GlobalInfrastructureEngine | None = None


def get_infrastructure_engine() -> GlobalInfrastructureEngine:
    """Return the ENGINE singleton; CORE is wired separately by API."""
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = GlobalInfrastructureEngine()
    return _ENGINE
